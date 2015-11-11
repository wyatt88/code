__author__ = 'wyatt'
###~coding: utf-8###

import urllib
import urllib2
import re
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
url = "http://www.douban.com/group/haixiuzu/discussion?start="

def get_pic(sublink,filename):
    fn=filename
    sl=sublink
    print "sl= "+sl
    try:
        subresponse= urllib2.urlopen(sl)
    except:
        print "error"
    subhtml=subresponse.read()
#    print subhtml
    pic_links=re.findall("http://img[0-9].douban.com/view/group_topic/large/public/.*\.jpg",subhtml)
    count_pics=len(pic_links)
    if count_pics > 0:
        file_path="/root/pics/"+str(fn)
        if not os.path.isdir(file_path):
            os.mkdir(file_path)


        for i in range(0,count_pics):
             fs=open(file_path+"/"+str(i)+".jpg",'w')
             pic=urllib2.urlopen(pic_links[i])
             pichtml=pic.read()
             fs.write(pichtml)
             fs.close()

for count in range(0,100):
    html = ""
    try:
        c = count*25
        response = urllib2.urlopen(url+str(c))

        html = response.read()
    except:
        print "error"
	break

    # links = re.findall(ur'<a href="http://www.douban.com/group/topic/[\d]*/" title=".*" .*</a>',html)
    links = re.findall(ur'<a.* href="http://www.douban.com/group/topic/[\d]*/".*</a>',html)
    print links
    for link in links:
        chineselink = str(link)
        sublink = re.findall(ur'http://www.douban.com/group/topic/\d+/',chineselink)
        topicurl = sublink[0]
        filename = re.findall(ur'title=".*" ',str(chineselink))
        get_pic(sublink[0],str(filename[0]).split()[0].split('=')[1].replace('"',""))


