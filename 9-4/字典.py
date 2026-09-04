# ==================== 字典基础知识（可视化对比版） ====================
# 每个例子都按：原始 → 操作 → 结果 展示
# 字典(Dict)用花括号 {} 括起来，每个元素是 键:值 对，键唯一


# ---------- 0. 定义字典 ----------
print("=== 0. 定义字典 ===")
dic1 = {'name': '张三', 'age': 18, 'sex': '男', 'pwd': '123456'}
print(f"原始: {dic1}")


# ---------- 1. 字典元素的查询 ----------
print("\n=== 1. 查询 ===")
dic1 = {'name': '张三', 'age': 18, 'sex': '男', 'pwd': '123456'}
print(f"原始: {dic1}")
print("操作: dic1['name']  用方括号取值（键不存在会报错）")
print(f"结果: {dic1['name']}")
print("操作: dic1.get('name')  用 get 取值（推荐，键不存在返回 None 不报错）")
print(f"结果: {dic1.get('name')}")
print("操作: dic1.get('xxx')  取不存在的键")
print(f"结果: {dic1.get('xxx')}（None = 空，不报错）")


# ---------- 2. 字典的修改和新增 ----------
print("\n=== 2. 修改和新增 ===")
dic1 = {'name': '张三', 'age': 18, 'sex': '男', 'pwd': '123456'}
print(f"原始: {dic1}")
print("操作: dic1['city'] = '北京'  （键不存在 = 新增）")
dic1['city'] = '北京'
print(f"结果: {dic1}")

print(f"\n原始: {dic1}")
print("操作: dic1['age'] = 20  （键已存在 = 修改）")
dic1['age'] = 20
print(f"结果: {dic1}")


# ---------- 3. 字典元素的删除 ----------
print("\n=== 3. 删除 ===")
dic1 = {'name': '张三', 'age': 18, 'sex': '男', 'pwd': '123456'}
print(f"原始: {dic1}")
print("操作: del dic1['pwd']  按键删除（内存释放）")
del dic1['pwd']
print(f"结果: {dic1}")

dic1 = {'name': '张三', 'age': 18, 'sex': '男', 'pwd': '123456'}
print(f"\n原始: {dic1}")
print("操作: dic1.pop('age')  弹出并返回该键的值")
v = dic1.pop('age')
print(f"结果: {dic1}（弹出的值: {v}）")


# ---------- 4. 字典的遍历 ----------
print("\n=== 4. 遍历 ===")
dic1 = {'name': '张三', 'age': 18, 'sex': '男', 'pwd': '123456'}
print(f"原始: {dic1}")
print("方式1: for j in dic1.keys()  遍历键")
for j in dic1.keys():
    print(f"  结果: {j}")
print("⚠️ 注意: 遍历出的 j 是键，可以用 dic1[j] 取值")

print("\n方式2: for j in dic1.values()  遍历值")
for j in dic1.values():
    print(f"  结果: {j}")
print("⚠️ 注意: 遍历出的 j 是值，不能再 dic1[j]（会 KeyError）")

print("\n方式3: for k, v in dic1.items()  同时遍历键和值（最常用）")
for k, v in dic1.items():
    print(f"  结果: {k} = {v}")


# ---------- 5. 字典 vs 列表 ----------
# 列表: [元素, 元素]      用下标访问    s[0]
# 字典: {键:值, 键:值}    用键访问      d['name']


# ---------- 小抄：一眼对照表 ----------
# 操作            |  写法               |  说明
# ---------------|--------------------|------------------------
# 定义            |  {'k': v}          |  花括号 + 键:值
# 查询(报错型)    |  d['k']            |  键不存在报 KeyError
# 查询(安全型)    |  d.get('k')        |  键不存在返回 None
# 新增/修改       |  d['k'] = v        |  键不存在=新增，存在=修改
# 按键删除        |  del d['k']        |  删除该键值对
# 弹出            |  d.pop('k')        |  删除并返回该键的值
# 遍历键          |  d.keys()          |  取出的是键
# 遍历值          |  d.values()        |  取出的是值
# 遍历键值        |  d.items()         |  for k, v in ... 最常用
