# author='scarlett'
# coding:utf-8
message = 'hello world'
print(message)
name = 'Scarlett lovepower'
print(name.title())  # 句点"." 符号让python对name执行方法title()指定的操作，方法是可对数据执行的操作
print(name.upper())  # 全部大写
print(name.lower())  # 全部小写
first_name = 'chen'
last_name = 'weiwei'
full_name = first_name + ' ' + last_name  # ' '表示姓名中间空格
print(full_name)
print('hello,' + full_name.title() + '!')
print('\tpython')  # \t制表符
print('languages:\npython\nC\njavascript')  # \n换行符
favorite_language = 'python '
favorite_language = favorite_language.rstrip()  # rstrip（）删除字符串末尾空白 .1strip（）删除开头空白.strip()删除两端空白
print(favorite_language)
age = 23
message = "happy " + str(age) + "rd birthday"  # str()表示是23而不是2+3
print(message)
