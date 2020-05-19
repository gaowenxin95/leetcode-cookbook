library(tidyverse)
fs::dir_ls(".", regexp = "\\.md$") %>%
    str_subset("README|LICENSE", negate = TRUE) %>%
    map(file.remove)
