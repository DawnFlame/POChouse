## [CVE-2020-2551]-IIOP反序列化

**漏洞概述**

攻击者通过IIOP协议远程访问WebLogic Server服务器上的远程接口；

传入恶意数据，从而获取服务器权限并在未授权情况下远程执行任意代码

```http
#影响版本
WebLogic 10.3.6.0.0
WebLogic 12.1.3.0.0
WebLogic 12.2.1.3.0
WebLogic 12.2.1.4.0
```

**漏洞验证**

网上暂无可稳定利用的EXP（部分无法利用），可尝试

https://github.com/Y4er/CVE-2020-2551

**漏洞分析**

https://www.anquanke.com/post/id/197605

https://www.anquanke.com/post/id/206494

**修复建议**

1、补丁升级：登陆https://support.oracle.com后，下载最新补丁
2、临时规避措施：通过禁用IIOP协议对漏洞进行缓解

## [CVE-2020-2883]-T3反序列化

**漏洞概述**

该漏洞是2555补丁的绕过

```http
#影响版本
WebLogic 10.3.6.0.0
WebLogic 12.1.3.0.0
WebLogic 12.2.1.3.0
WebLogic 12.2.1.4.0
```

**漏洞利用**

```bash
use multi/misc/weblogic_deserialize_badattr_extcomp
```

**修复建议**

1、升级补丁：登陆https://support.oracle.com后，下载最新补丁
2、临时规避措施：通过禁用T3协议对漏洞进行缓解

## [CVE-2020-14644]-远程命令执行

**漏洞概述**

```http
#影响版本
12.2.1.3.0
12.2.1.4.0
14.1.1.0.0
```

**漏洞利用**

下载EXP：https://github.com/potats0/cve_2020_14644/releases/tag/0.0.2

```bash
java -jar cve-2020-14644.jar 127.0.0.1 7001 whoami
```

**漏洞分析**

https://www.cnblogs.com/potatsoSec/p/13451993.html

## [CVE-2020-14882]-未授权命令执行

**漏洞概述**

```http
#影响版本 （有console控制台存在的）
10.3.6.0.0
12.1.3.0.0
12.2.1.3.0
12.2.1.4.0
14.1.1.0.0
```

未经身份验证的远程攻击者可能通过构造特殊的 HTTP GET请求，利用该漏洞在受影响的 WebLogic Server 上执行任意代码

**漏洞利用**

```bash
use exploit/multi/http/weblogic_admin_handle_rce
```

**修复建议**

配置 WebLogic 禁用 Console 控制台