import os
import urllib.request

from bs4 import BeautifulSoup
import requests

if not os.path.exists('./img'):
    os.mkdir('./img')

hosturl = "http://heroes.blizzard.cn"
OriginData = open('./StormOfHeros.txt','r')
for line in OriginData.readlines():
    heroName = line.split('\t')[0]
    heroAName = line.split('\t')[1]
    herohref = line.split('\t')[2]
    imghref = line.split('\t')[3]
    web_data = requests.get(hosturl+herohref)
    Soup = BeautifulSoup(web_data.text,'lxml')
    heroAblitys = Soup.select('div.s_cont_info.fl')
    shanghai = len(heroAblitys[0].select("div.stat_bar.clearFix div.cherry_bar"))
    fuzhu = len(heroAblitys[1].select("div.stat_bar.clearFix div.blue_bar"))
    cunhuo = len(heroAblitys[2].select("div.stat_bar.clearFix div.purple_bar"))
    shangshounandu = len(heroAblitys[3].select("div.stat_bar.clearFix div.purple_bar"))
    print(imghref)
    try:
        response = urllib.request.urlopen(imghref)
        with open('./img/'+heroName+'.jpg','wb') as fimg:
            fimg.write(response.read())
    except:
        pass
    with open('./heroAvility.txt','a+') as fp:
        fp.write(heroName+'\t'+heroAName+'\t'+'伤害能力：'+str(shanghai)+'\t' \
                 +'辅助:'+str(fuzhu)+'\t'+'存活：'+str(cunhuo)+'\t'+'难度：'+str(shangshounandu))
        fp.write('\n')