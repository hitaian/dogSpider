#coding:utf-8
import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup
import os

class spider:
    def __init__(self,url):
        pass
    def makeOpener(self):
        #proxy_support = urllib.request.ProxyHandler({'http': '1270.0.0.1:7777'})
        headers = {
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8',
                'Cache-Control':'max-age=0',
                'Connection':'keep-alive',
                'Host':'w2.aqu1024.club',
                'Upgrade-Insecure-Requests':'1',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36}'
        }
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        header = []
        for key,value in headers.items():
            elem = (key,value)
            header.append(elem)
        opener.addheaders =header
        return  opener

    #打开链接
    def openLink(self,link):
        link = link
        oper = self.makeOpener()
        data = oper.open(link,timeout=1000).read().decode('utf-8','ignore')
        soup = BeautifulSoup(data,'lxml')

        #link = soup.select()
        #print(soup.prettify())
        link = soup.find_all('a',id=True,href=True)
        for i in link:
                print (i)


    def guolv(self,tag):
        return not tag.has_attr()

        #获取内容页面链接

        #self.getContentLink(soup)

    #获取内容页链接
    def getContentLink(self,data):
        pass
    def downTorrent(self,data):

        pass


    def getType(self):
        pass


    #创建文件夹
    def newDir(self,name):
        if os.path.exists(name):
            print('已有这个文件夹')
        else:
            os.makedirs(name)
            print('创建'+ name + '成功')




    def getList(self):
        pass
