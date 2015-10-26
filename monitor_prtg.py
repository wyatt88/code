__author__ = 'wyatt'
#coding: utf-8


import urllib2
import telnetlib
import os,sys
import re
from pyquery import PyQuery
import logging

init_list=[]
host_user="xxx"
host_pwd="xxxxxx"
baseurl="http://192.168.0.13/sensorlist.htm?listid="
host_dict={"192.168.3.12":[host_user,host_pwd,1400],
           "192.168.3.14":[host_user,host_pwd,1606],
           "192.168.13.1":[host_user,host_pwd,1556],
           "192.168.15.1":[host_user,host_pwd,1743],
           "192.168.3.10":[host_user,host_pwd,1244],
           "192.168.3.13":[host_user,host_pwd,1476]
           }

reload(sys)
sys.setdefaultencoding('utf-8')
logging.basicConfig(filename="logs/app.log",level=logging.INFO)

def run_telnet_session(host,interface):
    telnet_host=host
    telnet_port=23
    usr=host_dict[host][0]
    pwd=host_dict[host][1]
    session=telnetlib.Telnet()
    session.set_debuglevel(0)
    session.open(telnet_host,telnet_port)
    #print session.read_until("Username:")
    session.write(usr+"\n\r")
    #print session.read_until("Password:")
    session.write(pwd+"\n\r")
    session.write("sys"+"\n\r")
    session.write("interface Ethernet "+interface + "\n\r")
    session.write("line-rate inbound 2048"+"\n\r")
    session.write("line-rate outbound 2048"+"\n\r")
    session.write('quit'+"\n\r")
    session.write('quit'+"\n\r")
    session.write('quit'+"\n\r")
    session.read_all()
    # session.interact()
    session.close()
    return True

def get_devtrs(listid):
    av_url=baseurl+str(listid)
    print av_url
    doc = PyQuery(url=av_url)
    tr_list=doc('tr').filter('.onesensor')
    return tr_list
    # reg=ur'<table class="sensortable">[\s\n\r].*</table>'
    # objgrep=re.compile(reg)
    # objlist=re.findall(objgrep,html)
    # return objlist

# doc = pq(url="http://192.168.0.13")
#html = urllib2.urlopen('http://192.168.0.13').read()
#doc = unicode(html.read(),"utf-8")
#fs=file("test.html","w")
#print html.read()
#fs.write(html.decode('gb2312','ignore').encode('utf-8'))
#fs.close()
#doc = pq(filename='test.html')

for host_ip in host_dict.keys():
    tmp_dict={}
    tmp_dict={host_ip:[]}
    listid = host_dict[host_ip][2]
    trs_list = get_devtrs(listid)
    print host_ip
    # print trs_list
    for tr in trs_list:
        try:
            interface = tr.getchildren()[1].getchildren()[1].text.decode('gb2312','ignore').split()[2]
            speed_tu=tr.getchildren()[2].text.split(',')
            if len(speed_tu) > 1:
                speed = int(speed_tu[0]+speed_tu[1])
                if interface.find("Gig")==-1:
                    if speed > 5000:
                        tmp_dict[host_ip].append(interface)
        except:
            continue
    logging.info(tmp_dict)
    if len(tmp_dict[host_ip])>0:

        interface_list=tmp_dict[host_ip]
        for inf in interface_list:
            if inf != "":
                inf_num=inf.split('net')[1].replace(')','')
                if run_telnet_session(host_ip,str(inf_num)):
                    logging.info("interface "+inf_num+" on "+host_ip+" rate is 2048")








# response=urllib2.urlopen('http://192.168.0.13')
# html=response.read()
# print get_tbody(html)




