'''
爬取豆瓣电影数据
了解ajax的基本爬取方式
'''
from urllib import request
import json
url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=40&genres=%E5%96%9C%E5%89%A7"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Connection": "keep-alive",
    "Cookie": "bid=74V0yuo2zLA; douban-fav-remind=1; __gads=ID=fd4cd7aeca3c7436:T=1581391275:S=ALNI_MYd4wdWoYCYc1le78es0NQSkqHDCg; ll='108296'; __yadk_uid=1IQH5VvgzvtFREH8EoRG82PtB0p9yRVG; __utmz=30149280.1582023863.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1582023863.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1582036648%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DoSP4M_3qE_MF-7O2msy_i0d3FC2Ga9ngT6pdtQH2co04-IrEIhbGL3fLITCLZ0oJ%26wd%3D%26eqid%3Df22106e00001a427000000045e4bc4af%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1163171358.1581391166.1582023863.1582036649.7; __utmb=30149280.0.10.1582036649; __utmc=30149280; __utma=223695111.1131661719.1582014237.1582023863.1582036649.3; __utmb=223695111.0.10.1582036649; __utmc=223695111; ap_v=0,6.0; _pk_id.100001.4cf6=b57a1bb1519f8ab1.1582014237.3.1582036727.1582023910.",
    "Host": "movie.douban.com",
    "Referer": "https://movie.douban.com/tag/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"
}
rsp = request.urlopen(url)

data = rsp.read().decode()

data = json.loads(data)

print(data)

