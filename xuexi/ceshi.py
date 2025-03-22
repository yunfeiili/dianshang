import pytest


# class TestDome:
#
#     def test_01(self):
#         print('----测试用例：test_01------')
#
#     def test_02(self):
#         print('----测试用例：test_02------')
#
#     def setup_method(self):
#         print("测试执行前的数据")
#     # def setup_method(function):
#     #     print("测试用例前置方法---setup_method---")
#
#     def teardown_method(self):
#         print("测试用例后置方法---teardown_method---")
#
#
#     def setup_class(self):
#         print("testdome类执行前准备的数据")
#
#
#
#     def teardown_class(self):
#         print("testdome类执行后删除的数据")
import openai

# 设置OpenAI API密钥
# api_key1="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"

# openai.api_key = api_key1
#
#
# def generate_technical_article(topic, max_tokens=1500):
#     prompt = f"Write a detailed technical article on: {topic}"
#
#     # 调用OpenAI API生成文章
#     response = openai.Completion.create(
#     engine = "gpt-4o-mini",
#     prompt = prompt,
#     max_tokens = max_tokens,
#     temperature = 0.7
#
# )
#
#     return response.choices[0].text.strip()
#
# # 测试生成文章
# if __name__ == "__main__":
#     topic = "AI-based image recognition techniques"
#     article = generate_technical_article(topic)
#     print("生成的文章:\n", article)

import requests,os
import parsel,csv

f = open('../房源.csv', mode='w', encoding='utf-8', newline='')
csv_w = csv.DictWriter(f,fieldnames=[
            '房子的名称',
            '房间的格局',
            '房间大小',
            '那年建造的',
            '房间总价格',
            '房子的位置',
            '具体位置',
            '单价元/㎡'
])
csv_w.writeheader()
url = 'https://changde.anjuke.com/sale/?pi=baidu-cpc-wh-ty1-pt&kwid=193207228578&bd_vid=11555949436292524859'
# url = 'https://wuhan.anjuke.com/sale/p3/'
headers = {
    "sec-ch-ua-platform": "Windows",
    "sec-ch-ua": "Chromium",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

res = requests.get(url=url,headers= headers)
print(res.text)
select = parsel.Selector(res.text)
div_list = select.css('.list-main[data-v-0bbbe4ac]')
for div in div_list:
    div_name = div.css('.property-content-title-name[data-v-dc4ef438]::text').get()  # 房子的名称
    div_fang = ''.join(div.css('.property-content-info-attribute span[data-v-dc4ef438]::text').getall())  # 房间的格局
    div_nian = ''.join(div.css('.property-content-info-text[data-v-dc4ef438]::text').getall()[8:9]).lstrip()  #那年建造的
    div_qian = div.css('.property-price-total-num[data-v-dc4ef438]::text').get() + '万'   # 房间总价格
    div_dizi = div.css('.property-content-info-comm-name[data-v-dc4ef438]::text').get()   # 房子的位置
    div_di = div.css('.property-price-average[data-v-dc4ef438]::text').get()  # 单价元/㎡
    div_daxiao = div.css('.property-content-info-attribute span[data-v-dc4ef438]::text').getall()[5].lstrip()  #房间大小
    div_juti = ''.join(div.css('.property-content-info-comm-address[data-v-dc4ef438] ::text').getall())
    dic_1= {
            '房子的名称':div_name,
            '房间的格局':div_fang,
            '房间大小': div_daxiao,
            '那年建造的':div_nian,
            '房间总价格':div_qian,
            '房子的位置':div_dizi,
            '具体位置': div_juti,
            '单价元/㎡':div_di,
    }
    csv_w.writerow(dic_1)
    print(dic_1)



