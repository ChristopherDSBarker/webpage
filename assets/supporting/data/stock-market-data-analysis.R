#Christopher Barker
#Dr. Cao
#Data 133
#Project 1
#need these
install.packages("ggplot2")
library(dplyr)
library(ggplot2)

#Load all the files
aaplData <- read.csv("AAPL.csv")
babaData <- read.csv("BABA.csv")
zmData <- read.csv("ZM.csv")
twtrData <- read.csv("TWTR.csv")
fbData <- read.csv("FB.csv")
pctyData <- read.csv("PCTY.csv")
msftData <- read.csv("MSFT.csv")
biduData <- read.csv("BIDU.csv")
amznData <- read.csv("AMZN.csv")
adbeData <- read.csv("ADBE.csv")




#Reading in some data
head(aaplData)
head(babaData)
head(zmData)
head(twtrData)
head(fbData)
head(pctyData)
head(msftData)
head(biduData)
head(amznData)
head(adbeData)

#check for any NA in data
anyNA(aaplData)
anyNA(babaData)
anyNA(zmData)
anyNA(twtrData)
anyNA(fbData)
anyNA(pctyData)
anyNA(msftData)
anyNA(biduData)
anyNA(amznData)
anyNA(adbeData)

#gives mean, median, etc
summary(aaplData)
summary(babaData)
summary(zmData)
summary(twtrData)
summary(fbData)
summary(pctyData)
summary(msftData)
summary(biduData)
summary(amznData)
summary(adbeData)

#attempt at sd
opendata <- aaplData$Open  
opendata <- opendata[!is.na(opendata)]
opendata <- opendata[!is.nan(opendata)]
opendata <- opendata[!is.null(opendata)]
print(opendata)
sd(opendata)

# ggplots

#string convertion
aaplData$Date <- as.Date(aaplData$Date)

#remove NA
aaplData <- aaplData %>%
  filter(!is.na(Open) & !is.na(Close) & !is.na(High) & !is.na(Low))

#GRAPH 1
#Candlestick plot for aapl aka apple


# calculate approximate width based on spacing of dates
# Calculate dynamic candle width in days
width <- 0.8 * median(diff(as.numeric(aaplData$Date)))

# Candlestick plot
aaplData$Date <- as.Date(aaplData$Date)
aaplData <- aaplData %>%
  filter(!is.na(Open) & !is.na(Close) & !is.na(High) & !is.na(Low))

ggplot(aaplData, aes(x = Date)) +
  geom_segment(aes(y = Low, yend = High, xend = Date), color = "black") +
  geom_rect(aes(ymin = pmin(Open, Close),
                ymax = pmax(Open, Close),
                xmin = Date - 0.7,
                xmax = Date + 0.7,
                fill = Close > Open)) +
  scale_fill_manual(values = c("TRUE" = "green", "FALSE" = "red")) +
  labs(title = "Apple Candlestick Chart", x = "Date", y = "Price (USD)") +
  theme_minimal()

#GRAPH TWO
fbData$Date <- as.Date(fbData$Date)  # formatted date

# plot
ggplot(fbData, aes(x = Date, y = Close)) + 
  geom_line(color = "blue") +
  labs(title = "Facebook Closing Price Over Time", 
       x = "Date",
       y = "Closing Price (USD)") +
  theme_minimal()

#GRAPH THREE 
amznData$Date <- as.Date(amznData$Date)
#Daily returns
amznData <- amznData %>%
  arrange(Date) %>%
  mutate(Return = (Close / lag(Close)) - 1)
#histogram
ggplot(amznData, aes(x = Return)) + 
  geom_histogram(binwidth = 0.01, fill = "yellow", color = "black") + 
  labs(title = "Amazon Histogram Daily Returns",
       x = "Daily Return",
       y = "Frequency") + 
  theme_minimal()


drawFigure1 <- function(filename, startRow, endRow) {
  # Load file
  df <- read.csv(filename)
  
  # Conversion of data type
  df$Date <- as.Date(df$Date)
  
  # Subset startRow and endRow
  df <- df[startRow:endRow, ]
  
  # Filter out rows with missing values
  df <- df %>%
    filter(!is.na(Open) & !is.na(Close) & !is.na(High) & !is.na(Low))
  
  # Calculate width for candlestick bars based on date 
  width <- 0.8 * median(diff(as.numeric(df$Date)))
  
  # Create candlestick chart with colored rectangles
  ggplot(df, aes(x = Date)) +
    geom_segment(aes(y = Low, yend = High, xend = Date), color = "black") +
    geom_rect(aes(ymin = pmin(Open, Close),
                  ymax = pmax(Open, Close),
                  xmin = Date - width / 2,
                  xmax = Date + width / 2,
                  fill = Close > Open)) +
    scale_fill_manual(values = c("TRUE" = "green", "FALSE" = "red")) +
    labs(title = paste("Candlestick Chart:", filename),
         x = "Date", y = "Price (USD)") +
    theme_minimal()
}

drawFigure2 <- function(filename, startRow, endRow) {
  # Load file
  df <- read.csv(filename)
  
  # Conversion
  df$Date <- as.Date(df$Date)
  
  # rows between startRow and endRow
  df <- df[startRow:endRow, ]
  
  # Plot Close price over time as a blue line 
  ggplot(df, aes(x = Date, y = Close)) + 
    geom_line(color = "blue") +
    labs(title = paste("Closing Price Over Time:", filename),
         x = "Date", y = "Closing Price (USD)") +
    theme_minimal()
}

drawFigure3 <- function(filename, startRow, endRow) {
  # Load data file
  df <- read.csv(filename)
  
  # Conversion
  df$Date <- as.Date(df$Date)
  
  # calculate daily returns based on Close price
  df <- df[startRow:endRow, ] %>%
    arrange(Date) %>%
    mutate(Return = (Close / lag(Close)) - 1)
  
  # histogram of daily returns with yellow fill and black border
  ggplot(df, aes(x = Return)) +
    geom_histogram(binwidth = 0.01, fill = "yellow", color = "black") +
    labs(title = paste("Histogram of Daily Returns:", filename),
         x = "Daily Return", y = "Frequency") +
    theme_minimal()
}











