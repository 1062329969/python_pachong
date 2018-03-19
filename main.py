#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "zhangyouliang"

import re
import os
import requests

save_path="D:/"

def getHTMLText(url,params=None):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        r = requests.request('GET',url,params=params,timeout=30,headers=headers)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

def getImages(html):
    reg = r'srcset="(.+?\.jpeg)?.*"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    if not os.path.isdir(save_path):
        os.makedirs(save_path)
    paths = save_path+'/'
    x = 0
    for imgurl in imglist:
        if(imgurl==''):
            continue;
        ir = requests.get(imgurl)
        if ir.status_code ==200:
            open(paths+str(x)+'.jpeg','wb').write(ir.content)
            x = x+1


if __name__ =='__main__':
    url="https://www.pexels.com/search/design/"
    rsp = getHTMLText(url)
    getImages(rsp)
