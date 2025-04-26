dict_1 = {
    "name":"张三",
    "age":23,
    "xinbie":"男"
}

# 获取字典中对应的值

# print(dict_1["name"])
# print(dict_1.get("age",77))
# print(dict_1.get("chengji",90))

# 在字典添加元素
dict_1["sos"] = "ios"

print(dict_1)

# 修改字典中的值
dict_1["name"] = "李四"

# for k , v in dict_1.items():
#     print(k,v)
#
#
# for k in dict_1.keys():
#     print(k)
#
#
# for v in dict_1.values():
#     print(v)

# 删除自动的值
del dict_1["name"]
print(dict_1)
