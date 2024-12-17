import json
import os

import jsonpath


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
import parsel
import requests,re
if not os.path.exists('./yinyue'):
    os.mkdir('./yinyue')
url = 'https://www.kugou.com/yy/html/rank.html'

headers = {
    "sec-ch-ua-platform": "Windows",
    "sec-ch-ua": "Chromium",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
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
    Hash_list = re.findall('"Hash":"(.*?)"',a.text)
    id_list= re.findall('"album_id":(.*?),',a.text)
    print(Hash_list)
    print(id_list)
    hash_id_list = zip(Hash_list,id_list)
    return hash_id_list

def xiazaigequ(hashs,album_id):
    new_url = f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={hashs}&dfid=1bnN3n3oSM4o0ndMFL0DiJlm&appid=1014&mid=3802bc9763ed46f1e83b944b4a4eca6d&platid=4&album_id={album_id}&_=1668837151152'
    # new_url = "https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1733926718133&mid=8afe2d8d979e1e492a2a1a43de277b42&uuid=8afe2d8d979e1e492a2a1a43de277b42&dfid=1JbfuJ3qIkQU36gESd2cjNwK&appid=1014&platid=4&encode_album_audio_id=blbhh495&token=&userid=0&signature=1f6c8abc631cec4717b54fa428dcc4a5"
    a = requests.get(url=new_url,headers=headers)
    play_backup_url = get_response_text(a.text,'play_backup_url')
    audio_name = get_response_text(a.text, 'audio_name')
    list_name = [audio_name,play_backup_url]
    return list_name

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
    mains()
    # html_url()
    # gequ("https://www.kugou.com/yy/rank/home/1-6666.html?from=rank")





