library("ggplot2")
data <- read.csv("titanic_train.csv")
males  = data[which(data$Sex == "male"),]

r <- lapply(males$Name, function(x) tail(strsplit(as.character(x), " ")[[1]], 1))

sortedNames <- sort(table(as.character(r)), decreasing = TRUE)

a <- sortedNames[1:5]

qplot(x=rownames(a), y=a, geom="col", fill=factor(a))
