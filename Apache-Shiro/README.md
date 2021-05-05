## 应用简介

Shiro 是 Apache 旗下的一个用于权限管理的开源框架，提供开箱即用的身份验证、授权、密码套件和会话管理等功能

## [CVE-2016-4437]-Shiro 550反序列化

**漏洞概述**

```http
#影响版本
Shiro <= 1.2.4
```

在 Shiro 1.2.4 及之前的版本，Shiro 秘钥是硬编码的一个值 `kPH+bIxk5D2deZiIxcaaaA==`，这便是 Shiro-550 的漏洞成因。但这个漏洞不只存在于 1.2.4 版本，后续版本的读取流程没有什么改动，这就意味着只要秘钥泄露，依然存在高危风险。

Shiro Top 100 Key 是基于一些 Github 示例代码收集的

**漏洞利用**

```bash
use multi/http/shiro_rememberme_v124_deserialize
```

## Shiro 721 Padding Oracle漏洞

```http
#影响版本
Shiro < 1.4.2
```

Shrio所使用的cookie里的rememberMe字段采用了AES-128-CBC的加密模式，这使得该字段可以被padding oracle 攻击利用。

攻击者可以使用一个合法有效的rememberMe 的cookie作为前缀来实施POA，然后制造一个特制的rememberMe来执行Java反序列化攻击，比如Shrio 550那样的

**实施步骤：**

1. 登录网站，任意用户，来获取一个合法的remmemberMe cookie。
2. 使用rememberMe cookie作为前缀来实施POA。
3. 加密Java反序列化的payload来制作特制的rememberMe
4. 带着新的rememberMe向网站发起请求

这个漏洞相较于550而言，它不需要知道key的值，但是它需要一个合法用户的rememberMe cookie，这大概是它比较鸡肋的地方了

**对于550和721飞鸿大佬写了一键化利用工具**

https://github.com/feihong-cs/ShiroExploit-Deprecated

## Shiro-682 权限绕过漏洞

```http
#影响版本
Shiro	1.3.2
Shiro < 1.5.0
```

**利用**

```bash
use "uri = uri + '/' " to bypassed shiro protect
即URL结尾添加反斜杠绕过权限验证
```

## [CVE-2020-13933]-Shiro 权限绕过漏洞

**Shiro < 1.6.0**

POC

```http
xxx.com/res/;name

当请求的资源存在时即可绕过权限验证查看资源
```

## Shiro漏洞分析

**Shiro RememberMe 漏洞检测的探索之路**

https://paper.seebug.org/1285/