#!/usr/bin/python
import sys
import re
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  
from lxml import html
from bs4 import BeautifulSoup

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

url = 'http://zq.win007.com/cn/TeamHeadPage/2016-2017/36.html'  
r = Render(url)  
result = r.frame.toHtml()
#This step is important.Converting QString to Ascii for lxml to process
#htlmlResult = html.fromstring(str(result.toAscii()))
bs4Obj = BeautifulSoup(str(result.toUtf8()), 'html.parser')
#archive_links = htlmlResult.xpath('//head/title')
teamUrlLinks = bs4Obj.find_all(href=re.compile("/cn/team/Summary/"))
teamUrls = set()
for teamUrl in teamUrlLinks:
	teamUrls.add(teamUrl['href'])

for url in teamUrls:
	print url