#!/usr/bin/python
__author__ = 'wenwen'
###~coding: utf-8~###

import urllib2
import urllib
import re
import sys
import os

url = "http://sc.chinaz.com/ppt/"
reload(sys)
sys.setdefaultencoding('utf-8')
file_path="/data/ppt/"

def analysis_html(index_html):
    ppt_pages=re.findall('<a.*href="/ppt/.*\.htm".*">',index_html)
    ppt_links=[]
    for ppt_page in ppt_pages:
        ppt_link=re.findall('ppt/.*\.htm',ppt_page)[0].split('/')[1]
        ppt_links.append(ppt_link)
    # print ppt_pages
    analysis_pptlink(ppt_links)
def analysis_pptlink(the_pptlinks):
    for ppt_link in the_pptlinks:
        init_ppt_link=url+ppt_link
        pptlink_html=""
        try:
            pptlink_rep = urllib2.urlopen(init_ppt_link)
            pptlink_html=pptlink_rep.read()
        except:
            print "error"
        downppt_url_init=re.findall('http://wt.*/Files/DownLoad/moban.*/ppt[0-9]+\.rar',pptlink_html)
        if len(downppt_url_init) == 0:
            continue
        else:
            downppt_url=downppt_url_init[0]
        downppt_a=str(re.findall('<a href="/ppt/[0-9]+\.htm">.*</a>',pptlink_html)[0])
        downppt_name=re.findall('>.*<',downppt_a)[0].replace(">","").replace("<","")
        if os.path.exists(file_path+downppt_name+".rar"):
            continue
        else:
            fs=open(file_path+downppt_name+".rar","w")
            ppt_response=urllib2.urlopen(downppt_url)
            pptlink_html=ppt_response.read()
            fs.write(pptlink_html)
            fs.close()




first_html=""
try:
    rep = urllib2.urlopen(url)
    first_html = rep.read()
except:
    print "error"
analysis_html(first_html)
index_all = re.findall("index_[0-9]+",first_html)
pre_index = index_all[-2].split('_')[0]+"_"
max_index = int(index_all[-2].split('_')[1])
for i in range(2,max_index+1):
    init_url=url+pre_index+str(i)+".html"
    print init_url
    other_rep=urllib2.urlopen(init_url)
    other_html=other_rep.read()
    analysis_html(other_html)
