import requests
from lxml import etree
import os,sys
#添加环境变量
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from normal import test2
from captcha import test
from conf import settings
# 指定url
url = 'http://www.douban.com/accounts/login'
session = requests.session()
# 登录界面的情况
response = session.get(url=url, headers=settings.headers, proxies=settings.proxy)
page_text = response.text
tree = etree.HTML(page_text)
# 如果出现验证码的div
captcha = tree.xpath('//div[@class="item item-captcha"]')
# 如果出现验证码先进行解码处理
if captcha:
    print('输入框出现验证码，使用破解验证码的登录方式')
    test.captcha_way()

else:
    print('输入框没有出现验证码，按正常的方法登录')
    test2.normal_way()



