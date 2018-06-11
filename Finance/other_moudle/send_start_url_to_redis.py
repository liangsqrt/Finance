#_*_coding:utf-8_*_
import redis
import requests
import random

#
redis1=redis.StrictRedis(host='127.0.0.1',port=6379,db=1)

all_website_key= redis1.keys('*')


web_begin_url_config={
    'DFCFW_news':'http://www.eastmoney.com/',
    'DFCFW_all_page': 'http://www.eastmoney.com/',

}




def send_ConfigWebname_to_redis():
    '''
    将配置文件中的爬虫全部发送到reids中去。
    :return:
    '''
    for webname in web_begin_url_config.keys():
        try:
            redis1.lpush(webname+':start_urls',web_begin_url_config[webname])
        except Exception as e:
            print(e)

def get_all_Rediswebsite_name():
    '''
    返回Redis中的所有爬虫的名称

    :return:
    '''
    webname=set()
    for onewebsite in all_website_key:
        try:
            if ':' in onewebsite:
                website_name=onewebsite.split(':')[0]
                webname.add(website_name)
        except Exception as e:
            print (e)

    print (len(webname))
    for onewebname in webname:
        print (onewebname)

    return list(webname)

def send_start_url_to_redis(web_name):
    '''
    将某个爬虫推送到redis中去

    :param web_name:
    :return:
    '''
    if web_name in web_begin_url_config.keys():
        redis1.lpush(str(web_name)+':start_urls',str(web_begin_url_config[web_name]))
    else:
        print (web_name,' is not defined')

def deal_web_dupefilter(web_name):
    '''
    删除一个网站对应的dupefilter

    :param web_name:
    :return:
    '''
    try:
        redis1.delete(web_name+':dupefilter')
    except Exception as e:
        print (e)

def deal_web_items(web_name):
    '''
    删除某个网站中的item
    :param web_name:
    :return:
    '''
    try:
        redis1.delete(web_name+':items')
    except Exception as e:
        print (e)

def deal_web_start_urls(web_name):
    '''
    删除某个网站的start_urls
    :param web_name:
    :return:
    '''
    try:
        redis1.delete(web_name+':start_urls')
    except Exception as e:
        print(e)

def deal_web_requests(web_name):
    '''
    删除某个万盏的requests
    :param web_name:
    :return:
    '''
    try:
        redis1.delete(web_name+':requests')
    except Exception as e:
        print(e)



def clear_redis():
    '''
    清空redis中与网站有关的所有数据。
    :return:
    '''
    for n,one in enumerate(get_all_Rediswebsite_name()):
        # send_start_url_to_redis(one)
        deal_web_dupefilter(one)
        deal_web_items(one)
        deal_web_requests(one)
        deal_web_start_urls(one)







if __name__ == '__main__':
    # clear_redis()

    # send_ConfigWebname_to_redis()

    # deal_web_dupefilter('tchrd')

    send_start_url_to_redis('DFCFW_all_page')