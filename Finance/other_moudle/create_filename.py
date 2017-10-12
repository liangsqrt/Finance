#_*_coding:utf-8_*_
import hashlib
import os



def DFCFW_forumdata_name(url,datetime):
    urlmd5=hashlib.md5(url).hexdigest()
    date=datetime.split(' ')[0]
    return date,urlmd5


def checkfile(filepath):
    dir_path=filepath.rsplit('/',1)[0]
    if os.path.exists(dir_path):
        pass
    else:
        os.makedirs(dir_path)

if __name__ == '__main__':
#     DFCFW_forumdata_name(url='www.baidu.com',datetime='12:12 12')
    checkfile('E:/matlab 2014a/appdata/data/data')