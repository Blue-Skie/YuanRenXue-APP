## 第五题
***
题解：
1. 直接使用r0capture将证书hook出来  证书路径在/sdcard/Download/下 密码为: r0ysue
`python ./r0capture/r0capture.py -U -f com.yuanrenxue.match2022`
***
2. 抓包
    1. 可以查看r0capture的日志 请求流程自吐
    2. 可以将证书导入到charles 之后运行  
   `frida -UF -l DroidSSLUnpinning.js`  
    便可以开始进行抓包了

***