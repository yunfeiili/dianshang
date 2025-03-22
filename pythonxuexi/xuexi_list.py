
list_1 = ["python",'java','C++',"PHP",'java']

# 遍历列表每一个元素
# for v in list_1:
#     print(v)

# 使列表中元素进行倒序展示
print(list_1[::-1])
list_1.reverse()
print(list_1)

# 列表进行切片,取头不取尾。列表索引从0开始
print(list_1[1:3])

print(list_1[0:3:2])# 步长为2进行切片

# 添加元素
list_1.append("C#")
print(list_1)


# 指定位置添加元素
list_1.insert(1,"测试")
print(list_1)

# 统计列列表中元素出现的次数
print(list_1.count("java"))


# 删除指定元素
list_1.remove("python")
print(list_1)
del list_1[2] # 根据索引删除对于的元素
print(list_1)

# 删除列表最后一个元素，并返回该元素数值
print(list_1.pop())


# 将list_2的数据添加到list_1中
list_2 = [1,2,3,4,5]
list_1.extend(list_2)
# list_2.extend(list_1)
print(list_1)
print(list_2)

# 列表指定位置添加元素
list_2[1] = "ceshi"
print(list_2)
list_2[0] = ["a","b"]
print(list_2)



list_3 = [5,2,3,9,6,11,34]
# 列表进行永久排序,reverse=True降序
list_3.sort(reverse=True)
print(list_3)

# 列表进行临时排序，reverse=False时升序
print(sorted(list_3,reverse=False))


