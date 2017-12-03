import random
import json
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import os

d = {
    'params': 'EuV5GEvQEkuUMEb7Segvw/z/9RSbFD+GZg7oub0e8YWnVTQ0kSgO+NV3OKus81LtyrRQrjp6Cw8Pio2F0IDDuh0H/uqTKq650cSye2XnT9HFIyxN2Ln8mYyPO5YT3jxGsqm862vqHp2Qk63FJyK5t3KQ1Z0NU3E5p8ZLaX746Lfk518SywSS/gp3A85E8UwtD6DHdVRTtZoBKT4UrcZjvXIQoOtt+fZl9gTznBtvbJI=',
    'encSecKey': 'dd333de1c1f25be8649a14bac52c70ac31f9fbbdd505c71e2987e94fee004be7ffe5020dbd0a533deca3b819008d3ec663b78edf06bb96d6f6d52652f69ab1dca7d2cc60dc0115f20e67b4fa761814e36b7e6597f03d92b22e7dc51a6a2bdf68a5f3d10ef2fb37886b1867e41ef3e688fa649252b7d8cd62a8ed33eb97bc3621'
    }
h = {
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
musicNum = 0

#存储热门评论到本地
def storeComments(localPath,comment):
    f=open(localPath,'a',encoding='utf-8')
    f.write(comment)
    f.write('\n')
    f.close()

#获取音乐评论
def get163MusicComments(songId):
    global musicNum
    musicCommentUrl = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(songId) + '?csrf_token=f990ac0c76a871bfd2c246599d447b26'       
    html = requests.post(musicCommentUrl,data = d,headers = h)
    #bsObj = BeautifulSoup(html.text,'html.parser')
    htmlJson = json.loads(html.text)
    #print(htmlJson)
    if(len(htmlJson['hotComments'])>14):
        musicNum = musicNum + 1
        print(songId)
        for index,item in enumerate(htmlJson['hotComments']):
            localPath = 'E://musicCommentTop'+ str(index) +'.txt'
            comment = item['content']
            storeComments(localPath,comment)
        
    return 



#主函数,以参数为起始点生成songId
def index(songId):
    global musicNum
    while musicNum < 10:
        get163MusicComments(songId)
        songId = songId - 1
        #print(musicNum)
    
    #统计大小
    for i in range(1,15):
        localPath = 'E://musicCommentTop'+ str(i) +'.txt'
        fileSize = os.path.getsize(localPath)
        f = open('E://musicCommentFileSize.txt','a')
        f.write(str(fileSize))
        f.write('\n')
        f.close()

    return
        

#清空所有txt内容
def cleanStoredComments(localPath):
    f=open(localPath,'w')
    f.write('')
    f.close()

#for i in range(1,15):
#    localPath = 'E://musicCommentTop'+ str(i) +'.txt'
#    cleanStoredComments(localPath)


if __name__ == '__main__':
    index(4872637)




