# author='scarlett'
# coding:utf-8
# 字典
alien_0 = {'color': 'green', 'points': 5}  # 键值对
print(alien_0['color'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25  # 添加键值对
change = {'color': 'yellow'}  # 小狗崽改的它喜欢的颜色
alien_0.update(change)
print(alien_0)
alien_0['speed'] = 'medium'
print('original x_position: ' + str(alien_0['x_position']))
