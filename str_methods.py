#filename:str_methods.py
name='loyy'
if name.startswith('lo'):
    print("是的，字符串以lo开头")
if 'y' in name:
    print("是的，它包含y")
if name.find('oyy') !=-1:
    print("是的,它包含字符串'oyy'")


mylist=['aaaa','bbbb','cccc','china']
print('_*_'.join(mylist))#用‘_*_’连接mylist 中的各项

