# Portal de credenciamento docente (ME315) servido como app Shiny.
#
# O front (index.html) é estático: o cálculo roda no navegador com SQLite (sql.js).
# Este app só entrega os arquivos, para rodar com shiny::runApp() ou publicar
# no shinyapps.io. O mesmo diretório continua funcionando no GitHub Pages.
#
# Rodar local:   shiny::runApp(".", launch.browser = TRUE)
# Publicar:      rsconnect::deployApp(".", appName = "portal-sjr")

library(shiny)

raiz <- normalizePath(".", winslash = "/")

# As pastas são expostas no mesmo caminho relativo que o index.html usa.
addResourcePath("vendor", file.path(raiz, "vendor"))
addResourcePath("data", file.path(raiz, "data"))

ler_pagina <- function() {
  linhas <- readLines(file.path(raiz, "index.html"),
                      encoding = "UTF-8", warn = FALSE)
  paste(linhas, collapse = "\n")
}

ui <- function(req) {
  # Documento HTML completo, entregue tal como está (sem a moldura
  # Bootstrap do Shiny). Lido a cada acesso, então edições aparecem
  # sem reiniciar o app.
  httpResponse(200L, "text/html; charset=UTF-8", ler_pagina())
}

server <- function(input, output, session) {}

shinyApp(ui, server, options = list(launch.browser = interactive()))
