# ==================== 捕获异常 try-except（讲解 + 可视化版） ====================
# 【为什么要捕获异常】
# 程序运行出错时,默认行为是: 打印红色错误信息 + 整个程序崩溃停止
# 捕获异常 = 提前预判"这里可能出错",出错时不让程序死,而是走备用方案
#
# 【基本结构】
# try:
#     可能出错的代码
# except 错误类型:
#     出这种错时怎么办
# else:
#     没出错时执行(很少用)
# finally:
#     无论出不出错都执行(常用于收尾,如关文件)
#
# 【执行规则】
# 1. try 里正常 → 跳过所有 except → 走 else → 走 finally
# 2. try 里出错 → 拿错误类型从上往下匹配 except,只进【第一个】匹配上的
# 3. 没有任何 except 匹配 → 错误照样抛出,程序崩溃
# 4. 父类 Exception 能抓所有错误,必须放最后(否则抢走子类的)


# ---------- 例1: 不捕获 vs 捕获 的对比 ----------
# 【讲解】
# int("abc") 会报 ValueError(字符串转不成数字)
print("=== 例1: 捕获后程序不死 ===")
try:
    num = int("abc")          # 这行必然出错
    print(f"转换成功: {num}")   # 出错后这行不会执行
except ValueError:
    print("结果: 转不成数字,但程序没死,继续往下走")


# ---------- 例2: 多种错误类型,分别处理 ----------
# 【讲解】
# 可以写多个 except,按错误类型给不同提示
print("\n=== 例2: 多 except 分别处理 ===")

def safe_divide(a, b):
    try:
        result = a / b
        return f"结果: {a} / {b} = {result}"
    except ZeroDivisionError:
        return f"结果: {a} / {b} → 除数不能为0!"
    except TypeError:
        return f"结果: {a!r} 和 {b!r} → 类型不对,没法除!"

print(safe_divide(10, 2))     # 正常
print(safe_divide(10, 0))     # ZeroDivisionError
print(safe_divide(10, "a"))   # TypeError


# ---------- 例3: as e 拿到错误详情 ----------
# 【讲解】
# except 错误类型 as e:  e 就是错误对象,打印 e 能看到具体原因
print("\n=== 例3: as e 获取错误信息 ===")
try:
    num = int("xyz")
except ValueError as e:
    print(f"抓到错误对象 e = {e!r}")
    print(f"e 的类型 = {type(e).__name__}")


# ---------- 例4: 常见错误类型一览(都会被抓住) ----------
print("\n=== 例4: 常见错误类型 ===")

def catch_it(func, name):
    try:
        func()
    except Exception as e:
        print(f"  {name}: 抓到 {type(e).__name__} → {e}")

catch_it(lambda: int("abc"),    "int('abc')  ")
catch_it(lambda: 1 / 0,         "1 / 0        ")
catch_it(lambda: [1, 2][5],     "列表[5]越界   ")
catch_it(lambda: {}["name"],    "字典取不存在的键")
catch_it(lambda: print(未定义),   "用不存在的变量  ")


# ---------- 例5: else 和 finally ----------
# 【讲解】
# else   : try 里没出错才执行
# finally: 不管出不出错,最后一定执行(收尾用)
print("\n=== 例5: else(没出错) / finally(总是执行) ===")

def demo(x):
    print(f"--- 输入 {x!r} ---")
    try:
        num = int(x)
    except ValueError:
        print("  except: 出错了")
    else:
        print(f"  else: 没出错,转换结果 = {num}")
    finally:
        print("  finally: 我一定会执行(收尾工作)")

demo("123")    # 没出错
demo("abc")    # 出错


# ---------- 例6: Exception 是"兜底",必须放最后 ----------
# 【讲解】
# 错误类型有父子关系: ZeroDivisionError 等都是 Exception 的子类
# except 从上往下匹配,如果 Exception 写前面,会把所有错误都抢走
print("\n=== 例6: 具体错误在前,Exception 兜底在后 ===")
try:
    [1, 2][9]
except IndexError:
    print("结果: IndexError 下标越界(具体类型先匹配上了)")
except Exception as e:
    print(f"结果: 兜底抓到 {type(e).__name__}")


# ---------- 小抄 ----------
# 关键字           |  什么时候执行
# ----------------|--------------------------
# try             |  放可能出错的代码
# except 类型      |  出该类型错误时执行(可写多个,只进第一个)
# except ... as e |  同时拿到错误对象 e
# except Exception|  兜底:抓所有错误(必须放最后)
# else            |  try 没出错才执行
# finally         |  无论对错都执行(收尾)
#
# 常见错误类型        |  触发场景
# ------------------|--------------------------
# ValueError        |  值不对:int("abc")
# ZeroDivisionError |  除以 0
# IndexError        |  列表/元组下标越界
# KeyError          |  字典键不存在
# NameError         |  变量没定义
# TypeError         |  类型不对:1/"a"
# FileNotFoundError |  文件不存在
