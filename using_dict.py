#filename:using_dict.py
ab={'taylor swift':'taylor@qq.com',
    'lisi':'lisi@153.com',
    'xiaomao':'xiaomao@gmail.com'
    
    }

print('lisi的email是',ab['lisi'])
#添加一个新的
ab['wangsan']='wangsan@huxiu.com'

#删除一个
del ab['lisi']

print(ab)


for name,addr in ab.items():
    print('%s 的email是%s'%(name,addr))

if 'wangsan' in ab:
    print('wangsan的地址是',ab['wangsan'])

    
