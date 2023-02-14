import argparse
import os

import RC4
import base64
import hashlib
import win32api
import win32security
import re


class Xsh:  # .xsh文件中的相关信息
    def __init__(self):
        self.Host = ''
        self.UserName = ''
        self.Password = ''
        self.encryptPw = ''
        self.Version = ''


def Xdecrypt(pw, userSID, username, version):  # 解密函数
    decrypted = ''
    if version.startswith('5.0') or version.startswith('4') or version.startswith('3') or version.startswith('2'):
        data = base64.b64decode(pw)  # base64解码
        string_to_hash = "!X@s#h$e%l^l&"
        hash_object = hashlib.md5()
        hash_object.update(string_to_hash.encode())
        key = hash_object.digest()  # md5加密
        pass_data = data[:(len(data) - 32)]
        decrypted = RC4.rc4_algorithm('decrypt', pass_data, key)  # RC4加密
    elif version.startswith('5.1') or version.startswith('5.2'):
        data = base64.b64decode(pw)
        hash_object = hashlib.sha256()
        hash_object.update(userSID.encode())
        key = hash_object.digest()
        pass_data = data[:(len(data) - 32)]
        decrypted = RC4.rc4_algorithm('decrypt', pass_data, key)
    elif version.startswith('5') or version.startswith('6')or version.startswith('7.0'):
        data = base64.b64decode(pw)
        hash_object = hashlib.sha256()
        hash_object.update(bytes(username + userSID, 'utf-8'))
        key = hash_object.digest()
        pass_data = data[:(len(data) - 32)]
        decrypted = RC4.rc4_algorithm('decrypt', pass_data, key)
    elif version.startswith('7'):
        str1 = username[::-1] + userSID
        str2 = str1[::-1]   # 字符串倒序
        data = base64.b64decode(pw)  # b64解码
        hash_object = hashlib.sha256()  # sha256编码
        hash_object.update(bytes(str2, 'utf-8'))
        key = hash_object.digest()
        pass_data = data[:(len(data)-32)]
        decrypted = RC4.rc4_algorithm('decrypt',pass_data,key)  # RC4加密
    return decrypted


def find_path():
    user = win32api.GetUserName()
    path = f"C:/Users/{user}/Documents/NetSarang Computer/7/Xshell/Sessions"
    if os.path.exists(path):
        print(f"找到.xsh文件路径：{path} ")
        print("--------------------")
        return path
    else:
        print("找不到.xsh文件路径")


def find_info(path):
    username = win32api.GetUserName()  # 本地
    SID = win32security.LookupAccountName(None, username)[0]
    SID = win32security.ConvertSidToStringSid(SID)
    fields = ["Password", "UserName", "Host", "Version"]
    files = [f for f in os.listdir(path) if f.endswith('.xsh')]
    print("找到.xsh文件：")
    print(files)
    for file in files:
        # 读取文件内容
        with open(os.path.join(path, file), 'r', encoding='utf-16') as f:
            content = f.read()
        values = []
        for field in fields:
            pattern = fr"{field}=(.*)"
            match = re.search(pattern, content)
            if match:
                values.append(match.group(1))
            else:
                values.append("")
        # print(values)
        xsh = Xsh()
        xsh.encryptPw = values[0]
        xsh.UserName = values[1]
        xsh.Host = values[2]
        xsh.Version = values[3]
        xsh.password = Xdecrypt(xsh.encryptPw, SID, username, xsh.Version)
        print("--------------------")
        print("Host：" + xsh.Host)
        print("用户名："+xsh.UserName)
        print("密码："+xsh.password)
        print("--------------------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='the path of Xshell session file')
    args = parser.parse_args()
    if args.path:
        print(f"自定义文件路径：{args.path}")
        find_info(args.path)
    else:
        path = find_path()
        find_info(path)

