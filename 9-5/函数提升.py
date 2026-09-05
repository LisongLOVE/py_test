# 缺省函数 带有默认值
# 缺省函数形参注意事项：
# 1. 形参（默认值）必须放最后
def st_info(name,age, sex="男"):
    print(f"姓名: {name}, 年龄: {age}, 性别: {sex}")

# 简化调用
st_info("张三",16)
st_info("李四", 20, "女")




# 多值参数
def sum_nums(*args):
    total = 0
    for num in args:
        total += num
    return total













# ==================== *args 和 args 的区别（讲解 + 可视化版） ====================
# 【讲解】
# 定义函数时写 *args: 星号 * 是"收集器",把调用时传的任意多个位置参数【打包】成一个元组
# 函数体内用 args(不带*): 它就是一个普通元组,里面装着收集到的所有值
#   - 可以 for 遍历
#   - 可以下标 args[0]、切片 args[1:]
#   - 可以 len(args) 看传了几个
# 注意:
#   1. args 这个名字是约定俗成(arguments 缩写),写成 *nums 也完全可以,关键是 *
#   2. *args 必须放在普通参数后面
#   3. 收集的是"位置参数";还有个 **kwargs 收集"关键字参数"(字典),以后会学


# ---------- 例1: *args 把多个参数打包成元组 ----------
print("=== 例1: *args 收集成元组 ===")
def show_args(*args):
    print(f"  函数体内 args = {args}")
    print(f"  type(args) = {type(args).__name__}")   # tuple 元组
    print(f"  len(args) = {len(args)}  (传了几个参数)")
    print(f"  args[0] = {args[0]}, args[-1] = {args[-1]}")

print("调用: show_args(10, 20, 30)")
show_args(10, 20, 30)
print("调用: show_args('a', 'b')  (传2个也行,个数不限)")
show_args("a", "b")


# ---------- 例2: 对比——没有 * 的普通参数 ----------
print("\n=== 例2: 有 * vs 没有 * ===")
def one_arg(args):        # 没有 *: args 只是一个普通参数,传什么是什么
    print(f"  one_arg 收到: args = {args}, 类型 = {type(args).__name__}")

def multi_arg(*args):     # 有 *: 把多个参数打包成元组
    print(f"  multi_arg 收到: args = {args}, 类型 = {type(args).__name__}")

print("调用: one_arg([1,2,3])   (手动传一个列表)")
one_arg([1, 2, 3])
print("调用: multi_arg(1,2,3)   (*自动打包成元组)")
multi_arg(1, 2, 3)


# ---------- 例3: 普通参数 + *args 混用 ----------
print("\n=== 例3: 普通参数必须在 *args 前面 ===")
def student_info(name, *scores):
    print(f"  姓名: {name}")
    print(f"  成绩(元组): {scores}")
    print(f"  平均分: {sum(scores) / len(scores):.1f}")

student_info("张三", 80, 90, 100)


# ---------- 小抄 ----------
# 写法              |  * 的作用        |  函数体内的 args
# -----------------|-----------------|------------------
# def f(*args):    |  收集多个位置参数 |  元组 tuple,如 (1,2,3)
# def f(args):     |  没有收集,普通参数|  传什么就是什么(一个值)
# f(1,2,3) 配 *args|  自动打包        |  args == (1, 2, 3)
# 遍历             |  for x in args:  |  逐个取出元组元素


# ==================== += 和 =+ 的区别（讲解 + 可视化版） ====================
# 【讲解】
# +=  : 复合赋值运算符,等价于 x = x + 右边  → 累加/追加
# =+  : 不是运算符!是 = 赋值 + 正号(+) → 等价于 x = (+右边) → 直接覆盖
#
# 常见复合赋值运算符(都是 运算符 在前,= 在后):
#   +=  加后赋值   x += 1  →  x = x + 1
#   -=  减后赋值   x -= 1  →  x = x - 1
#   *=  乘后赋值   x *= 2  →  x = x * 2
#   /=  除后赋值   x /= 2  →  x = x / 2
# 记忆: 运算符写在 = 左边才对!写反了(=+)逻辑完全变了


# ---------- 例1: += 累加(正确写法) ----------
print("=== 例1: += 累加(正确) ===")
total = 0
print(f"原始: total = {total}")
for num in [10, 20, 30]:
    total += num
    print(f"操作: total += {num}   (等价 total = total + {num}) → total = {total}")
print(f"结果: {total}  ← 10+20+30 = 60,累加成功")


# ---------- 例2: =+ 覆盖(错误写法,每次被覆盖) ----------
print("\n=== 例2: =+ 覆盖(错误,不是累加!) ===")
total2 = 0
print(f"原始: total2 = {total2}")
for num in [10, 20, 30]:
    total2 =+ num   # 等价于 total2 = (+num) = num,直接覆盖!
    print(f"操作: total2 =+ {num}   (等价 total2 = +{num} = {num}) → total2 = {total2}")
print(f"结果: {total2}  ← 只剩最后一个30!前两次全被覆盖了")


# ---------- 例3: 调用 sum_nums 验证 *args 多值参数 ----------
print("\n=== 例3: 多值参数 *args 调用 ===")
print(f"sum_nums(1,2,3)     = {sum_nums(1, 2, 3)}")
print(f"sum_nums(10,20,30)  = {sum_nums(10, 20, 30)}")


# ---------- 小抄 ----------
# 写法     |  等价于            |  效果
# --------|-------------------|----------------
# x += 5   |  x = x + 5        |  ✅ 累加5
# x =+ 5   |  x = (+5) = 5     |  ❌ 直接变成5(覆盖)
# x -= 5   |  x = x - 5        |  ✅ 减5
# x =- 5   |  x = (-5) = -5    |  ❌ 直接变成-5(覆盖)
