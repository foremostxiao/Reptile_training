from captcha import get_Code
import requests
from lxml import etree
import re,os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
import movie_list
def captcha_way():
    session = parse_captcha()

    movie_list.movice_lists(session)

def parse_captcha():
    url = 'https://www.douban.com/accounts/login?source=movie'
    # 个人主页的登录刚开始
    # url = 'https://www.douban.com/accounts/login'

    session = requests.session()
    page_text = session.get(url=url, headers=settings.headers, proxies=settings.proxy).text
    #  2.可以将页面数据中验证码进行解析，验证码图片下载到本地
    tree = etree.HTML(page_text)
    # 验证码图片xpath 的值： //*[@id="captcha_image"]
    codeImg_url = tree.xpath('//*[@id="captcha_image"]/@src')[0]
    # 获取了验证码图片的二进制数据值
    code_img = session.get(url=codeImg_url, headers=settings.headers, proxies=settings.proxy).content

    # 获取captcha-id
    # 正则解析
    # 使用re.S参数以后，正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。
    # <img id="captcha_image" src="https://www.douban.com/misc/captcha?id=O1pMk4XJ7wuKuLz8DYhVZpw3:en&amp;size=s" alt="captcha" class="captcha_image">
    c_id = re.findall('<img id="captcha_image".*?id=(.*?)&amp.*?>', page_text, re.S)[0]
    captcha_file = os.path.join(settings.data_path,'code.png')
    with open(captcha_file, 'wb')as f:
        f.write(code_img)

    # 调用验证码函数，获取识别结果
    codeText = get_Code.getCode(captcha_file)
    print(codeText)

    # 进行登录操作
    # 查看header下的url：
    post = 'https://accounts.douban.com/login'

    data = {
        "source": "movie",
        "redir": "https://movie.douban.com/",
        "form_email": "15027900535",
        "form_password": "bobo@15027900535",
        "captcha-solution": codeText,
        "captcha-id": c_id,
        "login": "登录",
    }

    print(c_id)
    login_text = session.post(url=post, data=data, headers=settings.headers, proxies=settings.proxy).text
    print('douban 登录成功')
    # with open('./index2.html', 'w', encoding='utf-8')as f:
    #     f.write(login_text)
    return session

#captcha_way()