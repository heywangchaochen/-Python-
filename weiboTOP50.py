# 2024.02.20
# 爬取微博热搜

import requests
import parsel
import csv

f = open(r'E:\Python_Data\微博热搜TOP50.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['排名', '标题', '热度值', '热度'])
csv_writer.writeheader()

# 地址
url = 'https://s.weibo.com/top/summary'
# 获取表头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'cookie': 'SUB=_2AkMSj3JLf8NxqwFRmfoQym_nZIt2yw_EieKk04OQJRMxHRl-yT9vqlAmtRB6OQ9cpGGRTe8pfZcAEUF83xkBSXegKncb; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhiEEzDju6ocs9mcBKrpl7g; _s_tentry=passport.weibo.com; Apache=3818410529414.6377.1708391806443; SINAGLOBAL=3818410529414.6377.1708391806443; ULV=1708391806454:1:1:1:3818410529414.6377.1708391806443:',
}

# 发送请求
response = requests.get(url=url, headers=headers)
selector = parsel.Selector(response.text)

lis = selector.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')
# print(lis)

# 循环遍历
for li in lis:
    num = li.xpath('./td[1]/text()').get()  # 排名
    title = li.xpath('./td[2]/a/text()').get()  # 标题
    core = li.xpath('./td[2]/span/text()').get()  # 热度值
    hot = li.xpath('./td[3]/i/text()').get()    # 热度

# 判断、替换关键字
#     message = "置顶" if num == None else num
#     print(message, title, core, hot)

    dit = {
        '排名': num,
        '标题': title,
        '热度值': core,
        '热度': hot,

    }
    csv_writer.writerow(dit)
    print(num, title, core, hot)



