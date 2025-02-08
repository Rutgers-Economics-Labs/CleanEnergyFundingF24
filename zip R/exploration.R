#install.packages("tidyverse")
#install.packages("lubridate")
library(tidyverse)
library(lubridate)
library(cluster)
library(mgcv)
library(factoextra)


data <- read.csv("/Users/main/Documents/GitHub/CleanEnergyFundingF24/data/new/ZIP/njzip.csv")
#data <- read.csv("njzip.csv")

data <- data |>
  select(-1) |>
  mutate(date = ym(date), 
         year = year(date),
         month = month(date)) |>
  mutate(class = as.factor(class),
         year = as.factor(year),
         month = as.factor(month)) |>
  mutate(ratio = awarded / cost,
         vehicleCost = cost/numberOfVehicles,
         vehiclesAwarded = awarded/numberOfVehicles)

class <- data |>
  group_by(class) |>
  summarise(
    total_vehicles = sum(numberOfVehicles),
    total_awarded = sum(awarded),
    total_cost = sum(cost),
    avg_cost_per_vehicle = mean(vehicleCost),
    avg_award_per_vehicle = mean(vehiclesAwarded),
    avg_award_to_cost_ratio = mean(ratio)
  )

yearly <- data |>
  mutate(year = year(date)) |>
  group_by(year) |>
  summarise(
    total_vehicles = sum(numberOfVehicles),
    total_awarded = sum(awarded),
    total_cost = sum(cost), 
    avg_cost_per_vehicle = mean(vehicleCost),
    avg_award_per_vehicle = mean(vehiclesAwarded),
    avg_award_to_cost_ratio = mean(ratio)
  )






lm <- glm(numberOfVehicles ~ year + awarded + ratio + class, data = data)
summary(lm)

ggplot(data, aes(x = awarded, y = numberOfVehicles, color = class)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "lm", color = "blue") +
  labs(title = "Linear Regression: Grant Amount vs. Number of Vehicles",
       x = "Grant Amount ($)", y = "Number of Vehicles") +
  theme_minimal()



########gam()###################
#    VISUALS      #
###################

ggplot(data, aes(x = ratio)) +
  geom_histogram(binwidth = 0.05, fill = "blue", alpha = 0.5) +
  labs(title = "Distribution of Grant Coverage Ratio", x = "Ratio", y = "Frequency")

data |>
  group_by(year, month) |>
  summarize(total_awarded = sum(awarded)) |>
  ggplot(aes(x = as.Date(paste(year, month, "01", sep = "-")), y = total_awarded)) +
  geom_line(color = "blue") +
  geom_point() +
  labs(title = "Total Grant Funding Over Time", x = "Date", y = "Total Grant Amount ($)")

data |>
  group_by(year, month) |>
  summarize(total_vehicles = sum(numberOfVehicles)) |>
  ggplot(aes(x = as.Date(paste(year, month, "01", sep = "-")), y = total_vehicles)) +
  geom_line(color = "green") +
  geom_point() +
  labs(title = "Number of EVs Purchased Over Time", x = "Date", y = "Total Number of Vehicles")

ggplot(data, aes(x = class, y = awarded)) +
  geom_boxplot(fill = "lightblue") +
  labs(title = "Grant Amount by Vehicle Class", x = "Vehicle Class", y = "Grant Awarded ($)") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggplot(data, aes(x = awarded, y = numberOfVehicles)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "lm", se = FALSE, color = "blue") +
  labs(title = "Grant Amount vs. Number of Vehicles Purchased", x = "Grant Amount ($)", y = "Number of Vehicles")

ggplot(data, aes(x = cost, y = awarded)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Total Vehicle Cost vs. Grant Awarded", x = "Total Cost ($)", y = "Grant Amount ($)")

