# author='scarlett'
# coding:utf-8
# 列表简介.访问列表元素
names = ['scarlett', 'victor', 'weiwei', 'piggy']
print(names)
print(names[0].title())
print(names[-1].title())
message = 'my favorite little pig is ' + names[1].title()
print(message)
# 修改添加元素
names[-1] = 'doggy'  # 修改列表元素
print(names)
names.append('red')  # 在列表末尾添加元素
names.insert(0, 'lovelywife')  # 在指定位置插入元素
names.insert(2, 'cutehusband')
print(names)
popped_names = names.pop(3)  # 弹出指定位置元素，原列表无，可弹出使用
print(popped_names)
del names[-1]  # 删除元素
names.remove('doggy')  # 根据值删除元素
print(names)
# 组织列表
cars = ['bmw', 'aodi', 'subara', 'toyota']
print(sorted(cars))  # sorted是按字母排序同时原列表不变
cars.reverse()  # 方法reverse（）反转列表元素
print(cars)
# 确定列表长度
print(len(cars))  # 注意区分函数和方法，函数可以直接在print内，方法不行

