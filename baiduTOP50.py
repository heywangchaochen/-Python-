import requests
import parsel
import csv

# 导出csv
f = open(r'E:\Python_Data\百度热搜TOP50.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['排名', '标题', '摘要', '热度值', '热度'])
csv_writer.writeheader()

# 地址
url = 'https://top.baidu.com/board?tab=realtime'

# 获取表头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'cookie': 'BIDUPSID=CB798502BEE95CCF2EDD0E893119DCC5; PSTM=1708325724; BAIDUID=C3FBFFE7863F5D1C7A495B0F0EF58ED1:FG=1; BAIDUID_BFESS=C3FBFFE7863F5D1C7A495B0F0EF58ED1:FG=1; ZFY=0QANgHQca3w:AsTF7lPYq2Y:BlYT3UBG:ArSU6UxuOBxiU:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=39996_40171_40203_39661_40207_40217_40222_40255; PSINO=2; delPer=0'

}

# 发送请求
response = requests.get(url=url, headers=headers)
selector = parsel.Selector(response.text)

lis = selector.xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div')
# print(lis)

# 循环遍历
for li in lis:
    num = li.xpath('./a/div[1]/text()').get()           # 排名
    title = li.xpath('./div[2]/a/div[1]/text()').get()  # 标题
    short = li.xpath('./div[2]/div[2]/text()').get()    # 摘要
    core = li.xpath('./div[1]/div[2]/text()').get()     # 热度值
    hot = li.xpath('./div[2]/a/div[2]/text()').get()    # 热度

    dit = {
        '排名': num,
        '标题': title,
        '摘要': short,
        '热度值': core,
        '热度': hot

    }
    csv_writer.writerow(dit)

    print(num, title, short, core, hot)

