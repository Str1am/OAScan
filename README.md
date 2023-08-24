# OAScan

一款用来扫描oa的漏洞的工具

## 23-8-24
根据hw添加了部分poc
目前支持的poc

### 0x01：致远
1. 致远A6用户信息泄露<br>
2. ajax.do文件上传<br>
3. createMysql.jsp 数据库敏感信息泄露<br>
4. initDataAssess.jsp 用户敏感信息泄露<br>
5. 致远登录绕过<br>
6. m1 server命令执行<br>
7. A8 状态监控页面信息泄露<br>
8. /seeyon/htmlofficeservlet文件上传<br>
9. getSessionList.jsp Session泄漏漏洞<br>
10. A6 test.jsp SQL注入漏洞<br>
11. /seeyon/wpsAssistServlet文件上传<br>
12. webmail.do任意文件下载<br>


### 0x02：泛微
1. 泛微云桥 e-Bridge 任意文件读取<br>
2. BshServlet命令执行漏洞<br>
3. 数据库配置信息泄漏漏洞<br>
4. getSqlData注入<br>
5. uploadOperation.jsp文件上传<br>
6. ln.FileDownload任意文件下载<br>
7. getdata.jsp注入<br>
8. LoginSSO.jsp注入<br>
9. /OfficeServer上传<br>
10. WorkflowServiceXml注入<br>
 
### 0x03：通达
1. ispirit/login_code.php存在通达任意用户登录<br>
2. logincheck_code.php存在通达任意用户登录<br>
3. im/upload.php任意文件上传<br>

### 0x04：用友
1. bsh.servlet.BshServlet 远程命令执行
2. 数据库读取
3. ELTextFile.load.d文件读取
4. NCFindWeb目录遍历
5. soapFormat.ajax xxe
6. com.ufida.web.action.ActionServlet未授权
7. jsinvoke文件上传（状态码判断，未直接上传文件）

## 使用介绍

mac用户可以添加命令到zshrc中

<img width="700" alt="image" src="https://github.com/Str1am/OAScan/assets/48739932/d5702204-0e72-4633-9034-921aeb63f699">

方便快速扫描

<img width="1067" alt="image" src="https://github.com/Str1am/OAScan/assets/48739932/69caf8d6-8f1a-4a9b-a5b8-1daad25391ea">


目前支持-u -m -f三种参数

-u用于指定url进行测试

<img width="1023" alt="image" src="https://user-images.githubusercontent.com/48739932/166615230-cf05ddfa-4922-4532-9952-18666da604b0.png">

-m参数用于指定oa系统进行扫描

<img width="955" alt="image" src="https://user-images.githubusercontent.com/48739932/166615278-22accb23-33ad-4b4e-9b7d-7e56d729736b.png">


指定单个poc进行扫描

<img width="948" alt="image" src="https://user-images.githubusercontent.com/48739932/166615366-6b172b90-b572-4778-a31c-22541caaf705.png">

在目录新建一个txt文件，传入url

-f指定即可

<img width="958" alt="image" src="https://user-images.githubusercontent.com/48739932/166616133-7752cf57-3402-408a-a59f-71f1e8665458.png">



由于代码设计原因，-m参数为poc中第一个_前的字符，指定单个poc即输入poc名称即可


由于本人代码水平有限，且为了防止恶意扫描以及环境有限，部分poc只是做提示和验证，并未进行攻击操作。当然在新的漏洞出来后会保持更新状态，欢迎在使用过程中提出意见。

如果对您有用，欢迎star。

## Refererce

PeiQi_Wiki

https://github.com/saucer-man/saucerframe

## 免责声明
此处提供的所有工具仅供授权状态下使用，且poc仅以检测作用为主，如发生违法犯罪行为,非授权攻击行为于本人无关
