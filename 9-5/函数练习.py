# 需求:
# 1、定义字典存储测试数据,包含账号和密码
# 2、遍历数据进行测试账号和密码校验
# 3、当手机号为"13488888888"且密码为"123456"时,输出"登录成功";否则"错误或密码错误"。
test_data = [
    {"username": "13488888888", "password": "123456"},
    {"username": "", "password": "123456"}
]
def login_test(username,password):
    # 函数只负责校验,返回 True/False,不负责打印
    if username=="13488888888" and password=="123456":
        print("登录成功")
        return True
    else:
        print("错误或密码错误")
        return False


# ⚠️ if __name__ == "__main__": 的作用:
# - 直接运行本文件时,__name__ 的值是 "__main__" → 条件成立,for 循环执行(自己测自己)
# - 被其他文件 import 时,__name__ 的值是模块名 "函数练习" → 条件不成立,for 循环不执行
#   → 别人 import 时只拿到函数工具,不会跑出一堆测试输出
if __name__ == "__main__":
    for item in test_data:
        username=item["username"]
        password=item["password"]
        # 打印结果放在调用处,根据返回值决定输出什么
        if login_test(username,password):
            print("登录成功")
        else:
            print("错误或密码错误")




