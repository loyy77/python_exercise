##Filename ctrl.py
##Description 猜数字的小游戏,有5次尝试机会

num=7   ##要猜的数字
flag=True
count=5 ##可尝试次数

while flag and count>0:
    s=int(input('input a integer(剩余尝试次数%d):'%count))

    count=count-1
    if s==num:
        print("对了！程序退出!")
        flag=False
    elif s>num:
        print("大了")
    else:
        print("小了")
            
