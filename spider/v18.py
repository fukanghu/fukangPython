'''
破解有道词典
v1
'''

from urllib import request, parse

def youdao(key):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {
    "i": "china i love you",
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "15819998556118",
    "sign": "64584ed9018041caecff2c0a0b1f5a8e",
    "ts": "1581999855611",
    "bv": "29c69ec4c3365ab92a0a2e28f719395f",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME"
    }
    # 参数data需要时bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application/json, text/javascript, */*; q = 0.01",
        "Accept - Encoding": "gzip, deflate",
        "Accept - Language": "en-US, en; q = 0.9, zh-CN; q = 0.8, zh; q = 0.7",
        "Connection": "keep-alive",
        "Content - Length": "240",
        "Content - Type": "application/x-www-form-urlencoded; charset = UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO = 453585145.93648994; OUTFOX_SEARCH_USER_ID = 1622357258@10.169.0.82; _ga = GA1.2.1702190112.1581086619; JSESSIONID = aaaKRInxSdYf39JRiIwbx; ___rl__test__cookies = 1581999855609",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User - Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",
        "X - Requested - With": "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("china i love you")
