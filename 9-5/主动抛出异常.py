# ==================== 主动抛出异常 raise（讲解 + 可视化版） ====================
# 【什么是主动抛出异常】
# 前面学的 try-except 是"接住"错误(被动捕获)
# raise 是反过来:程序员"主动制造"一个错误 —— 当数据不符合业务规则时,主动中断并提示
#
# 【为什么需要 raise】
# Python 只会在"语法/运行"出错时自动报错(如除0、类型错)
# 但业务规则它不懂,比如: 年龄不能是负数、密码不能少于6位
# 这类"逻辑上不允许"的情况,需要我们自己用 raise 喊停
#
# 【语法】
# raise 异常类型("提示信息")
#   异常类型常用: ValueError(值不合理)、Exception(通用)
#   抛出后: 程序中断,提示信息会显示出来;也可以被 try-except 接住


# ---------- 例1: 最基本的 raise ----------
# 【讲解】
# raise 一执行,程序立刻中断,后面的代码不再运行
print("=== 例1: raise 主动中断 ===")
try:
    print("raise 之前: 正常执行")
    raise ValueError("这是我主动抛出的错误!")
    print("raise 之后: 这行永远不会执行")   # 中断了,走不到
except ValueError as e:
    print(f"被接住: {e}")


# ---------- 例2: 实际用途——参数校验 ----------
# 【讲解】
# 函数开头检查参数是否合理,不合理就 raise 喊停,避免后面用错误数据算出错误结果
print("\n=== 例2: 函数参数校验 ===")

def register(name, age):
    if not name:
        raise ValueError("用户名不能为空")
    if age < 0 or age > 150:
        raise ValueError(f"年龄不合理: {age}(应在 0~150 之间)")
    return f"注册成功: {name}, {age}岁"

# 正常情况
print(f"正常: {register('张三', 18)}")
# 错误情况用 try 接住
for n, a in [("", 18), ("李四", -5)]:
    try:
        register(n, a)
    except ValueError as e:
        print(f"拦截: {e}")


# ---------- 例3: raise 抛出的错误,和系统错误一样能被捕获 ----------
# 【讲解】
# 主动 raise 的异常和 Python 自动报的错,本质完全一样,都能被 except 抓住
print("\n=== 例3: raise 的错误也能被 except 捕获 ===")
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("除数是0,我主动拦的!")   # 手动抛
    return a / b

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(f"抓到: {type(e).__name__} → {e}")


# ---------- 例4: 系统自动抛 vs 我们主动抛 ----------
print("\n=== 例4: 自动抛 vs 主动抛 ===")
# 自动抛: Python 自己发现的错误
try:
    int("abc")
except ValueError as e:
    print(f"系统自动抛: {e}")
# 主动抛: 我们根据业务规则抛
try:
    age = -3
    if age < 0:
        raise ValueError(f"年龄不能为负: {age}")
except ValueError as e:
    print(f"我们主动抛: {e}")


# ---------- 小抄 ----------
# 写法                          |  作用
# -----------------------------|------------------------
# raise ValueError("提示")      |  主动抛一个值错误
# raise Exception("提示")       |  主动抛一个通用错误
# raise                         |  在 except 里单独用:把抓到的错误原样再抛出去
#
# 对比          |  触发者      |  例子
# -------------|-------------|------------------------
# 系统自动报错   |  Python     |  1/0、int("abc")
# raise 主动抛   |  程序员     |  年龄<0、密码太短
#
# 记住: raise = "这里不符合规则,我主动叫停!";
#       try-except = "出错了别崩溃,我来处理"。两者常配合使用。
