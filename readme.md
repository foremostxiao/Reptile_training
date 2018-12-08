作业题目：
动态爬取豆瓣电影中“更多”电影详情数据
作业需求:

1.使用任意代理IP进行如下操作
2.使用requests模块进行豆瓣电影的个人用户登录操作
3.使用requests模块访问个人用户的电影排行榜->分类排行榜->任意分类对应的子页面
4.爬取需求3对应页面的电影详情数据
5.爬取3对应页面中滚动条向下拉动2000像素后加载出所有电影详情数据，存储到本地json文件中或者相应数据库中
【备注】电影详情数据包括：海报url、电影名称、导演、编剧、主演，类型，语言，上映日期，片长，豆瓣评分

建议：用Pycharm开发

测试环境：win7系统，python3.7.0，工具:pycharm-Profession-2018.2.4

目录结构：
	douban
		-captcha                          # 有验证码出现时的情况
			-get_Code.py                  # 验证码处理---云打码处理
			-test.py					  # 验证码情况下获取电影数据的主逻辑
		-conf								
			-phantomjs-2.1.1-macosx       # 根据使用者测试的版本进行选择，
			-phantomjs-2.1.1-windows
			-settings.py			      # 配置文件	
		-data                             # 数据存储
		-normal                           # 没有验证码的情况
			-test2.py                     # 没有验证码获取电影数据的主逻辑
		-mian.py						  # 程序开始
		-move_list.py                     # 有验证码和无验证码公用的逻辑代码

存在的疑惑：
在movie_list.py文件中
session = requests.session()

1、使用selenium+phantomJs处理页面动态加载数据的爬取

怎么根据获取url
bro.get(url)
本次我直接输入的网址，怎么使其获取个人主页下的电影排行榜，显示已登陆状态


