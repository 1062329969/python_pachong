import requests
import re
import pymysql
from bs4 import BeautifulSoup


config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'test',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

# print(soup)#可以看到网页的内容
def getImgUrl(url,params=None):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    arr = [];
    for article in soup.select('article.photo-item'):#爬取一些新闻信息
        for img in article.select('img'):
            imgre = re.findall(r'(.*)\?', img['src'])
            print(imgre)
            arr.append(imgre[0])
    if(len(arr)):
        return arr
    else:
        return False;


allimgurl = []
page = 1
while(1):
    url = "https://www.pexels.com/search/design/?page="+str(page)
    imgurl = getImgUrl(url)
    if(imgurl==False):
        break
    else:
        allimgurl+=imgurl
    page = page+1
# print(allimgurl)
