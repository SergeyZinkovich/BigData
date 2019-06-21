library("ggplot2")
data <- read.csv("titanic_train.csv")

males  = data[which(data$Sex == "male"),]
females  = data[which(data$Sex == "female"),]

ggplot(data=males, aes(x=factor(males$Survived), fill=Survived))+geom_bar()
ggplot(data=females, aes(x=factor(females$Survived), fill=Survived))+geom_bar()

