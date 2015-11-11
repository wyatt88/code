#!/usr/bin/python
#coding: utf-8
__author__ = 'wyatt'

import os,sys,time
import urllib2
import urllib
from multiprocessing.dummy import Pool as ThreadPools

class downloader():
    def __init__(self,qqUrl,splitnum):
        self.url = qqUrl
        self.blocks = splitnum
        self.filename = self.url.split('/')[-1]
        req = urllib2.Request(self.url)
        req.get_method = lambda : "HEAD"
        resp = urllib2.urlopen(req).headers
        self.total = int(resp['Content-Length'])

    def cal_range(self):
        initbyte = 0
        initoffset = self.offset
        endbyte = initoffset
        rangeLists = []
        for i in range(0,self.blocks):

            if i == self.blocks-1:
                rangeLists.append([initbyte,self.total])
            else:
                rangeLists.append([initbyte,endbyte])
            initbyte = endbyte+1
            endbyte = initbyte + initoffset
        print rangeLists
        return rangeLists

    def getRanges(self,rangeList):
	firstTime = time.time()
        startRange = int(rangeList[0])
        endRange = int(rangeList[1])
        print "start: %d end: %d is start" % (startRange,endRange)
        req = urllib2.Request(self.url)
        req.add_header('Range', 'Bytes=' + str(startRange) + '-' + str(endRange) )
        try:
            resp = urllib2.urlopen(req)
        except:
            print("error when open url: %s", self.url)
            sys.exit(2)
        if self.writeFile(resp.read(),startRange):
            secondTime = time.time()
            seconds = secondTime - firstTime
            print "start_pos: %d to end_pos: %d is done in %ss speed is %s Kb/s" %\
                  (startRange,endRange,str(seconds),str((self.offset/int(seconds))/1024))

    def writeFile(self,html,f_start):
        try:
            fd = os.dup(self.fd.fileno())
            fw = os.fdopen(fd,'w')
            fw.seek(f_start)
            fw.write(html)
        except Exception as e:
            print e.message
        finally:
            fw.close()
	    return 1


    def run(self):
        self.offset = self.total/int(self.blocks)
        self.fd = open(self.filename,'w')
        offsetList=self.cal_range()
        pool = ThreadPools(self.blocks)
        pool.map(self.getRanges,offsetList)
        pool.close()
        pool.join()

if __name__ == '__main__':
    down = downloader('http://archive.kernel.org/centos-vault/5.9/isos/x86_64/CentOS-5.9-x86_64-bin-DVD-1of2.iso',4)
    down.run()
