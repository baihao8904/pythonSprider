import requests
from bs4 import BeautifulSoup
import time
import csv
import collections

oneHeroUrl = "http://db.dota2.uuu9.com/hero/show/GA"
heroWeb_data = requests.get(oneHeroUrl)
heroSoup = BeautifulSoup(heroWeb_data.text,'lxml')
    #名称称号
heroName = heroSoup.select("div.bord span.name")[0].text.split('\n')[0].strip()
print(heroName)
heroChenghao = heroSoup.select("div.bord span.name")[0].text.split('\n')[1].strip()
    #特点标签
heroTags = heroSoup.select('div.bord div.tag a')
tagList = []
for item in heroTags:
    tagList.append(item.text.strip())
herotag = ",".join(tagList)
heroRanks = heroSoup.select("div.content.jianbg.cl ul li")
herorankList = []
for item in heroRanks:
    if len(item.select("em"))>0:
        ranksName = item.select("em")[0].text.strip()
        ranksNum = item.select('b')[0].text.strip().split("\n")[0].strip()
        herorankList.append(ranksName+ranksNum)
heroimg = heroSoup.select("span.heropic img")[0].get("src")
str = str(oneHeroUrl.split("/")[-1] + '\t' + heroName + '\t' + heroChenghao + '\t' + herotag + '\t' + ','.join(herorankList) + '\t'+heroimg)
with open('heros.txt', "a+") as fp:
    fp.write(str)
    fp.write("\n")