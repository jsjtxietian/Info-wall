#人、时间、地点、事件
#关系

from faker import Faker
fake = Faker(locale='zh_CN')

print(fake.name())
print(fake.company())
print(fake.date(pattern="%Y-%m-%d", end_datetime=None))
print(fake.email())
print(fake.job())
print(fake.phone_number())
print(fake.profile(fields=None, sex=None))

'''
fake.day_of_month()
# '04'
fake.day_of_week()
# 'Tuesday'
fake.month()
# '04'
fake.month_name()
# 'January'
fake.year()
# '2018'
fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
# '业务方面下载大学数据内容这是.生产类型方法的是还有她的.'

fake.paragraphs(nb=3, ext_word_list=None)
# [   '次数免费完全提高不会人民.过程帮助朋友现在完全最后什么.您的最新客户这是在线工程必须.',
#     '社会喜欢标准各种.不断那么希望在线来源已经.',
#     '欢迎留言客户发布控制.']

fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
# '参加以及下载网站成为企业注册.'

fake.sentences(nb=3, ext_word_list=None)
# ['之后国际她的任何地方起来表示.', '应该同时报告科技其实你们查看.', '事情已经基本阅读生产经济.']

fake.text(max_nb_chars=200, ext_word_list=None)
# ('威望开始有关他们当然的人信息其中.不是项目留言表示但是.\n'
#  '关于的话教育.\n'
#  '软件进入进行可是自己.\n'
#  '这种各种通过广告类别图片位置.分析类别中心全国研究.已经一起自己介绍责任留言.\n'
#  '大小回复加入一定网站注册产品.地方工具或者.设计国家资料工作只有新闻.\n'
#  '发展经验业务设计或者.信息作者就是来源因为等级.')

fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)
# [   '关系或者知道这些的话首页孩子.项目北京的人用户社会同时.实现这个起来他们需要显示.\n'
#     '自己我的比较.数据需要比较然后.如果研究加入她的.一样简介进入这个.\n'
#     '作为研究会员最新论坛或者.拥有名称标准原因.无法能力免费这么.\n'
#     '次数游戏拥有可能.一般查看网站两个.更新首页精华生产简介任何中心行业.\n'
#     '感觉开发查看简介可是.以上类型北京国家中心结果.她的然后说明查看参加以上积分.',
#     '注意标准品牌这些网站不会.分析点击日本这是.\n'
#     '标题阅读浏览过程一下会员.\n'
#     '广告介绍生活作者.有限简介一点新闻要求一次增加.一起同时全部环境免费技术语言之间.\n'
#     '数据的人文化不同之后因此生产.可以一直两个应用.直接原因积分不断搜索.\n'
#     '以后直接作品目前文件为了下载.基本社会大学发生时候类型.进行开发科技其实那个不同以及.研究以及但是.\n'
#     '评论企业出来投资.空间系列注册基本发现一些不要东西.',
#     '她的因为合作如果简介不同方面.活动报告首页成功.\n'
#     '等级不是标题.需要电脑部门城市生产有限.更多选择日期所以活动任何.\n'
#     '不断网上都是发展之间标题.\n'
#     '作者应用分析更新状态介绍登录.回复学校这些技术.\n'
#     '不能希望那个一切朋友完成说明特别.日期制作推荐方法部门运行市场.精华解决服务很多.\n'
#     '全部首页作品虽然业务.市场就是位置情况计划次数.重要空间选择功能原因.能够所以地址网上很多要求必须注意.']

fake.word(ext_word_list=None)
# '自己'

fake.words(nb=3, ext_word_list=None, unique=False)
# ['女人', '作者', '国内']
fake.profile(fields=None, sex=None)
# {   'address': '海南省秀芳市沈北新关岭街E座 301460',
#     'birthdate': datetime.date(1986, 7, 3),
#     'blood_group': 'AB-',
#     'company': '浙大万朋信息有限公司',
#     'current_location': (Decimal('75.9179895'), Decimal('-113.410597')),
#     'job': '平面设计总监',
#     'mail': 'xiulan78@gmail.com',
#     'name': '钟玉英',
#     'residence': '广东省长春县清浦王街Z座 699016',
#     'sex': 'M',
#     'ssn': '340303193703308923',
#     'username': 'mingma',
#     'website': [   'https://www.yan.cn/',
#                    'https://www.yanyu.net/',
#                    'https://www.ae.cn/']}

fake.simple_profile(sex=None)
# {   'address': '香港特别行政区淑华县西峰长沙街w座 297158',
#     'birthdate': datetime.date(1923, 4, 15),
#     'mail': 'jkang@yahoo.com',
#     'name': '朱宇',
#     'sex': 'F',
#     'username': 'jhao'}

fake.csv(header=None, data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False)
# ('"江佳","宁夏回族自治区勇县海港刘路t座 572661"\r\n'
#  '"陈婷婷","天津市南宁县大东嘉禾街W座 761105"\r\n'
#  '"黄龙","广西壮族自治区桂英县南湖香港路n座 517837"\r\n'
#  '"陈超","河南省杨县西夏杨路H座 607944"\r\n'
#  '"吴丽娟","重庆市博市海陵贵阳街X座 467534"\r\n'
#  '"陈磊","四川省婷婷县安次屈路h座 650699"\r\n'
#  '"刘峰","湖北省海口县孝南唐街c座 749665"\r\n'
#  '"钟旭","香港特别行政区明市怀柔许街u座 679878"\r\n'
#  '"刘杰","黑龙江省秀英市平山六盘水路z座 289684"\r\n'
#  '"贺秀兰","湖北省兵市蓟州王街i座 785795"\r\n')

'''