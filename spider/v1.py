from urllib import request
'''
使用urllib.request请求一个网页内容，并把内容打印出来
'''

if __name__ == '__main__':
    url = "http://s.yingjiesheng.com/search.php?word=%E7%BB%99%E6%8E%92%E6%B0%B4&area=0&jobterm=0&do=1&stype=0"
    # 打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)
    # 把返回结果读取出来
    # 读取出来内容类型为bytes
    html = rsp.read()
    print(type(html))
    # 如果想把bytes内容转换成字符串，需要解码
    html = html.decode()
    print(html)
