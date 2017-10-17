#coding:utf-8
import urllib.request
import urllib.parse
import http.cookiejar
from bs4 import BeautifulSoup
import os
import re
from config import *
import socket
#socket.setdefaulttimeout(10.0)

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

    #打开内容列表链接
    def openLink(self,link,type):
        type = type
        alllink = link
        oper = self.makeOpener()
        try:
            data = oper.open(alllink,timeout=15000).read().decode('utf-8','ignore')
        except urllib.request.HTTPError as e:
            print(e.code)
        soup = BeautifulSoup(data,'lxml')
        #获取总页数
        pagenum = soup.find_all(href = re.compile('page')) # 获取最后一页<a href="thread.php?fid=5&amp;page=140" style="font-weight:bold">»</a>
        page = self.getPagenum(pagenum)  # 获取总页数
        alllist = self.getAlllink(page,alllink)  #获取所有链接
        alllen = len(alllist)
        howpage = 0
        for all in alllist:
            contentLink = []
            print('Link'+ all)
            try:
                data = oper.open(all, timeout=15000).read().decode('utf-8', 'ignore') #打开page1
            except urllib.request.HTTPError as e:
                print(e.code)
            soup = BeautifulSoup(data, 'lxml')
            link = soup.find_all(href=re.compile('html'), id=True)
            #获取 href 的地址 并返回
            listLink = [tag.get('href') for tag in link] #htm_data/5/1710/824771.html
            url = config.url
            for i in listLink:
                contentLink.append(url+i) #http://xxx.com/htm_data/5/1710/824771.html
            print('正在下载第%d页'%(howpage+1))
            howpage += 1
            self.getContent(contentLink,type)           #[xx.com/1.html,xx.com/2.html]


    #解析所有的东东
    def getContent(self,contentLink,movieType):
        link = contentLink
        for i in link:
            oper = self.makeOpener()
            try:
                data = oper.open(i).read().decode('utf-8','ignore')
            except urllib.request.URLError as e:
                print(e.code)
            soup = BeautifulSoup(data, 'lxml')
            title = soup.title.get_text()
            title = self.takeTitle(title)
            if (self.contentDir(movieType, title)) == 0:
                continue
            else:
                img = soup.find_all('img', onload=True, onclick=True)  # 找到所有Image标签
                img = [tag.get('src') for tag in img]  # 得到图片下载地址
                self.download(img, movieType, title)  # 下载图片
                ##self.getContent(contentLink, movieType)
                torrentLink = soup.find_all(href=re.compile('www3'))  # 找到种子链接
                torrentName = self.get_torrentname(torrentLink)  # 得到精确的种子下载地址
                self.download_torrent(torrentName, movieType, title) # 如果出错就继续


#从第一页开始，获取所有列表链接，并返回列表
    def getAlllink(self,page,alllink):
        alllink = alllink
        p = 1
        alllist = []
        while p <= int(page):
            link = alllink + '&page='+str(p)
            p = int(p) + 1
            alllist.append(link)
        return  alllist

    def getPagenum(self,pagenum):
        pagenum = pagenum
        page = [tag.get('href') for tag in pagenum]
        page = page[-1]
        page = page.split('=')
        page = page[-1]
        return page

#下载图片
    def download(self,link,movietype,title):
        link = link
        path = movietype + '/' + title
        for i in link:

            filename = i.split('/')
            filename = filename [-1]
            try:
                urllib.request.urlretrieve(i, path+'/'+ filename)
            except urllib.request.HTTPError as e:
                print(e.code)

            print ('下载成功' + filename )

    # 获取种子名称
    def get_torrentname(self,link):
        for tag in link:
            link = tag.get('href')
            link = link.split('/')
            name = link[-1]
            return name

    #下载种子
    def download_torrent(self,name,movietype,title):
        print('下载种子中。。。。。')
        path = movietype + '/' + title # /亚洲无码/小哥可/
        name = name #OXWU4St.html
        url = config.torrent_url_down #'http://www3.uptorrentfilespacedownhostabc.club/updowm/down.php'
        torrent_file = config.torrent_url #http://www3.uptorrentfilespacedownhostabc.club/updowm/file.php/
        name_s = name.split('.')
        torrent_name = name_s[-2]

        data = {
            'type' : 'torrent',
            'id': torrent_name,
            'name':'xp1024.com_HEYZO-0846-FHD'
        }
        data  = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request(url,data=data)
        req.add_header ('Referer', torrent_file + name)
        req.add_header('Origin',config.torrent_origin)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')

        try :
            r = urllib.request.urlopen(req,timeout=15000) #打开这个链接
        except urllib.request.HTTPError as e:
            print(e.code)



        if 'Content-Disposition' in r.info():
            downinfo = (r.info().get('Content-Disposition'))
            downlink = (downinfo.split("\""))
            filename = downlink[1]
            f = open(path + '\\' + filename, 'wb')
            f.write(r.read())
            print('下载完成' + filename)
            f.close()
            return 1

    #创建文件夹
    def newDir(self,name):
        if os.path.exists(name):
            print('准备写入至',name)
        else:
            os.makedirs(name,777)
            print('创建'+ name + '成功')

    def contentDir(self,name,title):
        path = name + '/' + title
        if os.path.exists(path):
            print('已下载过忽略下载')
            return 0
        else:
            os.makedirs(path,777)
            print('创建'+ path + '成功')
            return 1




#过滤不正常文本
    def takeTitle(self,title):
        title = title
        title = title.replace(' ','')
        title = title.replace('-','')
        title = title.replace('xp1024.com', '')
        title = title.replace('1024核工厂', '')
        title = title.replace('|', '')
        title = title.replace('！', '')
        title = title.replace('/', '')
        title = title.replace('?', '')
        return title
