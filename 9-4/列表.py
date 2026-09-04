# ==================== 列表基础知识（可视化对比版） ====================
# 每个例子都按：原始 → 操作 → 结果 展示
# 列表(List)用方括号 [] 括起来，特点：有序、可修改、可放任意类型


# ---------- 0. 定义列表 ----------
print("=== 0. 定义列表 ===")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lis12 = [11, 22, 33, 44, 55]
names = ["张三", "李四", "王五"]
mixed = [1, "hello", 3.14, True]
empty = []
print(f"原始: list1 = {list1}")
print(f"原始: names = {names}")
print(f"原始: mixed = {mixed}")
print(f"原始: empty = {empty}")


# ---------- 1. 列表拼接与重复 ----------
print("\n=== 1. 拼接与重复 ===")
print(f"原始: list1 = {list1}")
print(f"      lis12 = {lis12}")
print("操作: list1 + lis12 （+ 号拼接）")
print(f"结果: {list1 + lis12}")

print(f"\n原始: [0]")
print("操作: [0] * 5 （* 号重复）")
print(f"结果: {[0] * 5}")


# ---------- 2. 列表下标（索引） ----------
print("\n=== 2. 下标（索引） ===")
s = ["a", "b", "c", "d", "e"]
print(f"原始: {s}")
print("提示: 下标  0  1  2  3  4（正着数从0开始）")
print("      下标 -5 -4 -3 -2 -1（倒数从-1开始）")
print("操作: s[0]  取第1个")
print(f"结果: {s[0]}")
print("操作: s[1]  取第2个")
print(f"结果: {s[1]}")
print("操作: s[-1] 取最后1个")
print(f"结果: {s[-1]}")
print("操作: s[-2] 取倒数第2个")
print(f"结果: {s[-2]}")


# ---------- 3. 列表切片（截取一段） ----------
print("\n=== 3. 切片 ===")
s = ["a", "b", "c", "d", "e"]
print(f"原始: {s}")
print("提示: 语法 s[起始:结束]  包含起始，不包含结束")
print("操作: s[0:3]  从下标0取到下标2")
print(f"结果: {s[0:3]}")
print("操作: s[2:]   从下标2取到最后")
print(f"结果: {s[2:]}")
print("操作: s[:3]   从开头取到下标2")
print(f"结果: {s[:3]}")
print("操作: s[:]    从头取到尾（复制）")
print(f"结果: {s[:]}")


# ---------- 4. 列表可以修改（可变，和字符串最大的区别！） ----------
print("\n=== 4. 修改元素 ===")
s = ["a", "b", "c"]
print(f"原始: {s}")
print("操作: s[0] = 'X'  把下标0的元素改成X")
s[0] = "X"
print(f"结果: {s}")
print("⚠️ 字符串不能这样改，列表可以！")


# ---------- 5. 列表常用方法 ----------
print("\n=== 5. 常用方法：增删改排 ===")

# 追加 append
s = [1, 2, 3]
print(f"原始: {s}")
print("操作: s.append(100)  末尾追加")
s.append(100)
print(f"结果: {s}")

# 插入 insert
s = [1, 2, 3]
print(f"\n原始: {s}")
print("操作: s.insert(1, 999)  在下标1处插入999")
s.insert(1, 999)
print(f"结果: {s}")

# 按值删除 remove
s = [1, 2, 1, 3]
print(f"\n原始: {s}")
print("操作: s.remove(1)  删除第一个值为1的元素")
s.remove(1)
print(f"结果: {s}")

# 按下标删除 del
s = [10, 20, 30]
print(f"\n原始: {s}")
print("操作: del s[0]  删除下标0的元素")
del s[0]
print(f"结果: {s}")

# 弹出 pop
s = [1, 2, 3]
print(f"\n原始: {s}")
print("操作: last = s.pop()  取出并删除最后一个")
last = s.pop()
print(f"结果: {s}（弹出的值: {last}）")

# 排序 sort
s = [3, 1, 4, 1, 5]
print(f"\n原始: {s}")
print("操作: s.sort()  升序排序")
s.sort()
print(f"结果: {s}")
print("操作: s.sort(reverse=True)  降序排序")
s.sort(reverse=True)
print(f"结果: {s}")

# 反转 reverse
s = [1, 2, 3]
print(f"\n原始: {s}")
print("操作: s.reverse()  原地翻转")
s.reverse()
print(f"结果: {s}")

# 统计次数 count
print(f"\n原始: [1, 1, 2, 3, 1]")
print("操作: .count(1)  统计1出现的次数")
print(f"结果: {[1, 1, 2, 3, 1].count(1)}")


# ---------- 6. 列表长度 ----------
print("\n=== 6. 长度 ===")
print("原始: [1, 2, 3]")
print("操作: len()  统计元素个数")
print(f"结果: {len([1, 2, 3])}")


# ---------- 7. 遍历列表 ----------
print("\n=== 7. 遍历 ===")
fruits = ["apple", "banana", "cherry"]
print(f"原始: {fruits}")
print("方式1: for f in fruits  直接遍历元素")
for f in fruits:
    print(f"  结果: {f}")
print("方式2: for i, f in enumerate(fruits)  同时取下标和元素（推荐）")
for i, f in enumerate(fruits):
    print(f"  结果: 下标{i} → {f}")


# ---------- 8. 判断元素是否在列表里 ----------
print("\n=== 8. 判断包含 ===")
nums = [1, 2, 3, 4, 5]
print(f"原始: {nums}")
print("检查: 3 in nums")
print(f"结果: {3 in nums}")
print("检查: 10 in nums")
print(f"结果: {10 in nums}")
print("检查: 10 not in nums")
print(f"结果: {10 not in nums}")


# ---------- 9. 判断空列表 ----------
print("\n=== 9. 空列表判断 ===")
empty = []
print(f"原始: {empty}")
print("检查: empty == []")
print(f"结果: {empty == []}")
print("检查: not empty（空列表当布尔值是 False）")
print(f"结果: {not empty}")


# ---------- 小抄：一眼对照表 ----------
# 操作            |  写法              |  说明
# ---------------|-------------------|------------------------
# 定义            |  [1, 2, 3]        |  方括号括起来
# 拼接            |  [1] + [2]        |  → [1, 2]
# 重复            |  [0] * 3          |  → [0, 0, 0]
# 取第i个元素     |  s[i]             |  i 从 0 起；-1 是最后
# 切片            |  s[1:4]           |  包含 1，不包含 4
# 修改元素        |  s[0] = X         |  列表可改(字符串不能)
# 追加            |  s.append(x)      |  末尾添加
# 插入            |  s.insert(i, x)   |  在下标 i 处插入
# 按值删除        |  s.remove(x)      |  删第一个值为 x 的元素
# 按下标删除      |  del s[i]         |  删除下标 i 的元素
# 弹出            |  s.pop()          |  取出并删除最后一个
# 排序            |  s.sort()         |  升序；降序加 reverse=True
# 反转            |  s.reverse()      |  原地翻转
# 统计次数        |  s.count(x)       |  x 在列表里出现几次
# 长度            |  len(s)           |  元素个数
# 是否包含        |  x in s           |  x 在 s 里返回 True
# 是否为空        |  s == [] 或 not s |  空列表当布尔值是 False
