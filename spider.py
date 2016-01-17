# This Python files uses the following encoding: utf-8
import sys
import urllib
import urllib2
import re
import os
import tool
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
class Spider:
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
        self.tool=tool.Tool()
 
    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')
 
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        content=[]
        items = re.findall(pattern,page)

        for item in items:
            personsite='http:'+item[0]
            content.append([personsite,item[1],item[2],item[3],item[4]])
        return content


    def getDetailPage(self,infoUrl):
        response=urllib2.urlopen(infoUrl)
        return response.read().decode('gbk')
 
    def getBrief(self,page):
      # pattern=re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
      # result=re.search(pattern,page)
        soup=BeautifulSoup(page)
        return soup.get_text()
      # return self.tool.replace(result.group(1))


    def saveImg(self,imgUrl,filename):
          u=urllib.urlopen(imgUrl)
          data=u.read()
          f=open(filename,'wb')
          f.write(data)
          print u"正在悄悄保存她的第一张图片为",filename
          f.close()

    def saveBrief(self,content,name):
          filename=name+'/'+name+".txt"
          f=open(filename,"w+")
          print u"正在悄悄保存她的个人信息为",filename
          f.write(content.encode('utf-8'))

    def mkdir(self,path):
       path=path.strip()
       isExists=os.path.exists(path)
       if not isExists:
          print u"偷偷新建了名字叫做",path,u'的文件夹'
          os.makedirs(path)
          return True
       else:
          print u'名为',path,u'的文件夹已经创建成功'
          return False


    def savePageInfo(self,pageIndex):
       contents=self.getContents(pageIndex)
       for item in contents:
           print u'发现一位模特，名字叫',item[2],u'年龄为',item[3],u'她在',item[4]
           print u'正在偷偷的保存',item[2],u'的信息'
           print u'又意外的发现她的个人地址为',item[0]
           
           detailUrl=item[0]
           detailPage=self.getDetailPage(detailUrl)
           brief=self.getBrief(detailUrl)
          # images=self.getAllimage(detailUrl)
           self.mkdir(item[2])
           self.saveBrief(brief,item[2])
    def savePagesInfo(self,start,end):
       for i in range(start,end):
           print u'正在偷偷的寻找第',i,u'个地方，看看美眉们在不在'
           self.savePageInfo(i)
spider = Spider()
spider.savePagesInfo(2,3)
