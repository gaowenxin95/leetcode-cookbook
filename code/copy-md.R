rmarkdown::render("commit.Rmd")
library(magrittr)
readr::read_lines("commit.md") %>%
    clipr::write_clip(allow_non_interactive = TRUE)
