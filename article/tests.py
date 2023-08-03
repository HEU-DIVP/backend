from django.test import TestCase

# Create your tests here.

## TODO: 启航网团情动态
# import requests
# import time
# import datetime
# from fake_useragent import UserAgent
# from lxml import etree
# from article.models import Article
#
# text_ls = []
# link_ls = []
# sleep_time = 0.1
# date_format = '%Y-%m-%d'
#
# for page in range(1, 30):
#     print(f'##### page {page} #####')
#     if page == 1:
#         url = 'http://qihang.hrbeu.edu.cn/960/list.htm'
#     else:
#         url = f'http://qihang.hrbeu.edu.cn/960/list{page}.htm'
#     res = requests.get(url=url, headers={'user-agent': UserAgent().random})
#     res.encoding = 'utf-8'
#     html = res.text
#     e = etree.HTML(html)
#     ele_link_ls = e.xpath('//span[@class="Article_Title"]/a/@href')
#     ele_text_ls = e.xpath('//span[@class="Article_Title"]/a/@title')
#
#     for link, title in zip(ele_link_ls, ele_text_ls):
#         if 'weixin' not in link:
#             _link = 'http://qihang.hrbeu.edu.cn' + link
#         else:
#             _link = link
#         link_ls.append(_link)
#         text_ls.append(title)
#     time.sleep(sleep_time)
#
#     # for link, title in zip(link_ls, title_ls):
#     #     print(f'{link} - {title}')
#
# count = 0
#
# for text, link in zip(text_ls, link_ls):
#     if 'weixin' in link or 'redirect' in link:
#         try:
#             timer = '1970-01-01'
#             Article.objects.create(
#                 title=text,
#                 source_id=3,
#                 url=link,
#                 click_count=0,
#                 create_time=datetime.datetime.strptime(timer, date_format).date()
#             )
#         except Exception as e:
#             print(str(e))
#         else:
#             print(f'line {count} - ok')
#             count += 1
#             continue
#     res = requests.get(url=link, headers={'user-agent': UserAgent().random})
#     res.encoding = 'utf-8'
#     html = res.text
#     e = etree.HTML(html)
#     timer_ls = e.xpath('//*[@id="container"]/div/div/p/span[3]')
#     click_ls = e.xpath('//*[@id="container"]/div/div/p/span[4]/span')
#     timer = ''
#     try:
#         click_num = click_ls[0].xpath('string(.)').strip()
#         timer = timer_ls[0].xpath('string(.)')
#     except Exception as e:
#         print(str(e))
#         click_num = 0
#         timer = '1970-01-01'
#     try:
#         Article.objects.create(
#             title=text,
#             source_id=3,
#             url=link,
#             click_count=click_num,
#             create_time=datetime.datetime.strptime(timer[5:15], date_format).date()
#         )
#     except Exception as e:
#         print(str(e))
#     else:
#         print(f'line {count} - ok')
#         count += 1
#
#     time.sleep(sleep_time)

