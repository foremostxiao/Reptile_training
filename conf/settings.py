import os,random
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
conf_file = os.path.join(BASE_DIR,"conf")
data_path = os.path.join(BASE_DIR,"data")
phantomjs_mac_file = os.path.join(conf_file,"phantomjs-2.1.1-macosx","bin",'phantomjs')
phantomjs_win_file = os.path.join(conf_file,"phantomjs-2.1.1-windows","bin",'phantomjs')


# IP段配置，如果失效了就要再去http://www.goubanjia.com/找http的ip段
proxy_list = [
    {"http": "35.230.96.112:80"},
    {'http': '221.7.255.168:8080'},
    {'http': '39.137.77.66:8080'},
    {'http': '223.19.141.26:80'},
    {'http': '212.46.220.214:80'},
    {'http': '123.57.76.102:80'},
]
proxy = random.choice(proxy_list)

headers =  {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 "
    "(KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}







