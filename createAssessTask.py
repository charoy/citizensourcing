from __future__ import print_function
import os, sys
from PIL import Image
import time
import glob


__author__ = 'charoy'

githubpath="https://raw.githubusercontent.com/charoy/citizensourcing/master/corpus/assess/"

def createcsv(path,taskfile):
    tasklist=glob.glob(path+"/*.jpg")
    print(tasklist)
    count=1;

    for s in tasklist:
        filename=os.path.split(s)[1]
        taskfile.write(githubpath+filename+"\n")
        count+=1



if __name__ == "__main__":
    taskfile=open("C:/Users/charoy/PyCharmProject/mycitizensourcing/corpus/assess/task.csv","w")
    taskfile.write("img\n")
    createcsv("C:/Users/charoy/PyCharmProject/mycitizensourcing/corpus/assess",taskfile)
    taskfile.close()



