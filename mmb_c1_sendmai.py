#!/usr/bin/python 
#coding:utf-8 
#author:wenwen 
 
import smtplib 
import email.MIMEMultipart  
import email.MIMEText  
import email.MIMEBase  
import os.path   
import sys
import urllib2
 
mail_host = 'smtp.126.com' 
mail_user = 'mmb_zabbix' 
mail_pass = '' 
mail_postfix = '126.com'
file_name = '/home/zabbix/test.html'

def get_file():
    try:
        reps = urllib2.urlopen('http://xxx:8080/mmmb/status/all?XML=true')
        html = reps.read()
        f = open(file_name,'w')
        f.write(html)
    except:
        f.close()
        return 0
    else:
        f.close()
        return 1
 
def send_mail(to_list,subject): 
    me = mail_user+"<"+mail_user+"@"+mail_postfix+">" 
    main_msg = email.MIMEMultipart.MIMEMultipart()  
  
# 构造MIMEText对象做为邮件显示内容并附加到根容器  
    text_msg = email.MIMEText.MIMEText("this is from 1.37's java manager page")  
    main_msg.attach(text_msg)  
  
# 构造MIMEBase对象做为文件附件内容并附加到根容器  
    contype = 'application/octet-stream'  
    maintype, subtype = contype.split('/', 1)  
  
## 读入文件内容并格式化  
    data = open(file_name, 'rb')  
    file_msg = email.MIMEBase.MIMEBase(maintype, subtype)  
    file_msg.set_payload(data.read( ))  
    data.close( )  
    email.Encoders.encode_base64(file_msg)  
  
## 设置附件头  
    basename = os.path.basename(file_name)  
    file_msg.add_header('Content-Disposition','attachment', filename = basename)  
    main_msg.attach(file_msg)  
  
# 设置根容器属性  
    main_msg['From'] = me  
    main_msg['To'] = to_list   
    main_msg['Subject'] = subject  
    main_msg['Date'] = email.Utils.formatdate( )  
  
# 得到格式化后的完整文本  
    fullText = main_msg.as_string( )  
       
    try: 
        s = smtplib.SMTP() 
        s.connect(mail_host) 
        s.login(mail_user,mail_pass) 
        s.sendmail(me,to_list,fullText) 
        s.close() 
        return True 
    except Exception,e: 
        print str(e) 
        return False 
     
if __name__ == "__main__":
    
    if get_file() > 0:
        to_list = 'wenwen@ebinf.com'
        subject = "MyTest"
        send_mail(to_list,subject) 




