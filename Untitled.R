library(tidyverse)
library()

d1 <- read.csv("/Users/main/Desktop/school/personal projects/research/NJEDA FALL 2024/all data/auction.csv")
d2 <- read.csv("/Users/main/Desktop/school/personal projects/research/NJEDA FALL 2024/all data/CPIAUCNS.csv")
d3 <- read.csv("/Users/main/Desktop/school/personal projects/research/NJEDA FALL 2024/all data/investments.csv")
d4 <- read.csv("/Users/main/Desktop/school/personal projects/research/NJEDA FALL 2024/all data/nj_annual_gdp.csv")
d5 <- read.csv("/Users/main/Desktop/school/personal projects/research/NJEDA FALL 2024/all data/nj_annual_median_incomes.csv")
d6 <- read.csv("/Users/main/Desktop/school/personal projects/research/NJEDA FALL 2024/all data/population.csv")


d2 <- d2 |>
  mutate(Year = year(DATE)) |>
  select(-DATE)

d5 <- d5 |>
  mutate(Year = year(DATE)) |>
  select(-DATE)

d6 <- d6 |>
  select(-X) |>
  mutate(Year = year)

df <- d2 |>
  left_join(d5, by = "Year") |>
  left_join(d6, by = "Year") |>
  select(-year)

