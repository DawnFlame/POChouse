## 应用简介

![](logo.png)

Nexus 是一个强大的 maven 仓库管理器，它极大的简化了本地内部仓库的维护和外部仓库的访问。

提供了强大的构件搜索功能，它基于REST，占用较少的内存，基于简单文件系统而非数据库。

官方网站：https://www.sonatype.com

默认账户：`admin/admin123`

## 相关应用

FOFA

```http
app="Nexus-Repository-Manager"
```

## 环境搭建

下载 Docker 镜像：

```
docker pull sonatype/nexus3:3.21.1
```

创建 nexus 数据存储目录：

```
mkdir /your-dir/nexus-data
```

运行 Docker 镜像，并且开启调试端口，其中 8081 为 web 访问端口，5050 端口为远程调试端口：

```
docker run -d --rm -p 8081:8081 -p 5050:5050 --name nexus -v /your-dir/nexus-data:/nexus-data -e INSTALL4J_ADD_VM_PARAMS="-Xms2g -Xmx2g -XX:MaxDirectMemorySize=3g  -Djava.util.prefs.userRoot=/nexus-data -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5050" sonatype/nexus3:3.21.1
```

下载 Nexus 源码，并且切换至 `3.21.0-05` 分支：

```
git clone https://github.com/sonatype/nexus-public.git
git checkout -b release-3.21.0-05 origin/release-3.21.0-05
```

IDEA 导入项目并且配置远程调试信息