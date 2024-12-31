import os,time
from lxml import etree
from requests.adapters import HTTPAdapter
if not os.path.exists('../meitu'):
    os.mkdir('../meitu')

def tupian():
    from pip._vendor import requests, urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    res = requests.Session()
    res.mount('https://', HTTPAdapter(max_retries=5))
    res.keep_alive = False
    headers = {
        "sec-ch-ua-platform":"Windows",
        "sec-ch-ua": "Chromium",
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    url = 'https://pic.netbian.com/4kmeinv/index_%d.html'
    for i in range(6,9):
        new_url = format(url%i)
        responses = requests.get(url=new_url,headers=headers)
        responses.encoding = 'GBK'
        paga_text = responses.text
        tree = etree.HTML(paga_text)
        li_list = tree.xpath('//div[@class="slist"]/ul/li')
        for li in li_list:
            li_src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
            li_name = li.xpath('./a/b/text()')[0] + ".jpg"
            time.sleep(1)
            li_data = res.get(url=li_src,headers=headers).content
            with open('../meitu/'+li_name,mode='wb') as fp:
                fp.write(li_data)
                print(li_name,'图片下载成功！！！')




tupian()