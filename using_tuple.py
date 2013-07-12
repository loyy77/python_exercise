#filename:using_tuple.py
zoo=('狼','大象','企鹅','猴子')
print('动物园的动物数量是：',len(zoo))

new_zoo=('猩猩','老虎','蟒蛇',zoo)
print('新动物园的动物数：',len(new_zoo))
print('这些动物是：',new_zoo)
print('从老动物园带来了动物：',new_zoo[3])
print('从老动物园带来的最后一个动物是',new_zoo[3][3])
