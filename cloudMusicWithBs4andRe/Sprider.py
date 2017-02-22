from bs4 import BeautifulSoup
import requests
import os


headers = {'Cookie':' os=pc; deviceId=B55AC773505E5606F9D355A1A15553CE78B89FC7D8CB8A157B84; osver=Microsoft-Windows-8-Professional-build-9200-64bit; appver=1.5.0.75771; usertrack=ezq0alR0yqJMJC0dr9tEAg==; MUSIC_A=088a57b553bd8cef58487f9d01ae',
    'Connection':'keep-alive',
    'Content-Type':'text/html',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
host_url = 'http://www.kuwo.cn/geci/a_89199/'
web_data = requests.get(host_url,headers=headers)
Soup = BeautifulSoup(web_data.text,'lxml')
music_url = Soup.select('ul li.song a')
title_dict = {}
for item in music_url:
    if item.text not in title_dict:
        title_dict[item.text] = item.get('href')
    # print(item.get('href'))
    # print(item.text)

if not os.path.exists('geci'):
    os.mkdir('geci')

for item in title_dict:
    print(item)
    print(title_dict[item])
    geci_web = requests.get(title_dict[item])
    geciSoup = BeautifulSoup(geci_web.text,'lxml')
    lrc = geciSoup.select('div.lrc br')
    print(lrc[0])
    break