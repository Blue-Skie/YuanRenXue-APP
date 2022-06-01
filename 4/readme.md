## 第四题
***
题解：
1. 用黄鸟 抓包找到服务器地址和端口
2. 开始hook
   1. 注入进程  
   `objection -g com.yuanrenxue.match2022  explore`
   2. 发送请求 hook protobuf  
   `android hooking search classes protobuf`
   3. 将打印出的类前面加上android hooking watch class 存入pb.txt
   4. 批量hook 发送请求 从hook结果中找到相关方法  
   `objection -g com.xuexiang.protobufdemo explore -c`
   5. `android hooking watch class_method com.google.protobuf.Utf8.encode --dump-args --dump-backtrace --dump-return`
   6. 查看到oOO00O.OooO0O0.writeTo
   7. 添加插件查看类和对象属性  
   `objection -g com.yuanrenxue.match2022  explore -P ~/.objection/plugins`
   8. `plugin wallbreaker objectsearch o OO00O.OooO0O0`
   9. 查看内存漫游中的源码  
   `plugin wallbreaker objectdump --f ullname 0x2ec6`
   10. 根据源码写出proto文件
   11. 使用grpc_tools将proto文件转成python代码  
   `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./data.proto`
***
