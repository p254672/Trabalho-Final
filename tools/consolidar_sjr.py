"""Consolida os CSVs do Scimago (um por area e por ano) em um CSV por ano.

Uso:  python tools/consolidar_sjr.py <pasta com os CSVs baixados> [pasta de saida]

Um periodico aparece em todas as areas a que pertence, sempre com a mesma
linha (Categories traz todas as categorias). Aqui cada Sourceid entra uma
vez por ano, so com as colunas que o portal usa. Tambem atualiza
data/manifest.json.
"""
import csv, json, re, sys
from pathlib import Path

COLS = ["Sourceid", "Title", "Type", "Issn", "SJR", "SJR Best Quartile", "Categories", "Areas"]
IQ = COLS.index("SJR Best Quartile")

origem = Path(sys.argv[1])
saida = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parent.parent / "data"

por_ano = {}
for f in sorted(origem.rglob("*.csv")):
    m = re.search(r"scimagojr\s+(\d{4})", f.name)
    if not m:
        print("ignorado (sem ano no nome):", f.name)
        continue
    ano = int(m.group(1))
    dados = por_ano.setdefault(ano, {"linhas": {}, "arquivos": 0})
    dados["arquivos"] += 1
    with open(f, encoding="utf-8-sig", newline="") as fh:
        r = csv.reader(fh, delimiter=";")
        h = [c.strip() for c in next(r)]
        ix = {c: h.index(c) for c in COLS}  # primeira ocorrencia (Publisher aparece duas vezes)
        for x in r:
            if len(x) < len(h) - 2:
                continue
            sid = x[ix["Sourceid"]].strip()
            linha = [x[ix[c]] for c in COLS]
            ant = dados["linhas"].get(sid)
            if ant is None:
                dados["linhas"][sid] = linha
                continue
            # "SJR Best Quartile" e o melhor quartil dentro da area do arquivo;
            # fica o melhor entre todas as areas. As demais colunas devem bater.
            if [v for i, v in enumerate(ant) if i != IQ] != [v for i, v in enumerate(linha) if i != IQ]:
                print(f"aviso: Sourceid {sid} difere entre areas em {ano} ({f.name})")
            if re.fullmatch(r"Q[1-4]", linha[IQ]) and (not re.fullmatch(r"Q[1-4]", ant[IQ]) or linha[IQ] < ant[IQ]):
                ant[IQ] = linha[IQ]

manifest = []
for ano in sorted(por_ano):
    d = por_ano[ano]
    nome = f"sjr-{ano}.csv"
    with open(saida / nome, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter=";", quoting=csv.QUOTE_MINIMAL)
        w.writerow(COLS)
        w.writerows(d["linhas"].values())
    manifest.append({"ano": ano, "arquivo": nome})
    print(f"{ano}: {d['arquivos']} arquivos de area, {len(d['linhas'])} periodicos -> {nome}")

with open(saida / "manifest.json", "w", encoding="utf-8") as fh:
    json.dump({"arquivos": manifest}, fh, ensure_ascii=False, indent=2)
    fh.write("\n")
