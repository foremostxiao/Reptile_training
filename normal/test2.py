import requests
import os
import sys
#添加环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
import movie_list


def normal_way():
    session = requests.session()
    # 1.发起登录请求：将cookie获取，切换存储到session对象中
    login_url = 'https://accounts.douban.com/login'
    # post 请求 ---data参数
    data = {

        'source': 'movice',
        'redir': 'https://movie.douban.com/',
        'form_email': '836342406@qq.com',
        'form_password': 'douban836342406,.',
        'login': '登录',
    }

    # 定位到具体分类排行榜
    login_response = session.post(url=login_url, data=data, headers=settings.headers, proxies=settings.proxy)
    print('login_success')

    # 2.发起请求(session(cookie))，获取响应页面数据
    movie_list.movice_lists(session)


