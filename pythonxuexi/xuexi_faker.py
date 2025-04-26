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
class ceshishuju():


    pass

