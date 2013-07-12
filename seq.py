#filename:seq.py
shoplist=['apple','mango','carrot','banana']
#
print('item 0 is',shoplist[0])
print('item 1 is',shoplist[1])
print('item 2 is',shoplist[2])
print('item 3 is',shoplist[3])
print('item -1 is',shoplist[-1])
print('item -2 is',shoplist[-2])

#slicing on a list
print('item 1 to 3 is',shoplist[1:3])
print('item 2 to end is',shoplist[2:])
print('item 1 to -1 is',shoplist[1:-1])
print('item start to end is ',shoplist[:])

#slicing on string
name="lishixi"
print("1 to 3 is ",name[1:3])
print("2 to end is",name[2:])
print("1 to -1 is ",name[1:-1])
print("start to end is",name[:])

