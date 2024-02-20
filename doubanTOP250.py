# 2024.02.20
# 爬取豆瓣电影排行TOP250

import requests
import parsel
import csv

f = open(r'E:\Python_Data\豆瓣电影 Top 250.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['电影名', '电影信息', '评分', '评价人数', '摘引', '豆瓣详情页'])
csv_writer.writeheader()
num = 0
while num <= 225:
    url = f'https://movie.douban.com/top250?start={num}&filter='
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    selector = parsel.Selector(response.text)
    # print(selector)
    lis = selector.xpath('//*[@id="content"]/div/div[1]/ol/li')

    for li in lis:
        movie_name = li.xpath('.//div/div[2]/div[1]/a/span[1]/text()').get()  # 电影名
        movie_info = li.xpath('.//div/div[2]/div[2]/p[1]/text()').getall()  # 电影信息
        movie_info = (''.join(movie_info).strip()).replace('\n', '')
        movie_score = li.xpath('.//div/div[2]/div[2]/div/span[2]/text()').get()  # 电影评分
        movie_num = li.xpath('.//div/div[2]/div[2]/div/span[4]/text()').get()  # 评价人数
        movie_lines = li.xpath('.//div/div[2]/div[2]/p[2]/span/text()').get()  # 电影摘引
        movie_href = li.xpath('.//div/div[2]/div[1]/a/@href').get()  # 豆瓣电影详情页

        dit = {
            '电影名': movie_name,
            '电影信息': movie_info,
            '评分': movie_score,
            '评价人数': movie_num,
            '摘引': movie_lines,
            '豆瓣详情页': movie_href

        }
        csv_writer.writerow(dit)
        print(movie_name, movie_info, movie_score, movie_num, movie_lines, movie_href)
    num += 25
