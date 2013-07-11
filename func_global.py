#filename:func_global.py
def func():
    global x

    print ('x is',x)
    x=2
    print ('changed local x to ',x)
x=540
func()
print('val of x is ',)
