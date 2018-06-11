#_*_coding:utf-8_*_
import requests
import socket
import json
import time
import random
import sys
import threading
import redis



class proxy_server:
    def __init__(self,callback=None,host='localhost',port=20010):
        self.url='http://svip.kuaidaili.com/api/getproxy/?orderid=953994536123042&num=100&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=1&an_an=1&an_ha=1&sp1=1&quality=2&sort=1&format=json&sep=1'
        self.proxy_list=[]
        self.examing_url='http://www.eastmoney.com/'
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection':'close'
        }
        self.IP_addr = "127.0.0.1"
        self.port = 20100
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.pool1 = redis.ConnectionPool(host='localhost', port=6379)
        self.redis1 = redis.Redis(connection_pool=self.pool1)


        # self.callback = callback
        # try:
        #     self.s.bind((host, port))
        # except socket.error as msg:
        #     print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        #     sys.exit()
        # self.s.listen(10)


    def get_proxy_from_web(self):
        response1=requests.get(self.url)
        proxy_data=json.loads(response1.text)
        proxy_list= proxy_data['data']['proxy_list']
        return proxy_list


    def examing_proxy(self,proxy_list):
        for i in proxy_list:
            try:
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((self.IP_addr, self.port))
                timea = time.time()
                proxy_raw={
                    'http':'http://'+str(i),
                    'https':'http://'+str(i)
                }

                __nouse=requests.get(url=self.examing_url,proxies=proxy_raw,timeout=10)
                timeb=time.time()
                timeused=timeb-timea
                if timeused<3:
                    # proxy_good_dict={
                    #     'proxy':i,
                    #     'used_times':0
                    # }
                    proxy_good_dict={
                        'act':'save_proxy',
                        'proxy':i
                    }
                    while True:
                        # if len(self.proxy_list)<300:
                        #     self.proxy_list.append(proxy_good_dict)
                        #     break
                        proxy_json=json.dumps(proxy_good_dict)
                        self.s.send(proxy_json)
                        response=self.s.recv(1024)
                        if response=='full':
                            self.s.close()
                            print ('服务器的代理满了，正在等待')
                            time.sleep(5)
                            continue
                        elif response=='sucessed':
                            self.s.close()
                            break
                else:
                    self.s.close()
            except Exception as e:
                print (e)
                pass
        self.s.close()


    def get_proxy(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.IP_addr,self.port))
        while True:
            try:
                get_proxy_json=json.dumps({'act':'get_proxy'})
                self.s.send(get_proxy_json)
                # self.s.accept()
                response=self.s.recv(1024)
                break
            except Exception as e:
                print (e)
            finally:
                print ('get代理的时候，链接已关闭')
                self.s.close()
            # index=random.randint(0,len(self.proxy_list))
            # proxy=self.proxy_list[index]
            # if proxy['used_times']<10:
            #     self.proxy_list[index]['used_times']+=1
            #     break
            # else:
            #     self.proxy_list.remove(proxy)
        # return proxy['proxy']
        # print response


    def startlistening(self):
        while True:
            print ('正在监听')
            need_recv=True
            conn, addr = self.s.accept()
            while need_recv:
                data= conn.recv(1024)
                print (addr,'\n')
                if data=='get_proxy':
                    proxy=self.get_proxy()
                    conn.send(str(proxy))
                else:
                    conn.close()
                    break


    def run_local_proxy(self):
        while True:
            proxy_list=self.get_proxy_from_web()
            self.examing_proxy(proxy_list)


    def run(self):
        thread1=threading.Thread(target=self.run_local_proxy,args=())
        thread2=threading.Thread(target=self.get_proxy,args=())
        # thread1.run()
        thread1.run()
        time.sleep(20)
        thread2.run()
        thread1.join()
        thread2.join()






if __name__ == '__main__':
    thisclass=proxy_server()
    # thisclass.run()
    thisclass.get_proxy()