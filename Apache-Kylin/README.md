## 应用简介

![](kylin_logo.png)

Apache Kylin是一个开源的分布式分析引擎，提供Hadoop之上的SQL查询接口及多维分析（OLAP）能力以支持超大规模数据，最初由eBay Inc. 开发并贡献至开源社区。它能在亚秒内查询巨大的Hive表。

官方网站：http://kylin.apache.org/cn

默认账户：admin/KYLIN

## 影响范围

FOFA

```http
app="APACHE-kylin"
body="kfkSchema"
```

## 环境搭建

[用 Docker 运行 Kylin](http://kylin.apache.org/cn/docs/install/kylin_docker.html)

## 相关漏洞

Apache Kylin的未授权配置泄露 CVE-2020-13937

```
http://xxx.xxx.xxx.xxx/kylin/api/admin/config
```