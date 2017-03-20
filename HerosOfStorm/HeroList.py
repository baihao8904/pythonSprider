from selenium import webdriver
from bs4 import BeautifulSoup

class hero_url(object):
    name = None
    agname  = None
    heroHref = None
    imgHref = None

browser = webdriver.PhantomJS()
browser.get('http://heroes.blizzard.cn/heroes/')
browser.implicitly_wait(20)
html = browser.page_source
"""
<div class="hero_list_item" data-ename="lucio" data-role="support" data-game="overwatch" data-name="卢西奥自由战士DJlucio">
<a href="/heroes/lucio">
<div class="hero_list_box">
<img src="http://heroes.nos.netease.com/2/cms/hero/lucio/Lucio.jpg">
</div><h4>卢西奥</h4>
<div class="hero_heading">
<span class="hero_icon icon_support_small">
</span><i>自由战士DJ</i>
</div><div class="hover-border"></div><span class="hero_free_icon"></span></a></div>
"""
# heroElements = browser.find_elements_by_xpath('//div[@class="hero_list_item"]')
# for item in heroElements:
#     heroInfo = hero_url()
#     heroInfo.name = item.find_element_by_xpath('.//h4').text.strip().split("\n")[0]
#     print(heroInfo.name)
Soup = BeautifulSoup(html,"lxml")
herosInfo = Soup.select("div.hero_list_item")
for item in herosInfo:
    heroInfo = hero_url()
    heroInfo.name = item.select("a h4")[0].text
    heroInfo.agname = item.select("div.hero_heading i")[0].text
    heroInfo.heroHref = item.select('a')[0].get('href')
    heroInfo.imgHref = item.select('a div img')[0].get('src')
    with open('StormOfHeros.txt','a+') as fp:
         fp.write(heroInfo.name+'\t'+heroInfo.agname+'\t'+heroInfo.heroHref+"\t" \
                  +heroInfo.imgHref)
         fp.write('\n')