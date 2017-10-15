#_*_coding:utf-8_*_
import socket
import json
import random

class Sockerserver:
    def __init__(self):
        self.socket=socket.socket()
        self.IP_addr="127.0.0.1"
        self.port=20100
        try:
            self.socket.bind((self.IP_addr,self.port))
        except socket.errno,msg:
            print msg
        self.proxy_list=[]

    def runserver(self):
        self.socket.listen(100)
        while True:
            print '当前代理列表的数量--',len(self.proxy_list)
            conn,addr=self.socket.accept()
            data_recv=conn.recv(1024)
            try:
                data=json.loads(data_recv)
                data_act=data['act']
                if data_act=='save_proxy':
                    if len(self.proxy_list)>500:
                        conn.send('full')
                    else:
                        self.proxy_list.append(
                            {
                                'used_times':0,
                                'proxy':data['proxy']
                            }
                        )
                        conn.send('sucessed')

                elif data_act=='get_proxy':
                    while True:
                        index=random.randint(len(self.proxy_list))
                        proxy_dict=self.proxy_list[index]
                        if proxy_dict['used_times']<5:
                            proxy=proxy_dict['proxy']
                            self.proxy_list[index]['used_times']+=1
                            conn.send(proxy)
                            break
                        else:
                            self.proxy_list.remove(proxy_dict)
                else:
                    continue

            except Exception as e:
                print e

if __name__ == '__main__':
    thisclass=Sockerserver()
    thisclass.runserver()