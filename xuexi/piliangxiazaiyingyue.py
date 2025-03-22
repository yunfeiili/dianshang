import jsonpath
import hashlib
import os
import time
import json
import parsel
import requests,re


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

def yinyue_dir():
    if not os.path.exists('./yinyue'):
        os.mkdir('./yinyue')

url = 'https://www.kugou.com/yy/html/rank.html'

headers = {
    "sec-ch-ua-platform": "Windows",
    "sec-ch-ua": "Chromium",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

def MD5_sign(timestamp, audio_id):
    """
    通过音乐id解密详情页单个音乐的signature参数
    :param timestamp: 时间戳
    :param audio_id: 音乐id(例如:72jrv7fa)
    :return:
    """
    signature_list = ['NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt',
                      'appid=1014',
                      f'clienttime={timestamp}',
                      'clientver=20000',
                      'dfid=3MmrUf3e5zpy3cStkN3Bn9oS',
                      f'encode_album_audio_id={audio_id}',
                      'mid=c4de83c1ebb2e73fc5ae95304a674918',
                      'platid=4',
                      'srcappid=2919',
                      'token=483ef68936faa09268f3a42f7ab7ee31b584a3f155828a100c95fadf7c5ddd1e',
                      'userid=2078452878',
                      'uuid=c4de83c1ebb2e73fc5ae95304a674918',
                      'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt']
    string = "".join(signature_list)
    MD5 = hashlib.md5()
    MD5.update(string.encode('utf-8'))
    sign = MD5.hexdigest()  # md5 32位加密内容
    return sign


def html_url():
    res = requests.get(url=url,headers=headers)
    select = parsel.Selector(res.text)
    titles = select.css('.pc_rank_sidebar ul a ::attr(title)').getall()
    hrefs = select.css('.pc_rank_sidebar ul a ::attr(href)').getall()
    list_hr_ti = zip(titles,hrefs)
    return list_hr_ti

def gequ(href):
    a = requests.get(url=href,headers=headers)
    album_id = re.findall('data-eid="(.*?)">', a.text)
    return album_id

def xiazaigequ(album_id):

    new_url = "https://wwwapi.kugou.com/play/songinfo?"
    timestamp = int(time.time() * 1000)
    sign = MD5_sign(timestamp, album_id)
    datas = {
        'srcappid': '2919',
        'clientver': '20000',
        'clienttime': timestamp,
        'mid': 'c4de83c1ebb2e73fc5ae95304a674918',
        'uuid': 'c4de83c1ebb2e73fc5ae95304a674918',
        'dfid': '3MmrUf3e5zpy3cStkN3Bn9oS',
        'appid': '1014',
        'platid': '4',
        'encode_album_audio_id': album_id,
        'token': '483ef68936faa09268f3a42f7ab7ee31b584a3f155828a100c95fadf7c5ddd1e',
        'userid': '2078452878',
        'signature': sign,

    }
    a = requests.get(url=new_url,headers=headers,params=datas)
    # print(a.text)
    play_backup_url = get_response_text(a.text,'play_backup_url')
    audio_name = get_response_text(a.text, 'audio_name')
    list_name = [audio_name,play_backup_url]
    # print(list_name)
    return list_name

def save(audio_name,play_backup_url):
    try:
        yinyue_dir()
        music = requests.get(url=play_backup_url,headers=headers).content
        with open('./yinyue/' + audio_name +'.mp3',mode='wb') as f:
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
        for ids in hash_id_list:
            list_name = xiazaigequ(ids)
            save(list_name[0] ,list_name[1])

if __name__ == '__main__':
   #酷狗飙升榜 https://www.kugou.com/yy/rank/home/1-6666.html?from=rank
   # gequ("https://www.kugou.com/yy/rank/home/1-6666.html?from=rank")
   # xiazaigequ("bposqx9d")
   mains()