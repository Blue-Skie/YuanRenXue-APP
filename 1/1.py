# -*- coding: utf-8 -*-
# @Time: 2022/5/21
# Author: Blue
import time

import jpype
import requests


def run():
    jvm_path = jpype.getDefaultJVMPath()
    jpype.startJVM(jvm_path, "-ea", f"-Djava.class.path=./YRX.jar", "-Dfile.encoding=utf-8",
                   convertStrings=True)
    instance = jpype.JClass('YRX.Sign')()
    s = requests.session()
    s.headers = {
        'Host': 'appmatch.yuanrenxue.com',
        'accept-language': 'zh-CN,zh;q=0.8',
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 10; zh-cn; MI 8 SE Build/QQ3A.200805.001) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1',
        'content-type': 'application/x-www-form-urlencoded',
        'cache-control': 'no-cache',
    }
    num = 0
    for page in range(1, 101):
        t = int(time.time())
        sign = instance.sign(f"page={page}{t}".encode())
        data = {
            'page': page,
            't': t,
            'sign': sign
        }
        response = s.post('https://appmatch.yuanrenxue.com/app1', data=data)
        result = response.json()
        for item in result['data']:
            num += int(item['value'].strip())
        print(page,num)
    print(num)
if __name__ == '__main__':
    run()
