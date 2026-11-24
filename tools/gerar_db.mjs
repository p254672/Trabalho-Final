// Gera data/sjr.db.gz: o banco SQLite pronto que o portal baixa ao abrir.
//
// Uso:  node tools/gerar_db.mjs
//
// Lê os CSVs listados em data/manifest.json (gerados por tools/consolidar_sjr.py),
// monta as tabelas com o MESMO código do index.html (DDL, parseCsv, carregarCsv,
// SQL_PERCENTIL são extraídos de lá, para não haver duas versões da regra),
// e grava o banco compactado. Com isso o navegador não precisa ler os CSVs
// nem calcular os percentis na abertura.
import fs from "node:fs";
import path from "node:path";
import zlib from "node:zlib";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const raiz = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const html = fs.readFileSync(path.join(raiz, "index.html"), "utf8");
const trecho = (re, nome) => {
  const m = html.match(re);
  if (!m) throw new Error(`não achei ${nome} no index.html`);
  return m[0];
};
const codigo = [
  trecho(/const normIssn[^\n]*\n/, "normIssn"),
  trecho(/const DDL = `[\s\S]*?`;/, "DDL"),
  trecho(/const SQL_PERCENTIL = `[\s\S]*?`;/, "SQL_PERCENTIL"),
  trecho(/function parseCsv\(text\)\{[\s\S]*?\n\}\n/, "parseCsv"),
  trecho(/function carregarCsv\(text, ano, nome[^)]*\)\{[\s\S]*?\n\}\n/, "carregarCsv"),
].join("\n");

const require = createRequire(import.meta.url);
const initSqlJs = require(path.join(raiz, "vendor", "sql-wasm.js"));
const SQL = await initSqlJs({ locateFile: f => path.join(raiz, "vendor", f) });

const db = new SQL.Database();
const state = { anosSjr: [], arquivosSjr: [] };
const montar = new Function("db", "state", codigo + "\nreturn { DDL, SQL_PERCENTIL, carregarCsv };");
const { DDL, SQL_PERCENTIL, carregarCsv } = montar(db, state);

db.run(DDL);
const manifest = JSON.parse(fs.readFileSync(path.join(raiz, "data", "manifest.json"), "utf8"));
for (const a of manifest.arquivos) {
  carregarCsv(fs.readFileSync(path.join(raiz, "data", a.arquivo), "utf8"), a.ano, a.arquivo, false);
  console.log(`${a.arquivo}: SJR ${a.ano}`);
}
// Os percentis NÃO vão no arquivo: o navegador os calcula na abertura com o
// SQL_PERCENTIL (rápido, e a regra continua visível no portal). O índice por
// sourceid também é recriado lá. Assim o arquivo fica bem menor.
void SQL_PERCENTIL;
db.exec("DROP INDEX IF EXISTS ix_issn_sid; DROP TABLE IF EXISTS percentil;");

// Metadados que o portal mostra (arquivos de origem) e a lista de categorias já agregada.
db.exec(`
CREATE TABLE fonte(nome TEXT, ano INTEGER, n INTEGER);
CREATE TABLE categoria_resumo AS
  SELECT categoria, COUNT(DISTINCT sourceid) AS n FROM periodico_categoria GROUP BY categoria ORDER BY categoria;`);
const pF = db.prepare("INSERT INTO fonte VALUES (?,?,?)");
state.arquivosSjr.forEach(f => pF.run([f.nome, f.ano, f.n]));
pF.free();
db.exec("VACUUM");

const bruto = Buffer.from(db.export());
const gz = zlib.gzipSync(bruto, { level: 9 });
fs.writeFileSync(path.join(raiz, "data", "sjr.db.gz"), gz);
const mb = n => (n / 1048576).toFixed(1) + " MB";
console.log(`data/sjr.db.gz: ${mb(gz.length)} (banco ${mb(bruto.length)})`);
