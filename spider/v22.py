'''
使用参数headers和parmas
研究返回结果
'''

import requests

# 完整访问url是下面url加上参数构成
url = "http://www.baidu.com"
kw = {
    "wd": "王八蛋"
}

headers = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"
}
rsp = requests.get(url, params=kw, headers=headers)

print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code) # 请求返回码