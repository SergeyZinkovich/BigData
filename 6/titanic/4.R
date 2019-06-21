library("ggplot2")
data <- read.csv("titanic_train.csv")

young <- data[which(data$Age < 30),]
old <- data[which(data$Age > 60),]

ggplot(data=young, aes(x=factor(young$Survived), fill=Survived))+geom_bar()
ggplot(data=old, aes(x=factor(old$Survived), fill=Survived))+geom_bar()
