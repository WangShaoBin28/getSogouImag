# coding=utf-8
import requests
import json
import os
import urllib


def getSogouImag(category, length, path):
    n = length
    cat = category
    imgs = requests.get(
        'https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=' + cat + '&tag=%E5%85%A8%E9%83%A8&start=0&len=' + str(
            n) + '&width=1920&height=1080')
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    img_url_strr = []

    if not os.path.exists(path):
        os.makedirs(path)
    for j in jd:
        img_url_strr.append(j['pic_url'])
        m = 0
    for img_url in img_url_strr:
        print('***** ' + path + str(m) + '.jpg *****' + '   Downloading...')
        urllib.urlretrieve(img_url, str(path) + str(m) + '.jpg')
        m = m + 1
        print('Download complete!')


getSogouImag('壁纸', 10, 'D:/bbb/')
