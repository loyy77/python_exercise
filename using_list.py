#filename:using_list.py
#this is my shopping list

shoplist=['apple','mango','carrot','banana']
print('i have',len(shoplist),'个水果')
print('这些水果是：')
for item in shoplist:
    print(item),

print('\n我又买了rice')
shoplist.append('rice')
print('现在我的购物列表是：',shoplist)
print('我要排序我的列表：')
shoplist.sort()
print('排序后的列表',shoplist)

print('我买的第一个物品是：',shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print('我买了',olditem)
print('我现在的购物列表是:',shoplist)

