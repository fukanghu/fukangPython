'''
v2
处理js加密代码
'''
# 通过查找，能找到js代码中操作代码
'''
1. 这个是计算salt的公式，salt: i
r = "" + (new Date).getTime(),
        i = r + parseInt(10 * Math.random(), 10);
        
2. sign:n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
md一共需要四个参数，第一个和第四个都是固定值的字符串，第三个时所谓的salt，第二个参数就是输入的要查找的单词

'''

def getSalt():

    '''
    salt公式 r = "" + (new Date).getTime(),
        i = r + parseInt(10 * Math.random(), 10);
    把它翻译成python代码
    :return:
    '''
    import time, random

    salt = int(time.time()*1000) + random.randint(0,10)

    return salt

def getMD5(v):
    import hashlib
    md5 = hashlib.md5()
    # update需要bytes格式
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()
    return sign

def getSign(key, salt):
    sign = 'n.md5("fanyideskweb" + key + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj")'
    sign = getMD5(sign)
    return sign

from urllib import request, parse

def youdao(key):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    salt = getSalt()

    data = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": str(salt),
    "sign": getSign(key, salt),
    "ts": "1581999855611",
    "bv": "29c69ec4c3365ab92a0a2e28f719395f",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME"
    }
    print(data)
    # 参数data需要时bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application/json, text/javascript, */*; q = 0.01",
        "Accept - Encoding": "gzip, deflate",
        "Accept - Language": "en-US, en; q = 0.9, zh-CN; q = 0.8, zh; q = 0.7",
        "Connection": "keep-alive",
        "Content - Length": len(data),
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
