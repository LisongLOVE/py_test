# 匿名函数
# 也叫 lambda 函数
# 正常情况
def add(a, b):
    return a + b
print(add(1, 2))
# 匿名函数
# 一行函数
# 直接创建lambda匿名函数（未赋值、未调用，仅作为匿名函数的形式示例）
lambda c, d: c + d
# 将lambda匿名函数赋值给变量result，方便后续调用
result=lambda c, d: c + d
# 调用变量result指向的匿名函数，传入1和2，打印运算结果
print(result(1, 2))
