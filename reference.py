#filename:reference.py
shoplist=['apple','mango','carrot','banana']
mylist=shoplist
del shoplist[0]

print(shoplist)
print(mylist)

#slice

mylist=shoplist[:]
del mylist[0]#删第一项
print(shoplist)
print(mylist)
