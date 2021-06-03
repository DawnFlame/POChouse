## 应用简介

Apache Struts2 是一个基于MVC设计模式的Web应用框架，会对某些标签属性（比如 id）的属性值进行二次表达式解析，因此在某些场景下将可能导致远程代码执行。

## 相关资产

FOFA

```http
app="Struts2"
```

## 环境搭建

Docker一键搭建Vulhub

## 重要漏洞

**S2-016**:影响版本Struts 2.0.0-2.3.15; GET请求发送数据; 支持获取WEB路径,任意命令执行,反弹shell和文件上传

**S2-037**:影响版本Struts 2.3.20-2.3.28.1; GET请求发送数据; 支持获取WEB路径,任意命令执行和反弹shell
**S2-046**:影响版本Struts 2.3.5-2.3.31,2.5-2.5.10; POST请求发送数据,不需要参数; 支持获取WEB路径,任意命令执行,反弹shell和文件上传

**S2-048**:影响版本Struts 2.3.x with Struts 1 plugin and Struts 1 action; POST请求发送数据; 默认参数为:username,password; 支持任意命令执行和反弹shell

**S2-053**:影响版本Struts 2.0.1-2.3.33,2.5-2.5.10; POST请求发送数据; 默认参数为:username,password; 支持任意命令执行和反弹shell

**S2-devMode**:影响版本Struts 2.1.0-2.3.1; GET请求发送数据; 支持获取WEB路径,任意命令执行和反弹shell

## 漏洞利用

1、某Struts全版本检测工具

2、[Railgun](https://github.com/lz520520/railgun)

3、Goby

以上工具皆可扫描利用

