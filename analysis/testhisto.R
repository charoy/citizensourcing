library(psych)
runs <- read.csv(file="info.csv",header=T,sep=",")
score <- table(runs$info,runs$task_id)
summary(score)

aggscore <- aggregate(runs$info,by=list(runs$task_id), FUN=list,rm=T)

aggscore

hist(runs$info, xlab = "Grade",
  main = "Histogram of Photo Scores")