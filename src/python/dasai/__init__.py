# !/usr/bin/python
# -*- coding: UTF-8 -*-

from json import *
import httplib
import json

import urllib2


def http_get():
    url = 'http://opendata.sz.gov.cn/api/798418111/1/service.xhtml?page=1&rows=100&appKey=d287c7d3e868497a8805ff62df802214'  # 页面的地址
    response = urllib2.urlopen(url)  # 调用urllib2向服务器发送get请求
    return response.read()  # 获取服务器返回的页面信息


ret = http_get()
print ret
print type(ret)
dum = json.dumps(ret)
a = json.load(dum)
print type(a)
d=JSONDecoder().decode(ret)
print d
print type(d)
print "WFQYMC\t","CFRQ\t","ZZJGDM\t","BH\t","WFWGXW\t","GSJSRQ\t","QYDZ\t","SXBM\t","ZCH\t","XZCFZL\t","XZCFJDSWH\t","CFZXJG\t"
for i in range(0,100):
    print i,d['data'][i]["WFQYMC"],d['data'][i]["CFRQ"],d['data'][i]["ZZJGDM"],d['data'][i]["BH"],d['data'][i]["WFWGXW"]

