library(psych)
runs <- read.csv(file="info.csv",header=T,sep=",")
score <- table(runs$info,runs$task_id)
summary(score)

aggscore <- aggregate(runs$info,by=list(runs$task_id), FUN=list,rm=T)

aggscore


boxplot(info~task_id,data=runs,main="score by photo")