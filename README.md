# Xdecrypt
xshell密码恢复工具，用于读取本地的.xsh文件并解密其中的密码，适用各版本xshell。
本来是帮别人用python写的解密部分，写完干脆整理一下做个小工具。
## 使用方法
1. 打开终端或命令行提示符
2. 切换到 Xdecrypt.exe 文件所在的目录
3. 运行命令 Xdecrypt.exe
```
D:\Xdecrypt\dist>Xdecrypt.exe
找到.xsh文件路径：C:/Users/Lenovo/Documents/NetSarang Computer/7/Xshell/Sessions
--------------------
找到.xsh文件：
['新建会话.xsh']
--------------------
Host：xxx.xxx.xx.xxx
用户名：root
密码：xxxxxxxxxxxxx
--------------------

```
当您的.xsh文件不在默认目录时，您可以自行指定目录：
```
D:\Xdecrypt\dist>Xdecrypt.exe -p "C:/Users/Lenovo/Documents/NetSarang Computer/7/Xshell/Sessions"
自定义文件路径：C:/Users/Lenovo/Documents/NetSarang Computer/7/Xshell/Sessions
找到.xsh文件：
['新建会话.xsh']
--------------------
Host：xxx.xxx.xx.xxx
用户名：root
密码：xxxxxxxxx
--------------------

```
## 注意
- 本工具仅用于恢复您自己的密码，不得用于非法用途。
- 使用本工具造成的任何后果，均由使用者自行承担。
## 参考
https://github.com/JDArmy/SharpXDecrypt
https://github.com/HyperSine/how-does-Xmanager-encrypt-password
