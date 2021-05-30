## FastAdmin 用户权限RCE

影响版本：
- < V1.2.0.20210401_beta

前提：
```
1、普通用户权限
2、需要修改默认配置才能使用分片上传功能，设置application/extra/upload.php下的chunking项为true
```

exp:
```
Usage: python fastadmin.py url
默认Webshell密码为hhh
```

[@赛博回忆录](https://github.com/exp1orer/FastAdmin_Upload)
[@exp1orer](https://www.mdeditor.tw/pl/gQ9m)