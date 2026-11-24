// Atualiza as credenciais (em hash PBKDF2-SHA256) dentro do index.html, sem texto puro.
// Uso:  node tools/gerar_credencial.mjs "<senha>" "<usuario1>" ["<usuario2>" ...]
// Os usuários são comparados sem diferenciar maiúsculas/minúsculas.
import { pbkdf2Sync, randomBytes } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";
const [senha, ...usuarios] = process.argv.slice(2);
if (!senha || !usuarios.length) { console.error('Uso: node tools/gerar_credencial.mjs "<senha>" "<usuario>" [...]'); process.exit(1); }
const norm = u => u.trim().toLowerCase().replace(/\s+/g, " ");
const iter = 210000, salt = randomBytes(16);
const hashes = usuarios.map(u => pbkdf2Sync(Buffer.from(norm(u) + "\u0000" + senha, "utf8"), salt, iter, 32, "sha256").toString("base64"));
const bloco = `/*AUTH:BEGIN*/\nconst AUTH = ${JSON.stringify({ salt: salt.toString("base64"), iter, hashes }, null, 2)};\n/*AUTH:END*/`;
const url = new URL("../index.html", import.meta.url);
const html = readFileSync(url, "utf8");
if (!/\/\*AUTH:BEGIN\*\/[\s\S]*?\/\*AUTH:END\*\//.test(html)) { console.error("Bloco AUTH não encontrado no index.html."); process.exit(1); }
writeFileSync(url, html.replace(/\/\*AUTH:BEGIN\*\/[\s\S]*?\/\*AUTH:END\*\//, () => bloco));
console.log("Credenciais atualizadas no index.html para", usuarios.length, "usuário(s).");
