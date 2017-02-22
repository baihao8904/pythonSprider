import os
import requests
from bs4 import BeautifulSoup


if not os.path.exists('LRC'):
    os.mkdir('LRC')
file_path = os.path.join(os.path.dirname(__file__),'LRC')

headers = {'Cookie':'BDUSS=NONkRmd3QwOHpYQ0NoV1JTSGNJTkFVQ3VUVU9maXJwVFR2UEhpOTd2anE4WnRZSVFBQUFBJCQAAAAAAAAAAAEAAADI1SsFYmFpaGFvODkwNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOpkdFjqZHRYZ0; BAIDUID=A11589DFF4AA5712E4010ED9CD0E0DF0:FG=1; PSTM=1487728703; BIDUPSID=C254634169B710F61184901E4CB67E76; PSINO=2; H_PS_PSSID=1440_19034_21098_17001_21263_22036',
    'Connection':'keep-alive',
    'Content-Type':'text/html',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

host_url = 'http://music.baidu.com/artist/90654808'

web_Data = requests.get(url=host_url,headers=headers)
Soup = BeautifulSoup(web_Data.text,'lxml')
mucictitle = Soup.select('li span.song-title a')
music_ID_List = []
for item in mucictitle:
    if item.get('href')[1]=='s':
        music_ID_List.append(item.get('href'))

for item in music_ID_List:
    Song_url = 'http://music.baidu.com'+item
    Song_webdata = requests.get(Song_url,headers=headers)
    SongSoup = BeautifulSoup(Song_webdata.text,'lxml')
    lrcdata = SongSoup.select('a.down-lrc-btn')[0].get('data-lyricdata')
    lrcUrl = lrcdata.split('\"')[3]
    print(lrcUrl)
    LRC = requests.get(lrcUrl)
    LRC_webdata = BeautifulSoup(LRC.text,'lxml')
    print('请求完毕正在保存歌词')
    with open(os.path.join(file_path,'薛之谦'+'.txt'),'a+') as fp:
        fp.write(LRC_webdata.text)
        fp.write('\n')
    print('保存完毕')