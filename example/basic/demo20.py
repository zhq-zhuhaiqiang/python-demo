#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
利用第三方接口实现输入QQ号判断是否在线
"""

import requests,json
from xml.etree import ElementTree as ET
# import numpy as np

def is_online(qq_num):
    """
    调用第三方接口，查询qq号码是否在线
    :param qq_num: QQ号码，String
    :return: node.text String
    """
    data = requests.get("http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx/qqCheckOnline?qqcode=%s" % qq_num)
    # print(json.dumps(data,cls=MyEncoder,indent=4))
    result = data.text
    print('result:')
    print(result)
    node = ET.XML(result)
    print('node:')
    print(node)
    print('node.text:')
    print(node.text)

    return node.text
    
# class MyEncoder(json.JSONEncoder):
#    def default(self, obj):
#     if isinstance(obj, np.ndarray):
#       return obj.tolist()
#     elif isinstance(obj, bytes):
#       return str(obj, encoding='utf-8')
#     return json.JSONEncoder.default(self, obj)
def main():
  
    """
    主函数
    :return: None
    """
    pass
    print(456)
    # exit() 
    try:
      inp=0
      print("处理异常开始".center(20,"="))
      # return
      # b=1/0
      inp = input("请输入要查询的QQ号：")
      print("我在抛异常的后面")
      
    except Exception as e:
      pass
      print("我是一个异常:",e)
      return
      # exit()  
    else :
      print("居然没有异常抛出")
    finally:
      print("我是finally分支")
      
    print("处理异常结束")
    print(inp)
    result = is_online(inp)
    if result == "Y":
        print("[%s]在线" % inp)
    elif result == "N":
        print("[%s]离线" % inp)
    elif result == "E":
        print("QQ号码错误！")
    else:
        print("您输入的内容有误！")

# print(__name__)
if __name__ == '__main__':
    main()