## TODO: 启航网创新工作
# import requests
# import time
# import datetime
# from fake_useragent import UserAgent
# from lxml import etree
# from article.models import Article
#
# text_ls = []
# link_ls = []
# sleep_time = 0.1
# date_format = '%Y-%m-%d'
#
# for page in range(1, 25):
#     print(f'##### page {page} #####')
#     if page == 1:
#         url = 'http://qihang.hrbeu.edu.cn/964/list.htm'
#     else:
#         url = f'http://qihang.hrbeu.edu.cn/964/list{page}.htm'
#     res = requests.get(url=url, headers={'user-agent': UserAgent().random})
#     res.encoding = 'utf-8'
#     html = res.text
#     e = etree.HTML(html)
#     ele_link_ls = e.xpath('//span[@class="Article_Title"]/a/@href')
#     ele_text_ls = e.xpath('//span[@class="Article_Title"]/a/@title')
#
#     for link, title in zip(ele_link_ls, ele_text_ls):
#         if 'weixin' not in link:
#             _link = 'http://qihang.hrbeu.edu.cn' + link
#         else:
#             _link = link
#         # _link=link
#         link_ls.append(_link)
#         text_ls.append(title)
#     time.sleep(sleep_time)
#
#     # for link, title in zip(link_ls, title_ls):
#     #     print(f'{link} - {title}')
#
# count = 0
#
# for text, link in zip(text_ls, link_ls):
#     if 'weixin' in link or 'redirect' in link:
#     # if 'qihang' not in link:
#         # print(link)
#         try:
#             timer = '1970-01-01'
#             Article.objects.create(
#                 title=text,
#                 source_id=9,
#                 url=link,
#                 click_count=0,
#                 create_time=datetime.datetime.strptime(timer, date_format).date()
#             )
#         except Exception as e:
#             print(str(e))
#         else:
#             print(f'line {count} - ok')
#             count += 1
#             continue
#     res = requests.get(url=link, headers={'user-agent': UserAgent().random})
#     res.encoding = 'utf-8'
#     html = res.text
#     e = etree.HTML(html)
#     timer_ls = e.xpath('//*[@id="container"]/div/div/p/span[3]')
#     click_ls = e.xpath('//*[@id="container"]/div/div/p/span[4]/span')
#     timer = ''
#     try:
#         click_num = click_ls[0].xpath('string(.)').strip()
#         timer = timer_ls[0].xpath('string(.)')
#     except Exception as e:
#         print(str(e))
#         click_num = 0
#         timer = '1970-01-01'
#     try:
#         Article.objects.create(
#             title=text,
#             source_id=9,
#             url=link,
#             click_count=click_num,
#             create_time=datetime.datetime.strptime(timer[5:15], date_format).date()
#         )
#     except Exception as e:
#         print(str(e))
#     else:
#         print(f'line {count} - ok')
#         count += 1
#
#     time.sleep(sleep_time)

## TODO: 工学
# import requests
# import time
# import datetime
# from fake_useragent import UserAgent
# from lxml import etree
#
# from article.models import Article
#
# total_page = 2198
# for page in range(259, total_page + 1):
#     print(f'##### page {page} #####')
#     if page == 1:
#         url = 'http://gongxue.cn/xw.htm'
#     else:
#         url = f'http://gongxue.cn/xw/{total_page - page + 1}.htm'
#     res = requests.get(
#         url=url,
#         headers={'user-agent': UserAgent().random}
#     )
#     res.encoding = 'utf-8'
#     html = res.text
#     e = etree.HTML(html)
#     ele_link_ls = e.xpath('//div[@class="list-right-tt txt-elise"]/a/@href')
#     ele_text_ls = e.xpath('//div[@class="list-right-tt txt-elise"]/a/text()')
#     for link, title in zip(ele_link_ls, ele_text_ls):
#         if str(link)[0] == '.':
#             _link = 'http://gongxue.cn/' + str(link)[3:]
#         elif 'http' in str(link):
#             _link = link
#         else:
#             _link = 'http://gongxue.cn/' + str(link)
#         # print(f'{link} - {title}')
#         res = requests.get(
#             url=f'http://gongxue.cn/{link}',
#             headers={'user-agent': UserAgent().random}
#         )
#         res.encoding = 'utf-8'
#         html = res.text
#         e = etree.HTML(html)
#         click_id = str(link).split('/')[-1].split('.')[0]
#         if 'gongxue' in _link:
#             timer_ls = e.xpath('//*[@id="print"]/div[4]/div[4]/text()')
#         else:
#             timer_ls = ['1970-01-01']
#         if not timer_ls:
#             timer_ls = e.xpath('/html/body/div[3]/div[2]/form/div[2]/div[1]/text()')
#         try:
#             if len(timer_ls[0]) < 10:
#                 timer_ls = e.xpath('//*[@id="print"]/div[4]/div[5]/text()')
#         except Exception as e:
#             print(str(e))
#             print(_link)
#             continue
#         try:
#             click_count = requests.get(
#                 url=f'http://gongxue.cn/system/resource/code/news/click/dynclicks.jsp?clickid={click_id}&owner=1600759291&clicktype=wbnews',
#                 headers={'user-agent': UserAgent().random}
#             ).text
#         except Exception as e:
#             print(str(e))
#             print(_link)
#             continue
#         try:
#             Article.objects.create(
#                 title=title,
#                 source_id=10,
#                 url=_link,
#                 click_count=click_count,
#                 create_time=datetime.datetime.strptime(timer_ls[0], '%Y-%m-%d').date()
#             )
#         except Exception as e:
#             print(str(e))
#             continue
#         else:
#             print(f'{_link} - {click_count} - {timer_ls[0]} - ok')
#         time.sleep(0.1)
