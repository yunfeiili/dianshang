

#字符串的大小写

str_1 = "Then is a string"

print("原始的数据: " + str_1)

# 字符串之小写
print("字符串之小写: " + str_1.lower())

# 字符串大写
print("字符串大写: " + str_1.upper())

# 字符串每个单词开头大写
print("字符串每个单词开头大写: " + str_1.title())


# 字符串格式话操作

name = '小明'
age = 18
print(f"{name}今年{age}岁。")
print("我的儿子叫{}，他今年已经{}岁了，已经成年了".format(name,age))


# 制表符进行换行处理

str_2 = "python\njava\nC++\nphp"
print("换行处理:\n" + str_2)

# 删除空白

str_3 = " Then is a string "

# 删除右边结尾的空白
print(str_3.rstrip())

# 删除左边开始的空白
print(str_3.lstrip())

# 以空格进行分割，输出列表
print(str_3.split())

# 以指定字符进行分割，输出列表
print(str_3.split("a"))


http = "https://www.baidu.com/index.htm"

# print(http.removeprefix("https"))

# 判断以什么开头
print(http.startswith("http"))

# 判断以什么开头
print(http.endswith("m"))

# 字符串的替换,替换所以相同的字符
print(http.replace("www","http"))

# 遍历字符串中的每个字符
for i in http:
    print(i)


str_4 = "JJJJJjjjjGHYGSHGFSGFAJLSGFGFUAGFUEUFAUIEHFUIAEGFEHj"
dict_1 = {

}
str_4 = str_4.lower()
for i in str_4:
    dict_1[i] = str_4.count(i)

for k , v in dict_1.items():
    print("当前的key是: {}, 总共出现的次数是: {}".format(k,v))

print(dict_1)

