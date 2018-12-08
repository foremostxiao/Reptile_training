import requests
import json
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import os
import sys
#添加环境变量
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from conf import settings
def movice_lists(session):
    # 分类url
    get_url = 'http://movie.douban.com/typerank'
    param = {
        'type_name': '喜剧',
        'type': '24',
        'interval_id': '100:90',
        'action': '',
    }
    response = session.get(url=get_url, headers=settings.headers, params=param, proxies=settings.proxy)

    #获取当前页并保存在本地
    page_text = response.text
    data_path = settings.data_path
    comedy_file = os.path.join(data_path, 'douban.html')

    with open(comedy_file, 'w', encoding='utf-8')as f:
        f.write(page_text)
        print('定位到喜剧页面，并保存到本地')

    # 使用selenium+phantomJs处理页面动态加载数据的爬取

    # window
    bro = webdriver.PhantomJS(executable_path=settings.phantomjs_win_file)

    # mac
    #bro = webdriver.PhantomJS(executable_path=settings.phantomjs_mac_file)

    # -------------------------重点解决-------------------
    # 怎么根据获取url
    # bro.get(url)
    # 本次我直接输入的网址，怎么使其获取个人主页下的电影排行榜，显示已登陆状态

    bro.get('https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action=')
    page_text = bro.page_source
    bro_file = settings.data_path
    bro_text = os.path.join(bro_file,'bro_text.html')
    with open(bro_text,'w', encoding='utf-8')as f:
        f.write(page_text)
    print('bro success')

    sleep(1)
    data_path = settings.data_path
    photo = os.path.join(data_path, 'current.png')
    bro.save_screenshot(photo)

#-------------------True-----------------------------------
    js = 'window.scrollTo(0,2000)'
    # 如何让浏览器对象执行js代码
    bro.execute_script(js)
    sleep(1)
    data_path = settings.data_path
    photo2 = os.path.join(data_path, 'current2.png')
    bro.save_screenshot(photo2)

    # 获取加载数据后的页面: page_source获取浏览器当前数据
    page_text = bro.page_source
    soup = BeautifulSoup(page_text, 'lxml')
    a_list = soup.select('.movie-list-item > .movie-content > a')
    print('page_source sucess')

    for a in a_list:
        movie_url = a['href']
        # 获取详细内容
        get_content(movie_url)

def get_content(movie_url):
    content_page = requests.get(url=movie_url, headers=settings.headers, proxies=settings.proxy).text
    soup = BeautifulSoup(content_page, 'lxml')
    rating_num = soup.select('.rating_self .rating_num')[0].text
    img_url = soup.select('#mainpic > a > img')[0]['src']
    movie_name = soup.select('#content > h1 > span')[0].text
    movie_name = movie_name.split(' ')[0]
    # print('电影名字：', movie_name)

    # 下面的方法可以获取全部内容
    content_list = ''
    content_list += '电影名字:' + movie_name + '\n' + '海报url:' + img_url+'\n'+'豆瓣评分:'+rating_num
    span_class = soup.select('#info')
    for index in span_class:
        content = index.text
        content_list += content
    print(content_list)
    data_path = settings.data_path
    file_name = os.path.join(data_path,movie_name+'.json')
    with open(file_name, 'w', encoding='utf-8')as f:
        json.dump(content_list, f)