import os
import urllib.request

import time

imgpath = './img'
if not os.path.exists('./img'):
    os.mkdir('./img')
file = open("./heros.txt", 'r', encoding='utf-8')
imgList = []
nameList = []
for line in file.readlines():
    nameList.append(line.split("\t")[2].strip())
    imgList.append(line.split("\t")[-1].strip())
while len(nameList)>0:
    print(nameList[-1])
    imgPath = imgpath + "/" + nameList[-1] + '.png'
    with open(imgPath,"wb") as fpimg:
        try:
            nameList.pop()
            response = urllib.request.urlopen(imgList.pop())
            fpimg.write(response.read())
            time.sleep(5)
        except:
            print('deal with %s error' %nameList[-1])