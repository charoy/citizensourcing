from __future__ import print_function
import os, sys
from PIL import Image
import time
import glob
print

__author__ = 'charoy'

githubpath="https://raw.githubusercontent.com/charoy/citizensourcing/master/corpus/select/"

def merge(imgs,newimg):
    band_size = 30
    images = map(Image.open,imgs)
    print(images)
    mh = min(i.size[1] for i in images)
    print(mh)
    w = 0
    out_images = []

    for img in images:
        if img.size[1] > mh:
            rat = float(img.size[0]) / float(img.size[1])
            out = img.resize((int(mh * rat), mh))
        else:
            out = img
        w += out.size[0]
        out_images.append(out)

    w += (len(images) -1) * band_size

    result = Image.new("RGBA", (w, mh))

    x = 0
    for i in out_images:
        result.paste(i, (x, 0))
        x += i.size[0] + band_size

    result.save(newimg)

import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

def createtasks(path,taskfile):
    imgpath=path+"/*_n.jpg"
    images=glob.glob(imgpath)
    result=findsubsets(images,2)
    dirname=os.path.split(path)[1]
    print(dirname)
    count=0;
    for s in result:
        merge(s,path+"/result"+str(count)+".jpg")
        taskfile.write("2;"+githubpath+dirname+"/result"+str(count)+".jpg\n")
        count+=1


def createcsv(path,taskfile):
    tasklist=glob.glob(path+"/*")
    print(tasklist)
    count=1;
    for i in tasklist:
        createtasks(i,taskfile)


if __name__ == "__main__":
    images=glob.glob("C:/Users/charoy/PyCharmProject/mycitizensourcing/corpus/select/1/*_n.jpg")
    merge(images,"C:/Users/charoy/PyCharmProject/mycitizensourcing/corpus/select/1/result1.jpg")
    taskfile=open("C:/Users/charoy/PyCharmProject/mycitizensourcing/corpus/select/task.csv","w")
    taskfile.write("len;img\n")
    createcsv("C:/Users/charoy/PyCharmProject/mycitizensourcing/corpus/select",taskfile)
    taskfile.close()
