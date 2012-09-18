 ##Filename:break
while True:
        s=input("请输入随意的字符串，程序将计算输入字符串的长度，（quit退出）")
        if s=="quit":
              print("exit!")
              break
        print("输入字符串的长度为：%d"%len(s))
