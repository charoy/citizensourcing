library(psych)
library(jsonlite)
runs <- fromJSON("../taskruns/moretests150715/crowdsourcing4_task_run.json")
runs

score <- table(runs$info)
score
summary(score)
hist(score, xlab = "Grade",
  main = "Histogram of Photo Scores")