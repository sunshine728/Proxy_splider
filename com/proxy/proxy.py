from sqlite3 import Time

import requests
import redis
from bs4  import BeautifulSoup
class Database:
    def __init__(self):
        self.host = 'localhost'
        self.port = 6379

    def write(self, website, ip_name,port_name):
        try:
            key = ip_name
            val = port_name
            r = redis.StrictRedis(host=self.host, port=self.port)
            r.set(key, val)
        except Exception as exception:
            print(exception)

    def read(self, website, ip_name):
        try:
            key = ip_name
            r = redis.StrictRedis(host=self.host, port=self.port)
            value = r.get(key)
            print(key,value)
            return value
        except Exception as exception:
            print(exception)

    def get_url(self,url):

# urls ={'https://www.kuaidaili.com/free/inha/1/','https://www.kuaidaili.com/free/inha/2/','https://www.kuaidaili.com/free/inha/3/'}
# for url in urls:
#         print(url)
        r = requests.get(url)
    # print('----------------------------------------------')
    #     print(r.text)
    # print('----------------------------------------------')
        soup = BeautifulSoup(r.text,'lxml')
        all_tr = soup.find_all('tr')
        # print(all_tr)
        for tr in all_tr:
            all_td = tr.find_all('td')
            all_td1 = [x for x in all_td]
            # print(all_td1)
            if all_td1.__len__()!=0:
                ip = all_td1[0].text.strip()
                port = all_td1[1].text.strip()
                # print("ip:"+"---"+ip,"port"+"---"+port)
                #写入redis数据库
                db = Database()
                db.write(ip,ip , port)
                db.read(ip,ip)
        r.close()
if __name__ == '__main__':
    Database.get_url(Database,'https://www.kuaidaili.com/free/inha/2/')
    Database.get_url(Database,'https://www.kuaidaili.com/free/inha/1/')
    Database.get_url(Database,'https://www.kuaidaili.com/free/inha/3/')