# Portal de credenciamento docente (SJR) — protótipo

Site estático: HTML + SQLite no navegador (sql.js). Roda no GitHub Pages, sem servidor, e também como app Shiny (`app.R`).

Duas seções:
- **§1 Apuração do docente**: melhores artigos na janela do Art. Y, soma dos pᵢ (Art. X) escrita como equação, tabela com demonstração do percentil de cada artigo.
- **§2 Revistas por categoria**: ranking das revistas de uma categoria do SJR pelo percentil médio nos últimos 4 anos SJR carregados (top 20 ajustável, busca por nome ou ISSN, exportação CSV).

## Rodar como app Shiny (R)
```r
install.packages("shiny")            # uma vez
shiny::runApp("portal-sjr", launch.browser = TRUE)
```
Para publicar no shinyapps.io: `rsconnect::deployApp("portal-sjr")`. O `app.R` só entrega os arquivos; o cálculo continua no navegador.

## Abrir no VS Code
1. Descompacte e abra a pasta: `code portal-sjr` (ou File → Open Folder).
2. Aceite instalar a extensão recomendada **Live Server**.
3. Clique com o botão direito em `index.html` → *Open with Live Server*. O site abre em `http://127.0.0.1:5500`.

## Como publicar no GitHub Pages
1. Crie um repositório e suba o conteúdo desta pasta na raiz.
2. Settings → Pages → Source: *Deploy from a branch* → `main` / `(root)`.
3. O site fica em `https://<usuario>.github.io/<repo>/`.

Para testar local: `python3 -m http.server` nesta pasta e abrir `http://localhost:8000`
(abrir o arquivo direto, via `file://`, bloqueia o `fetch` dos CSVs).

## Acesso (login)
A página pede usuário e senha. As credenciais ficam dentro do `index.html` (bloco `AUTH`) apenas como hash (PBKDF2-SHA256, 210 mil iterações), sem texto puro.
Para trocar: `node tools/gerar_credencial.mjs "<nova senha>" "<usuario>" ["<outro usuario>"]` e commitar o `index.html` atualizado.

**Limite importante:** o GitHub Pages é estático, então a verificação acontece no navegador. Ela barra o uso casual, mas não é segurança de verdade:
quem baixar os arquivos do site consegue contorná-la, e uma senha curta pode ser descoberta por tentativa e erro a partir do hash.
Por isso, nada sensível deve ficar no repositório (só o SJR, que é público). Os dados dos docentes ficam apenas na memória do navegador.

## Base SJR
- Baixe em scimagojr.com → Journal Rankings → por **área** (sem sub-área, sem região, apenas Journals), em CSV.
- Para o ranking da §2 cobrir os 4 anos, inclua os CSVs dos 4 anos SJR mais recentes; com menos anos a página avisa e usa só os anos carregados.
- Baixe **todas as áreas** de interesse: o percentil de uma categoria só é correto se todos os periódicos dela estiverem carregados.
- Consolide os CSVs baixados (um por área e por ano) em um CSV por ano:
  `py tools/consolidar_sjr.py <pasta dos CSVs do Scimago>`. O script grava `data/sjr-<ano>.csv` e reescreve `data/manifest.json`.
  Cada periódico entra uma vez por ano (ele se repete em todas as suas áreas); o `SJR Best Quartile` fica o melhor entre as áreas.
- Gere a base que o site baixa: `node tools/gerar_db.mjs`. Ele lê os CSVs do manifest com o mesmo código do `index.html`
  e grava `data/sjr.db.gz` (SQLite compactado, cerca de 5 MB). Os percentis não vão no arquivo: o navegador os calcula
  na abertura com o SQL mostrado no portal. Sem `data/sjr.db.gz`, o portal volta a ler os CSVs do manifest.
- Só `data/sjr.db.gz` e `data/manifest.json` vão para o repositório; os CSVs ficam locais (`.gitignore`).
  Depois de trocar os CSVs, rode os dois scripts de novo e faça commit do novo `sjr.db.gz`.
- Base atual: SJR 2022–2025, as 27 áreas do Scimago (cerca de 30,5 mil periódicos por ano, 310 categorias).
- `tools/gerar_exemplo.py` gera um CSV fictício só para teste; não o liste no manifest junto com os dados reais.

## Dados dos docentes
Não ficam no repositório. O XML do Lattes é lido no navegador e só nome e artigos são aproveitados.
Em repositório público, nunca commite XML do Lattes (tem CPF, RG, filiação).

## Regras implementadas (Case ME315)
- Art. X: p_i = maior percentil do periódico entre todas as categorias do SJR (e anos carregados na janela);
  só p_i ≥ 0,25 conta; soma dos até 4 melhores ≥ 1,25.
- Percentil por categoria e ano: `1 - (posição - 1) / N`, com posição por SJR decrescente (RANK).
  Periódicos sem valor de SJR no ano ficam fora do ranking e de N, como no Scimago
  (com essa regra, o quartil derivado do percentil coincide com o quartil oficial em cerca de 97% dos casos).
- Art. Y: base 48 meses; parentalidade 72; PcD/dependente 60; licença médica soma a duração informada.

## Pontos a validar com o professor
1. Fórmula do percentil (acima) e se o SJR a usar é o de cada ano do período.
2. Acúmulo de exceções (aqui: parentalidade e PcD não se somam; médica se soma).
3. Filtro por ano-calendário (o Lattes não traz mês).
