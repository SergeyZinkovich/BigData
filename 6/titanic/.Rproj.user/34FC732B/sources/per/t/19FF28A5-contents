library("ggplot2")
data <- read.csv("titanic_train.csv")

qplot(factor(data$Pclass), data = data, geom = "bar", fill=data$Pclass)
table(data$Pclass)
table(data$Sex)
females = data[which(data$Sex == 'female'),]
males = data[which(data$Sex == 'male'),]

qplot(factor(males$Pclass), data = males, geom = "bar", main = "Males", fill=males$Pclass)
qplot(factor(females$Pclass), data = females, geom = "bar", main = "Females", fill=females$Pclass)

table(females$Pclass)

table(males$Pclass)

