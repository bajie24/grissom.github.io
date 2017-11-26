import random
import json
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

d = {
    'params': '此处当有params',
    'encSecKey': '此处当有encSecKey'
    }
h = {
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
musicNum = 0

#存储热门评论到本地
def storeComments(localPath,comment):
    f=open(localPath,'a')
    f.write(comment)
    f.write('\n')
    f.close()

#获取音乐评论
def get163MusicComments(songId):
    global musicNum
    musicCommentUrl = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(songId) + '?csrf_token=此处当有token'       
    html = requests.post(musicCommentUrl,data = d,headers = h)
    #bsObj = BeautifulSoup(html.text,'html.parser')
    htmlJson = json.loads(html.text)
    #print(htmlJson)
    if(len(htmlJson['hotComments'])>14):
        musicNum = musicNum + 1
        print(musicNum)
        for index,item in enumerate(htmlJson['hotComments']):
            localPath = 'E://musicCommentTop'+ str(index) +'.txt'
            comment = item['content']
            storeComments(localPath,comment)
    else:
        return
    return 



#主函数,以参数为起始点生成songId
def index(songId):
    global musicNum
    while musicNum < 10:
        get163MusicComments(songId)
        songId = songId - 1
        print(musicNum)
        
    
index(4875075)

#清空所有txt内容
def cleanStoredComments(localPath):
    f=open(localPath,'w')
    f.write('')
    f.close()

#for i in range(1,15):
#    localPath = 'E://musicCommentTop'+ str(i) +'.txt'
#    cleanStoredComments(localPath)


