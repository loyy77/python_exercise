## Filename continue.py
while True:
    s=input("请输入一个长度大于3 的单词以计算单词的长度")
    if s=="quit":
        print("程序退出")
        break
    elif len(s)<3:
        print("这么短的单词你也好意思!")
        continue
    print("单词长度为%d"%len(s))
    
