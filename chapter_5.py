# author='lwz'
# coding:utf-8
# if语句
car = 'bmw'
car == 'bmw'  # 两个=判断是否相等，相等运算符
requested_topping = 'mushrooms'
if requested_topping != 'chocalate':  # :非常容易掉落，!=表示不等
    print('hold the food')
age = 12
if age < 4:
    print('your cost is 0')
elif age < 18:
    print('your cost is 5')
elif age < 65:
    print('your cost is 8')
else:
    print('your cost is 10')  # if-elif-else中条件测试通过将跳过余下测试
# 可以省略else
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 8
elif age >=65:
    price = 5
print('your cost is ' + str(price) + '.')
