# ==================== 匿名函数 lambda + sort 的 key（讲解 + 可视化版） ====================
# 【这行代码在干嘛】
# user_list.sort(key=lambda x: x["age"])
#   含义: 对 user_list 排序,排序的依据(key)是每个字典里的 "age"
#
# 【拆解两个知识点】
# 1. sort(key=函数): key 参数告诉 sort "拿什么来比大小"
#    sort 会把列表里每个元素挨个传给这个函数,用返回值做比较
# 2. lambda x: x["age"]: 匿名函数(没有名字的函数),等价于:
#        def 临时函数(x):
#            return x["age"]
#    写法: lambda 参数: 返回值   (一行搞定,用完即弃)


# ---------- 例1: 原始数据 ----------
user_list = [
    {"name": "张三", "age": 16, "sex": "男"},
    {"name": "李四", "age": 20, "sex": "女"},
    {"name": "王五", "age": 22, "sex": "男"},
    {"name": "赵六", "age": 18, "sex": "女"},
]
print("=== 原始数据(年龄顺序乱) ===")
for u in user_list:
    print(f"  {u['name']}: {u['age']}岁")


# ---------- 例2: lambda 匿名函数是什么 ----------
# 【讲解】
# lambda x: x["age"] 就是一个"临时工函数":
#   传入 x(一个字典) → 返回 x["age"](年龄数字)
print("\n=== lambda 等价于普通函数 ===")
get_age = lambda x: x["age"]        # 把匿名函数赋值给变量,方便演示
print(f"原始: 张三那个字典 = {user_list[0]}")
print(f"操作: get_age(该字典)  即取 x['age']")
print(f"结果: 返回 {get_age(user_list[0])}")


# ---------- 例3: 按年龄升序排序(题目要求) ----------
print("\n=== 按年龄升序 sort(key=lambda x: x['age']) ===")
user_list.sort(key=lambda x: x["age"])
for u in user_list:
    print(f"  {u['name']}: {u['age']}岁")


# ---------- 例4: 按年龄降序(reverse=True) ----------
print("\n=== 按年龄降序(加 reverse=True) ===")
user_list.sort(key=lambda x: x["age"], reverse=True)
for u in user_list:
    print(f"  {u['name']}: {u['age']}岁")


# ---------- 例5: 换个 key 排序——按姓名排 ----------
print("\n=== 换个依据:按姓名排序 key=lambda x: x['name'] ===")
user_list.sort(key=lambda x: x["name"])
for u in user_list:
    print(f"  {u['name']}: {u['age']}岁")


# ---------- 例6: lambda 完整对照普通 def 写法 ----------
# 【讲解】下面两种写法效果完全一样,lambda 只是更简洁
def get_age_def(x):        # 普通写法:要起名、要写 return
    return x["age"]

user_list.sort(key=get_age_def)           # 写法A: 用 def 函数
print(f"def 写法: {user_list}\n")
user_list.sort(key=lambda x: x["age"])    # 写法B: 用 lambda 匿名函数(更常用,一行)
print(f"lambda 写法: {user_list}")


# ---------- 小抄 ----------
# 写法                              |  含义
# ---------------------------------|------------------------
# sort()                           |  直接按元素本身排(数字/字母)
# sort(key=lambda x: x["age"])     |  按字典的 age 排
# sort(key=lambda x: x["name"])    |  按字典的 name 排
# sort(key=..., reverse=True)      |  降序(从大到小)
# lambda x: 表达式                 |  匿名函数:传入x,返回表达式结果
