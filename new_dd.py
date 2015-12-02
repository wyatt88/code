#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'wenwen'

import urllib2
import sys
from multiprocessing.dummy import Pool as ThreadPools
import re
from pyquery import PyQuery
from time import sleep

reload(sys)
sys.setdefaultencoding("utf-8")

class collectData():
    def __init__(self,keywords):
        self.initUrl1 = "http://www.zufangzi.com/house/houseControllor/conditionSearchKeyword.do?parameter1=0&parameter2=22200&pageNum="
        self.initUrl2 = "&keyword="
        self.kwdList = keywords

    def getMax(self,html):
        firsthtml = html
        # print firsthtml
        resultstr = re.findall('<div class="listPR">.*<input',firsthtml)[0]
        number = int(re.findall('\d+',resultstr)[0])
        return number

    def accessEveryPage(self,keyword,mpn):
        allhtml = ""
        for i in range(1,mpn+1):
            everypageurl = self.initUrl1+str(i)+self.initUrl2+keyword
            EPreps = urllib2.urlopen(everypageurl)
            try:
                EPhtml = EPreps.read()
            except:
                print "EP Error"
            else:
                allhtml += EPhtml
        everyhouseurl = list(set(re.findall('http://.*/detail/.*\.html',allhtml)))
        houselist = self.accessEveryHouse(everyhouseurl)
        totalDataDict[str(keyword)] = houselist

    def accessEveryHouse(self,EHU):
        houselist=[]
        for houseurl in EHU:
            # housereps = urllib2.urlopen(houseurl)

            try:
                housedoc = PyQuery(url=houseurl)

                # househtml = housereps.read()
            except:
                print "EH Error"
            else:
                EHprice = str(housedoc('div').filter('.xqyC1R_1').find('i')).split(';')[1].replace('</i>','')
                EHdetails = housedoc('div').filter('.xqyC1R_3').find('p')
                EHarea = EHdetails.find('em').text()
                EHcommunite = EHdetails.eq(7).text().split()[1]
                housedict={houseurl:[str(EHcommunite).encode('utf-8'),EHprice,str(EHarea).encode('utf-8')]}
                houselist.append(housedict)
        return houselist


        # print EHcommunite

    def getPageList(self,keyword):
        firsturl = self.initUrl1+"1"+self.initUrl2+keyword
        try:
            reps = urllib2.urlopen(firsturl)
            html = reps.read()
        except urllib2.HTTPError as e:
            if e.code == 404:
                sleep(5)
        else:
            maxpagenum = self.getMax(html)
            self.accessEveryPage(keyword,maxpagenum)

    def run(self):
        pool = ThreadPools(2)
        pool.map(self.getPageList,self.kwdList)
        pool.close()
        pool.join()

keywordList = [
    u'中关村',
    u'世纪城',
    u'西单',
    u'洋桥',
    u'西苑',
    u'小西天'

]
if __name__ == "__main__":
    totalDataDict = {}
    dingdingCollect = collectData(keywordList)
    dingdingCollect.run()
    unicode2chinese = str(totalDataDict).decode('string_escape')
    datafile = open('dingdingDATA.txt','w')
    try:
        datafile.write(unicode2chinese.encode('utf-8'))
    except:
        print "Write file Error"
    finally:
        datafile.close()
        print unicode2chinese
        for kw in keywordList:
            print str(len(totalDataDict[kw]))+' '+kw
