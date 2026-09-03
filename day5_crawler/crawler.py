import requests
import re
import csv
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36'
}


def get_html(url):
    r = requests.get(url, headers=headers, timeout=10)
    r.encoding = 'utf-8'
    return r.text


f = open('douban.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(f)
writer.writerow(['排名', '电影名', '评分', '评价人数'])

for start in range(0, 250, 25):
    url = 'https://movie.douban.com/top250?start=%d' % start
    print('正在抓取', url)
    soup = BeautifulSoup(get_html(url), 'html.parser')
    items = soup.find_all('div', class_='item')
    for item in items:
        rank = item.find('em').get_text()
        name = item.find('span', class_='title').get_text()
        score = item.find('span', class_='rating_num').get_text()
        m = re.findall(r'(\d+)人评价', str(item))
        renshu = m[0] if m else '未知'
        writer.writerow([rank, name, score, renshu])
        print(rank, name, score, renshu)

f.close()
print('抓取完成，结果保存在 douban.csv')
