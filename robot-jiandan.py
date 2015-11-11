#!/usr/bin/python
__author__='wenwen'
###~coding: utf-8###

import urllib
import urllib2
import re
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
url = ("http://jandan.net/pic/page-","#comments")
user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'

def get_pic(init_html,path_name):
    pic_html=init_html
    # print pic_html
    path=str(path_name)
    jpg_pic_links=re.findall(ur'http://ww[0-9].sinaimg.cn/.*\.jpg',str(pic_html))
    #print pic_links

    count_pics=len(jpg_pic_links)
    if count_pics > 0:
        # print count_pics
        file_path="/root/"+path
        if not os.path.isdir(file_path):
            os.mkdir(file_path)


        for i in range(0,count_pics):
             fs=open(file_path+"/"+str(i)+".jpg",'w')

             pic_res=urllib2.Request(jpg_pic_links[i])
             pic_res.add_header('User-Agent',user_agent)
             pic=urllib2.urlopen(pic_res)
             pichtml=pic.read()
             fs.write(pichtml)
             fs.close()


req = urllib2.Request('http://jandan.net/pic')
req.add_header('User-Agent',user_agent)
res = urllib2.urlopen(req)
html=res.read()
max_span=re.findall('<span class="current-comment-page">.*</span>',html)[0]
max_page=int(re.findall('[0-9]+',max_span)[0])
for count in range(max_page,1,-1):
    pichtml = ""
    try:

        request = urllib2.Request(url[0]+str(count)+url[1])
        request.add_header('User-Agent',user_agent)
        response = urllib2.urlopen(request)
        pichtml = response.read()

    except:
        print "error"

    get_pic(pichtml,count)

