

import jsonpath
import hashlib
import os
import time
import json


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

import requests,re
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


def MD5_sign_search(timestamp, music_name):
    """
    通过音乐id解密搜索页的signature参数
    :param timestamp:时间戳
    :param music_name:搜索框音乐名（例如:把回忆拼好给你)
    :return:加密后32位md5参数(例如:72181cc6baf76ee0404837d5d657dd5c)
    """
    signature_list = ['NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt',
                      'appid=1014',
                      'bitrate=0',
                      'callback=callback123',
                      f'clienttime={timestamp}',
                      'clientver=1000',
                      'dfid=3MmrUf3e5zpy3cStkN3Bn9oS',
                      'filter=10',
                      'inputtype=0',
                      'iscorrection=1',
                      'isfuzzy=0',
                      f'keyword={music_name}',
                      'mid=c4de83c1ebb2e73fc5ae95304a674918',
                      'page=1',
                      'pagesize=30',
                      'platform=WebFilter',
                      'privilege_filter=0',
                      'srcappid=2919',
                      'token=483ef68936faa09268f3a42f7ab7ee31b584a3f155828a100c95fadf7c5ddd1e',
                      'userid=2078452878',
                      'uuid=c4de83c1ebb2e73fc5ae95304a674918',
                      'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt']
    string = "".join(signature_list)
    MD5 = hashlib.md5()
    MD5.update(string.encode('utf-8'))
    sign_lis = MD5.hexdigest()  # md5 32位加密内容
    return sign_lis


def fetch_url(audio_id):
    """
    通过音乐ID爬取当前音乐的md3地址
    :param audio_id: 音乐ID(72jrv7fa)
    :return:音乐url(........mp3)
    """
    timestamp = int(time.time() * 1000)
    print('audio_id:', audio_id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }
    sign = MD5_sign(timestamp, audio_id)
    datas = {
        'srcappid': '2919',
        'clientver': '20000',
        'clienttime': timestamp,
        'mid': 'c4de83c1ebb2e73fc5ae95304a674918',
        'uuid': 'c4de83c1ebb2e73fc5ae95304a674918',
        'dfid': '3MmrUf3e5zpy3cStkN3Bn9oS',
        'appid': '1014',
        'platid': '4',
        'encode_album_audio_id': audio_id,
        'token': '483ef68936faa09268f3a42f7ab7ee31b584a3f155828a100c95fadf7c5ddd1e',
        'userid': '2078452878',
        'signature': sign,
    }
    response = requests.get(url='https://wwwapi.kugou.com/play/songinfo?', headers=headers, params=datas)
    jsurl = response.json()
    # print('jsurl: ', jsurl)
    play_url = jsurl['data']['play_url']
    return play_url


def audio_id_list(music_name):
    """
    通过搜索栏参数(音乐名)获取 搜索第一个的 音乐名 and ID
    :param music_name: 搜索栏参数(音乐名) 例如: 苏星婕 - 把回忆拼好给你
    :return: 音乐名  音乐ID(苏星婕 - 把回忆拼好给你   72jrv7fa)
    """
    timestamp = int(time.time() * 1000)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }
    sign = MD5_sign_search(timestamp, music_name)
    datas = {
        'callback': 'callback123',
        'srcappid': '2919',
        'clientver': '1000',
        'clienttime': timestamp,
        'mid': 'c4de83c1ebb2e73fc5ae95304a674918',
        'uuid': 'c4de83c1ebb2e73fc5ae95304a674918',
        'dfid': '3MmrUf3e5zpy3cStkN3Bn9oS',
        'keyword': music_name,
        'page': '1',
        'pagesize': '30',
        'bitrate': '0',
        'isfuzzy': '0',
        'inputtype': '0',
        'platform': 'WebFilter',
        'userid': '2078452878',
        'iscorrection': '1',
        'privilege_filter': '0',
        'filter': '10',
        'token': '483ef68936faa09268f3a42f7ab7ee31b584a3f155828a100c95fadf7c5ddd1e',
        'appid': '1014',
        'signature': sign,
    }
    response = requests.get(url='https://complexsearch.kugou.com/v2/search/song?', headers=headers, params=datas)
    callback_dict = re.findall('callback123\((.*)\)', response.text)[0]
    jsurl = json.loads(callback_dict)
    fileName = jsurl['data']['lists'][0]['FileName']
    eMixSongID = jsurl['data']['lists'][0]['EMixSongID']
    return fileName, eMixSongID


def download_url(file_name, url_mp3):
    """
    通过已经获取的mp3文件保存到文件夹中
    :param file_name: 音乐名
    :param url_mp3: 音乐url(.....mp3)
    :return: 无
    """
    response = requests.get(url_mp3)
    try:
        with open(f"./music_files/{file_name}.mp3", "wb") as f:
            f.write(response.content)
    except:
        with open(f"./music_files/{int(time.time() * 1000)}.mp3", "wb") as f:
            f.write(response.content)

    print(f'{file_name}-----下载成功')


def directory_create():
    """判断文件是否存在。不存在则创建改文件"""
    directory = "./music_files"
    if not os.path.exists(directory):
        os.makedirs(directory)


if __name__ == '__main__':
    directory_create()  # 判断music_flie文件是否存在

    music_name = '听说你'
    audio_id = audio_id_list(music_name)  # (苏星婕 - 把回忆拼好给你, 72jrv7fa)
    file_name = audio_id[0]  # 苏星婕 - 把回忆拼好给你
    emixsong_id = audio_id[1]  # 72jrv7fa
    time.sleep(2)
    url_mp3 = fetch_url(emixsong_id)  # 获取 ......mp3
    download_url(file_name, url_mp3)  # 下载保存




