import httpx
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url = target + '/OfficeServer'
        req = httpx.get(url,headers=headers)
        if "WVS" in req.headers.get("server") and "ecology_JSessionId" in req.headers.get("set-cookie") and req.status_code == 200:
            print("\033[0;31m 泛微OfficeServer可访问，尝试是否存在文件上传漏洞："+ url )
    except:
        pass


