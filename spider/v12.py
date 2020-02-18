from urllib import request

if __name__ == '__main__':
    url = "http://www.renren.com/486004051/profile"

    headers = {
        "Cookie" : "anonymid=k6k9bp43jmtwi0; depovince=GW; jebecookies=1c1a5490-b1de-481b-b90d-f37c5442d3ba|||||; _r01_=1; ick_login=faae4aad-e80e-4cef-b835-d3d890fae366; taihe_bi_sdk_uid=ddd5f49fc2b1e9915996af4718fe91af; taihe_bi_sdk_session=9da2b5690d1545e8c669e3f1aa1111db; _de=5D013324EA74570F0F19516F0C7507CF; p=10950e1341489854e53adef07263f4c61; first_login_flag=1; ln_uact=18855584656; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20131027/1820/h_main_IJo9_c51300001523111a.jpg; t=2685f1a5b1706204394490f0da5915be1; societyguester=2685f1a5b1706204394490f0da5915be1; id=486004051; xnsid=c324329f; ver=7.0; loginfrom=null; JSESSIONID=abc3oWLLTVAg2_9Y828ax; jebe_key=e08e0518-14cc-41dc-ae99-f7226ea6ec73%7C3eac524597dd002934b8e46122df5d81%7C1581569004149%7C1%7C1581569003843; jebe_key=e08e0518-14cc-41dc-ae99-f7226ea6ec73%7C3eac524597dd002934b8e46122df5d81%7C1581569004149%7C1%7C1581569003845; wp_fold=0"
    }

    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    with open("rsp.html", "w") as f:
        f.write(html)

