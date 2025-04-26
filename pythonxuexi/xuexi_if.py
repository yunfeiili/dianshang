
cars = ["audi","bme","python","java","c++"]

# for car in cars:
#     if car == "python":
#
#         print(car.upper())
#
#     else:
#
#         print(car.title())

# for car in cars:
#
#     if car.upper() == "JAVA":
#
#         print("这就是我要找发数据")
#         break
#
#     else:
#
#         print(f"这个数据就是: {car}")


# for i in range(1,4):
#     name = input("请输入名称: ")
#     pwp = int(input("请输入密码: "))
#
#     if name == "andmi" and pwp == 123456:
#
#         print("登录成功！！！！")
#
#         break
#     else:
#         print(f"密码或者账号错误，请重新登录~~~\n您剩余登录次数{3-i}")


# age = 12

def ceshi(age):

    if age <= 10:
        print("这还是一个小孩子")
    elif 10 <  age <= 30 :
        print("这还是一个青年")
    elif 30 < age <= 40:
        print("这还是一个中年")
    elif 40 < age <= 60:
        print("这还是一个老年人")
    elif 60 < age <= 100:
        print("这还是一个长寿的人")
    elif age > 100:
        print("这还是一个百岁老人")
