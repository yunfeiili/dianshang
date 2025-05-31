import csv

from faker import Faker

fake = Faker("zh_CN")
# print(fake.name())  # 随机生成一个名字
# print(fake.address())  # 随机生成一个地址
# print(fake.email())  # 随机生成一个邮箱
#
# print(fake.unique.name())
# print(fake.texts())
# print(fake.md5())

def userss():
    f = open('../data/users.csv', mode='w', encoding='utf-8', newline='')
    csv_w = csv.DictWriter(f,fieldnames=[
                '姓名',
                '邮箱',
                '电话',
                '身份证',
                '职位',
                '家庭住址',
                '用户id',
                '信用卡号',
    ])
    csv_w.writeheader()


    for i in range(100):
        dic_1 = {
            "姓名": fake.unique.name(),
            "邮箱": fake.unique.email(),
            "电话": fake.unique.phone_number(),
            "身份证": fake.unique.ssn(),
            "家庭住址": fake.unique.address(),
            "用户id": fake.unique.uuid4(),
            "职位": fake.unique.job(),
            "信用卡号":fake.unique.credit_card_number(),

        }
        csv_w.writerow(dic_1)
# print(dic_1)
userss()
import json
import random
import string

import jsonpath
from faker import Faker


faker = Faker('zh_CN')
'''
zh_CN（简体中文）、zh_TW（繁体中文）、zh_TW（台湾）、en_US（美国英文）、en_GB（英国英文）、de_DE（德文）、ja_JP（日文）、ko_KR（韩文）、fr_FR（法文）
'''
def get_random():
    """生成一串6位数的字符+数组混合的字符串"""
    number = string.ascii_letters + string.digits
    number_n = ''.join(random.sample(number, 6))
    return number_n



def create_string_number(n=9):
    """生成一串指定位数的字符+数组混合的字符串"""
    m = random.randint(1, n)
    a = "".join([str(random.randint(0, 9)) for _ in range(m)])
    b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
    return ''.join(random.sample(list(a + b), n))

def rand_str():
    ''' 随机生成1000000到2000000数据 '''
    return str(random.randint(1000000, 2000000))

def  numbers():
    '''生成随机的电话号码 '''
    q = [134,133,135,136,137,138,139,150,151,152,157,158,159,182,183,
    184,187,188,147,178,130,131,132,155,156,145,185,186,176,175,
    133,153,180,181,189,177,173,149]
    e = random.choice(q)
    w = int(''.join(random.sample(string.digits,8)))
    return '{}{}'.format(e,w)



def get_name():
    '''
    :return: 随机生成一个中文名称
    '''
    return faker.name()

def get_email():
    '''

    :return: 随机获取电子邮箱
    '''
    return faker.email()

def get_text():
    '''

    :return: 随机获取一段文本
    '''
    return faker.text()


def get_phone():
    '''
    :return: 返回随机的手机号
    '''
    return faker.phone_number()


    # 获取指定内容
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


