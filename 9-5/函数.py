# 1.定义函数
def num_test(num):
    num=int(input("请输入一个数字："))
    if num==100:
        print("恭喜你猜对了")
        return True
    else:
        print("很遗憾，你猜错了")
        return False
    

# 2.调用函数
num_test(100)

