# author='scarlett'
# coding:utf-8
# 操作列表
# 循环列表
magicians = ['alice', 'dick', 'piggy']
for magician in magicians:
    print(magician)
    print(magician.title() + ' is cute')
print('first part is easy')
# 创建数值列表
for value in range(1, 5):
    print(value)  # 创建数值，从指定的第一个数值到指定的第二个值为止，不含第二个值
numbers = list(range(1,6))  # 函数list将range转化为列表
print(numbers)
event_numbers =list( range(3, 22, 2))  # 指定步长，从3开始不断加2
print(event_numbers)
squares = [value**2 for value in range(1,5)]  # 计算1-4的平方
print(squares)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))  # 最小，最大，求和
# 列表切片
players = ['ss', 'dd', 'ff', 'gg', 'hh']
print(players[0:3])  # 输出0，1，2前三个元素，终止在3之前
print(players[:3])  # 输出自列表头开始
print(players[1:])  # 输出至列表末尾
print(players[:])  # 输出全表
print(players[-3:])
for player in players[:3]:  # 遍历切片
    print(player.title())
# 复制列表
my_foods = ['pizza', 'falafel', 'chocalate', 'coco']
friend_foods = my_foods[:]
print(friend_foods)  # 从原列表中提取一个切片创建这个列表的副本，将副本存储到新变量中
my_foods.append('cannoli')
friend_foods.append('cream')
print(my_foods)
print(friend_foods)  # 注意使用切片复制列表和直接将原变量赋值给新变量的区别：变量指向同一个列表
# 元组：不可变的列表
dimensions = (200,50)  # 元组实质是个列表，元素不可变的，要修改只能重新给变量赋值
print(dimensions[0])
for dimension in dimensions:
    print(dimension)
"b"