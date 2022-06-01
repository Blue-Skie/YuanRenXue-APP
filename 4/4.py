# -*- coding: utf-8 -*-
# @Time: 2022/5/15
# Author: Blue
import time

import grpc
import jpype

import data_pb2_grpc
import data_pb2

_HOST = '180.76.60.244'
_PORT = '9901'


# python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./data.proto
def run():
    jvm_path = jpype.getDefaultJVMPath()
    jpype.startJVM(jvm_path, "-ea", f"-Djava.class.path=./unidbg_4/unidbg.jar", "-Dfile.encoding=utf-8",
                   convertStrings=True)
    instance = jpype.JClass('com.yrx4.MainActivity')()

    num = 0
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 监听频道

    client = data_pb2_grpc.ChallengeStub(channel=conn)  # 客户端使用Stub类发送请求,参数为频道,为了绑定链接
    for page in range(1, 101):
        t = int(time.time()) * 1000
        sign = instance.GetSign(f"{page}:{t}", t)

        response = client.SayHello(data_pb2.HelloRequest(page=page, time=t, sign=sign))  # 返回的结果就是proto中定义的类
        for item in response.resp:
            num += int(item.message)

        print(page, num)

    print(num)


if __name__ == '__main__':
    run()
