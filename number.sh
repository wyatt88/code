#!/bin/bash

startdate=2013001
enddate=2015021
now=`date +%Y%m%d`
staticfile=/root/$now
dir1=$startdate$enddate

if [ ! -d $dir1 ]
then
   mkdir $dir1
fi
wget "http://zx.caipiao.163.com/trend/ssq_historyPeriod.html?beginPeriod=$startdate&endPeriod=$enddate&historyPeriodSelect=2015021&historyPeriod=2015022&year="
result=`ls | grep ssq | grep $startdate | grep $enddate`
echo $result
mv $result $dir1/1.tmp

cd $dir1
lines=`cat 1.tmp | grep 开奖日期 | wc -l`
echo "共$lines期" >> $staticfile

cat 1.tmp | grep 开奖日期 -A 8 > 2.tmp
sed -i '/^.*br01.*$/'d 2.tmp

