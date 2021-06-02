## 漏洞概述

Shrio所使用的cookie里的rememberMe字段采用了AES-128-CBC的加密模式，这使得该字段可以被padding oracle 攻击利用。

攻击者可以使用一个合法有效的rememberMe 的cookie作为前缀来实施POA，然后制造一个特制的rememberMe来执行Java反序列化攻击，比如Shrio 550那样的

## 影响范围

```http
Shiro < 1.4.2
```

## 漏洞利用

1. 登录网站，任意用户，获取一个合法的remmemberMe cookie（勾选Remember Me）。
2. 使用rememberMe cookie作为前缀来实施POA。
3. 加密Java反序列化的payload来制作特制的rememberMe
4. 带着新的rememberMe向网站发起请求

这个漏洞相较于550而言，它不需要知道key的值，但是它需要一个合法用户的rememberMe cookie；

**飞鸿大佬写了一键化利用工具**

https://github.com/feihong-cs/ShiroExploit-Deprecated

## 参考链接

[Shiro 721 Padding Oracle攻击漏洞分析](https://www.anquanke.com/post/id/193165)

[Shiro-721 RCE Via Padding Oracle Attack](https://github.com/inspiringz/Shiro-721)