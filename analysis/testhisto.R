library(psych)
runs <- read.csv(file="../taskruns/tests/crowdsourcing4_task_run.csv",header=T,sep=",")
score <- table(runs$task_run__info)
summary(score)
hist(runs$task_run__info, xlab = "Grade",
  main = "Histogram of Photo Scores")