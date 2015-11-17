#!/usr/bin/python
#coding: utf-8
__author__ = 'wenwen'

import urllib2
import urllib
import os,sys
from multiprocessing.dummy import Pool as ThreadPools
import re
from pyquery import PyQuery

reload(sys)
sys.setdefaultencoding('utf-8')
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
                housedict={houseurl:[EHcommunite,EHprice,EHarea]}
                houselist.append(housedict)
        return houselist


        # print EHcommunite

    def getPageList(self,keyword):
        firsturl = self.initUrl1+"1"+self.initUrl2+keyword
        reps = urllib2.urlopen(firsturl)
        try:
            html = reps.read()
        except:
            print "Error"
        else:
            maxpagenum = self.getMax(html)
            self.accessEveryPage(keyword,maxpagenum)

    def run(self):
        pool = ThreadPools(len(self.kwdList))
        pool.map(self.getPageList,self.kwdList)
        pool.close()
        pool.join()







keywordList = [
    u'中关村'
]
if __name__ == "__main__":
    totalDataDict = {}
    dingdingCollect = collectData(keywordList)
    dingdingCollect.run()
    datafile = open('dingdingDATA.txt','w')
    datafile.write(str(totalDataDict))
    datafile.close()
    print totalDataDict
