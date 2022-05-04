# OAScan

一款用来扫描oa的漏洞的工具

#### 使用介绍

目前支持-u -m -f三种参数

-u用于指定url进行测试

<img width="1023" alt="image" src="https://user-images.githubusercontent.com/48739932/166615230-cf05ddfa-4922-4532-9952-18666da604b0.png">

为了方便测试，加入了-m参数用于指定oa系统进行扫描

<img width="955" alt="image" src="https://user-images.githubusercontent.com/48739932/166615278-22accb23-33ad-4b4e-9b7d-7e56d729736b.png">


当然也能指定单个poc进行扫描

<img width="948" alt="image" src="https://user-images.githubusercontent.com/48739932/166615366-6b172b90-b572-4778-a31c-22541caaf705.png">

在目录新建一个txt文件，传入url

-f指定即可

<img width="958" alt="image" src="https://user-images.githubusercontent.com/48739932/166616133-7752cf57-3402-408a-a59f-71f1e8665458.png">



由于代码设计原因，-m参数为poc中第一个_前的字符，指定单个poc即输入poc名称即可


由于本人代码水平有限，且为了防止恶意扫描以及环境有限，部分poc只是做提示和验证，并未进行攻击操作。当然在新的漏洞出来后会保持更新状态，欢迎在使用过程中提出意见。

如果对您有用，欢迎star。

#### 免责声明
此处提供的所有工具仅供授权状态下使用，且poc仅以检测作用为主，如发生违法犯罪行为,非授权攻击行为于本人无关
