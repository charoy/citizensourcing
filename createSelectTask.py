from __future__ import print_function
import os, sys
from PIL import Image
import time
import glob
print

__author__ = 'charoy'

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



if __name__ == "__main__":
    images=glob.glob("C:/Users/charoy/PyCharmProject/mycitizensourcing/corpus/select/1/*_n.jpg")
    merge(images,"C:/Users/charoy/PyCharmProject/mycitizensourcing/corpus/select/1/result1.jpg")
