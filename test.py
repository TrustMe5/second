import re
import urllib
import urllib2

class Spider:
      def __init__(self):
          self.site="http://mm.taobao.com/json/request_top_list.htm"

      def getPage(self,pageIndex):
          url=self.site+'?page='+str(pageIndex)
          print url
          request=urllib2.Request(url)
          response=urllib2.urlopen(request)
          return response.read().decode('gbk')

      def getContent(self,pageIndex):
          page=self.getPage(pageIndex)
          pattern=re.compile('<div class="list-item.*?<a.*?href="(.*?)".*?<img.*?src="(.*?)".*?<a class="lady-name".*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
          itemlist=re.findall(pattern,page)
          for item in itemlist:
              personsite='http:'+item[0]
              print personsite,item[1],item[2],item[3],item[4]



spider=Spider()

spider.getContent(1)
