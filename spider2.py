# 爬取知乎网站的美女图片链接，并保存到本地


from urllib import request  
from  bs4 import BeautifulSoup  
import re  
import time
import urllib
import http  
  
url = "https://www.pexels.com/popular-photos"

user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.44 Safari/537.36 OPR/24.0.1558.25 (Edition Next)'
myheader={'User-Agent':user_agent,
          'Host':'www.pexels.com',
          'GET':url}


req = urllib.request.Request(url, headers=myheader)
html = urllib.request.urlopen(req).read().decode('utf-8')  
soup = BeautifulSoup(html,'html.parser')  
# print(soup.prettify())
      
#用Beautiful Soup结合正则表达式来提取包含所有图片链接（img标签中，class=**，以.jpg结尾的链接）的语句  
links = soup.find_all('img', attrs={'class':'photo-item__img'})  
# print(links)  
#设置保存图片的路径，否则会保存到程序当前路径  
#路径前的r是保持字符串原始值的意思，就是说不对其中的符号进行转义  
path = r'./images/'
for link in links:  
    print(link.attrs['src'])  
    #保存链接并命名，time.time()返回当前时间戳防止命名冲突  
    #使用request.urlretrieve直接将所有远程链接数据下载到本地  
    request.urlretrieve(link.attrs['src'],path+'%s.jpg' % time.time())  
