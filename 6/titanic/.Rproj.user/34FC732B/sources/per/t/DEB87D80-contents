library("ggplot2")
data <- read.csv("titanic_train.csv")

dev <- round(sd(data$Fare), digits = 2)
med <- round(median(data$Fare), digits = 2)

qplot(x=c("deviation", "median"), y=c(dev, med), geom="col", xlab = "")

med 
dev
