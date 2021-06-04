## 应用简介

WebLogic是美国Oracle公司出品的一个application server，确切的说是一个基于JAVAEE架构的中间件；

WebLogic是用于开发、集成、部署和管理大型分布式Web应用、网络应用和数据库应用的Java应用服务器

## 影响范围

FOFA

```http

```

## 环境搭建

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