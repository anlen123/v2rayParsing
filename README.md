# 使用方法

把v2ray 的订阅连接写入 ding.inf 中

```inf
xxxxx
```

```python
python(python3) main.py

    ~/v2ray    master !1 ?1  python main.py                                                               ✔  base  
1 : 发现偷奈飞的机场举报有奖
2 : 本站地址: kycc.wtf
3 : 电报群: t.me/gfwservice
4 : 使用前请更新订阅，以获取最新节点
5 : 协议更新了，请使用最新版客户端！中转正在维护，可用性较低，建议使用直连。
6 : NF|amerforever666@gmail.com|Madison0212
7 : DSY|luhh507@4kcd.live|qwe123@@|KYCC
8 : 香港|主|01|流解|HKT|东莞移动
9 : 香港|主|01|流解|HKT|广港隧道
10 : 香港|主|01|流解|HGC|汕头移动
你切换的节点: 
```
输入节点的数字, 当前目录下的config.json文件就会更新为可用的文件

# 执行v2ray 
```shell
./v2ray -c config.json
```

或者你可以使用我写的脚本
先给权限 chmod 755 run.sh
```shell
./run.sh 
```

后台就会自动执行v2ray服务端

杀死服务端命令(先给权限 chmod 755 kill.sh)
```shell
./kill.sh
```

http 端口为1081, sock端口为1089  可以在config.json 文件中修改, 当然在ws_tls.json中修改更好
# 使用单节点

把节点信息存入node中

执行命令
```python
python(python3) node.py
```
