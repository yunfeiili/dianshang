import json
import os
import parsel
import requests,re,time
import jsonpath,hashlib


def get_response_text(res,key):
    '''
    获取文本中指定的内容
    :param res: 文本
    :param key: 取对应的value值
    :return:
    '''
    try:
        text = json.loads(res)
        value = jsonpath.jsonpath(text,'$..{}'.format(key))
        if value:
            if len(value) == 1:
                return value[0]
            return value
        return value
    except:
        return None

if not os.path.exists('./yinyue'):
    os.mkdir('./yinyue')
url = 'https://www.kugou.com/yy/html/rank.html'

headers = {
    "sec-ch-ua-platform": "Windows",
    "sec-ch-ua": "Chromium",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

def html_url():
    res = requests.get(url=url,headers=headers)
    select = parsel.Selector(res.text)
    titles = select.css('.pc_rank_sidebar ul a ::attr(title)').getall()
    hrefs = select.css('.pc_rank_sidebar ul a ::attr(href)').getall()
    list_hr_ti = zip(titles,hrefs)
    return list_hr_ti

def gequ(href):
    a = requests.get(url=href,headers=headers)
    audioid_list = re.findall('data-eid="(.*?)">', a.text)
    print(audioid_list)
    return audioid_list

def md5jiami(miao,haomiao):
    s = ['NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt',
         'appid=1014',
         f"clienttime={miao}",
         'clientver=1000',
         'dfid=1JbfuJ3qIkQU36gESd2cjNwK',
         'mid=8afe2d8d979e1e492a2a1a43de277b42',
         'srcappid=2919',
         f'uuid={haomiao}',
         '{"userid":"0","plat":103,"m_type":0,"vip_type":0,"own_ads":{}}',
         'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt']
    string = "".join(s)
    MD5 = hashlib.md5()
    MD5.update(string.encode("utf-8"))
    sign = MD5.hexdigest()
    return sign

def xiazaigequ():

    # t = time.time()
    # miao = int(t)
    # haomiao = int(round(t * 1000))
    new_url = "https://wwwapi.kugou.com/play/songinfo"
    data = {
            "srcappid": "2919",
            "clientver": "20000",
            "clienttime": "1735402905287",
            "mid": "8afe2d8d979e1e492a2a1a43de277b42",
            "uuid": "8afe2d8d979e1e492a2a1a43de277b42",
            "dfid": "1JbfuJ3qIkQU36gESd2cjNwK",
            "appid": "1014",
            "platid": "4",
            "encode_album_audio_id": "bm9x7j72",
            "token": "",
            "userid": "0",
            "signature": "801a38e9a3c1af35bb880af59e609904"
        }


    a = requests.get(url=new_url,headers=headers,params= data)
    print(a.url)
    play_backup_url = get_response_text(a.text,'play_backup_url')
    audio_name = get_response_text(a.text, 'audio_name')
    list_name = [audio_name,play_backup_url]
    print(list_name)
    # return list_name

def save(audio_name,play_backup_url):
    try:
        music = requests.get(url=play_backup_url,headers=headers).content
        with open('../yinyue/' + audio_name +'.mp3',mode='wb') as f:
            f.write(music)
            print(audio_name,'保存成功！！！')
    except Exception as e:
        print(e)
        print('没保存成功的歌曲名称是：',audio_name)

def mains():
    hrefs_url = html_url()
    for name,href_url in hrefs_url:
        print(f'=================正在爬取{name}的歌曲==============')
        hash_id_list = gequ(href_url)
        for hash,ids in hash_id_list:
            list_name = xiazaigequ(hash,ids)
            save(list_name[0] ,list_name[1])

if __name__ == '__main__':
    # html_url()
    # id_list = gequ("https://www.kugou.com/yy/rank/home/1-6666.html?from=rank")
    # for i in id_list:
    #     xiazaigequ(i)

    # xiazaigequ()
    print(md5jiami(1735440849,1735440849481))
    # t = time.time()
    miao = int(time.time())
    haomiao = int(round(time.time() * 1000))
    print(miao)
    print(haomiao)
    1735440849
    1735440849481



