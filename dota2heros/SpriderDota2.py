import os

import requests
from bs4 import BeautifulSoup
import time
import csv
import collections
base_url = "http://db.dota2.uuu9.com"
headers ={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        'Connection':"keep-alive",
    }
# web_Data = requests.get(base_url,headers=headers)
# Soup = BeautifulSoup(web_Data.text,'lxml')
# hero_url = Soup.select("div#herolist1 a")
# heroUrlList = []
# for aurl in hero_url:
#     heroUrlList.append(aurl.get("href"))
# print(heroUrlList)
heroUrlList = ['/hero/show/Huskar', '/hero/show/OK', '/hero/show/CG', '/hero/show/DK', '/hero/show/Lich', '/hero/show/BM', '/hero/show/Coco', '/hero/show/SNK', '/hero/show/TH', '/hero/show/SG', '/hero/show/Tiny', '/hero/show/Sven', '/hero/show/ES', '/hero/show/SK', '/hero/show/Pud', '/hero/show/AM', '/hero/show/AXE', '/hero/show/Bane']
for item in heroUrlList:
    print("dealwith"+item)
    oneHeroUrl = base_url+item
    heroWeb_data = requests.get(oneHeroUrl,headers=headers)
    heroSoup = BeautifulSoup(heroWeb_data.text,'lxml')
    #名称称号
    heroName = heroSoup.select("div.bord span.name")[0].text.split('\n')[0].strip()

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
        if len(item.select("em")) > 0:
            ranksName = item.select("em")[0].text.strip()
            ranksNum = item.select('b')[0].text.strip().split("\n")[0].strip()
            herorankList.append(ranksName+ranksNum)
    heroimg = heroSoup.select("span.heropic img")[0].get("src")
    with open('heros.txt',"a+") as fp:
        fp.write(oneHeroUrl.split("/")[-1]+'\t'+ heroName+'\t'+heroChenghao+'\t'+herotag+'\t'+','.join(herorankList)+'\t'+heroimg)
        fp.write("\n")

time.sleep(5)