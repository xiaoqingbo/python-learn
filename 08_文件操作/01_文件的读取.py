"""
演示对文件的读取
"""

# 打开文件
import time

f = open("D:/word.txt", "r", encoding="UTF-8")
# 读取文件 - read()

# print(f.read())
# print(type(f.read()))
# print(f"read方法读取全部内容的结果是：{f.read()}")
#print("-----------------------------------------------")
# 读取文件 - readLines()
# lines = f.readlines()   # 读取文件的全部行，封装到列表中
# # print(f"lines对象的类型：{type(lines)}")
# print(lines)
# print(type(lines))

# 读取文件 - readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")
# print(type(line1))
# print(f"第二行数据是：{line2}")
# print(type(line2))
# print(f"第三行数据是：{line3}")
# print(type(line3))

# for循环读取文件行
# for line in f:
#     print(f"每一行数据是:{line}")
# # 文件的关闭
# f.close()
# time.sleep(500000)
# with open 语法操作文件
with open("D:/word.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")

