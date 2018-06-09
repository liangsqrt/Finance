#_*_coding:utf-8_*_
import os
import platform



ENCNname_dict={
    'DFCFW_news':'东方财富网新闻'
}

def getNameCN(ENname):

    if ENname in ENCNname_dict.keys():
        cnName= ENCNname_dict[ENname]
    else:
        cnName= '未知网站'
    if platform.system() != 'Linux':
        # cnName=cnName.decode('utf-8').encode('gbk')
        cnName=cnName#全程使用utf-8以免出错

    return cnName