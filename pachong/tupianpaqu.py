from pip._vendor import  urllib3
from lxml import etree
import requests


from PIL import Image
import os

def getfiles(input_path):
    path_list = []
    filenames = os.listdir(input_path)
    for filename in filenames:
        a = os.path.join(input_path, filename)
        img = Image.open(a)
        new_img = img.resize((375, 500))
        new_img.save(filename)
        path_list.append(a)
    return path_list


if __name__ == '__main__':
    url = 'https://www.vcg.com/creative-image/xigua/'
    url1 = "https://www.vcg.com/creative-photo/?orientType%5B0%5D=4"

    header = {
            'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


    response = requests.get(url=url, headers=header)
    response.encoding = 'utf-8'
    page_text = response.text
    tree = etree.HTML(page_text)
    figure_list = tree.xpath('//div[@class="gallery_inner"]/figure')
    if not os.path.exists('./piclitl'):
        os.makedirs('./piclitl')
    for figure in figure_list:
        try:
            img_src = figure.xpath('./a/img/@data-src')[0]
            img_src = 'https:' + img_src
            img_name = img_src.split('/')[-1]
        except(IndexError):
            print('未成功匹配到字段')
        try:
            img_data = requests.get(url=img_src, headers=header).content
        except(requests.exceptions.InvalidURL):
            print('没有访问地址')
        img_path = 'piclitl/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功')










