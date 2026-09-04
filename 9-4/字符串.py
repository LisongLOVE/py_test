# ==================== 字符串基础知识（可视化对比版） ====================
# 每个例子都按：原始 → 操作 → 结果 展示
# 字符串就是用引号括起来的一段文字，特点：有序、不可修改


# ---------- 0. 定义字符串 ----------
print("=== 0. 定义字符串 ===")
s1 = 'hello'
s2 = "world"
s3 = """可以跨多行"""
print(f"原始: s1 = {s1!r}（单引号）")
print(f"原始: s2 = {s2!r}（双引号）")
print(f"原始: s3 = {s3!r}（三引号，可跨多行）")


# ---------- 1. 字符串拼接与重复 ----------
print("\n=== 1. 拼接与重复 ===")
a = "你好"
b = "世界"
print(f"原始: a = {a!r}, b = {b!r}")
print("操作: a + b  （+ 号拼接）")
print(f"结果: {a + b}")
print("操作: '=' * 5  （* 号重复）")
print(f"结果: {'=' * 5}")


# ---------- 2. 字符串下标（索引） ----------
print("\n=== 2. 下标（索引） ===")
s = "python"
print(f"原始: {s}")
print("提示: 下标  0  1  2  3  4  5（正着数从0开始）")
print("      下标 -6 -5 -4 -3 -2 -1（倒数从-1开始）")
print("操作: s[0]  取第1个字符")
print(f"结果: {s[0]}")
print("操作: s[1]  取第2个字符")
print(f"结果: {s[1]}")
print("操作: s[-1] 取最后1个字符")
print(f"结果: {s[-1]}")
print("操作: s[-2] 取倒数第2个字符")
print(f"结果: {s[-2]}")


# ---------- 3. 字符串切片（截取一段） ----------
print("\n=== 3. 切片 ===")
s = "python"
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


# ---------- 4. 字符串常用方法 ----------
print("\n=== 4. 常用方法 ===")

# 去两端空格
s = " Hello Python "
print(f"原始: {s!r}")
print("操作: s.strip()  去掉两端空格")
print(f"结果: {s.strip()!r}")

# 转大小写
s = "abc"
print(f"\n原始: {s!r}")
print("操作: s.upper()  全转大写")
print(f"结果: {s.upper()}")
s = "ABC"
print(f"\n原始: {s!r}")
print("操作: s.lower()  全转小写")
print(f"结果: {s.lower()}")

# 替换
s = "I like cats"
print(f"\n原始: {s!r}")
print("操作: s.replace('cats', 'dogs')  把cats换成dogs")
print(f"结果: {s.replace('cats', 'dogs')}")

# 分割
s = "a,b,c"
print(f"\n原始: {s!r}")
print("操作: s.split(',')  按逗号切成列表")
print(f"结果: {s.split(',')}")

# 查找
s = "hello"
print(f"\n原始: {s!r}")
print("操作: s.find('l')  查找l第一次出现的位置")
print(f"结果: {s.find('l')}（下标）")
print("操作: s.find('z')  查找不存在的字符")
print(f"结果: {s.find('z')}（-1 = 找不到）")


# ---------- 5. 字符串长度 ----------
print("\n=== 5. 长度 ===")
print("原始: 'python'")
print("操作: len()  统计字符个数")
print(f"结果: {len('python')}")


# ---------- 6. 字符串格式化 ----------
print("\n=== 6. 格式化 ===")
name = "张三"
age = 18
print(f"原始: name = {name}, age = {age}")
print("方式1: f'我叫{name}，今年{age}岁'  （f-string 最推荐）")
print(f"结果: 我叫{name}，今年{age}岁")
print("方式2: '我叫%s，今年%d岁' % (name, age)  （老写法）")
print(f"结果: {'我叫%s，今年%d岁' % (name, age)}")
print("方式3: '...{}...{}'.format(name, age)")
print(f"结果: {'我叫{}，今年{}岁'.format(name, age)}")


# ---------- 7. 字符串不能修改（不可变） ----------
print("\n=== 7. 不可变 ===")
s = "abc"
print(f"原始: {s}")
print("❌ 操作: s[0] = 'A'  会报错！字符串不能修改单个字符")
# s[0] = "A"    # 取消注释会报 TypeError
print("✅ 操作: s = 'A' + s[1:]  新建一个字符串来'修改'")
s = "A" + s[1:]
print(f"结果: {s}")


# ---------- 8. 字符串的判断 ----------
print("\n=== 8. 判断 ===")

# (1) 是否为空字符串
s1 = ""
s2 = " "
print(f"原始: s1 = {s1!r}（空字符串）")
print("检查: s1 == \"\"")
print(f"结果: {s1 == ''}")
print("检查: not s1（空字符串当布尔值是 False）")
print(f"结果: {not s1}")
print(f"原始: s2 = {s2!r}（一个空格）")
print("检查: s2 == \"\"  ⚠️ 一个空格不等于空字符串！")
print(f"结果: {s2 == ''}")

# (2) 是否相等
print(f"\n检查: 'abc' == 'abc'")
print(f"结果: {'abc' == 'abc'}")
print("检查: 'abc' == 'ABC'  ⚠️ 大小写不同也算不同")
print(f"结果: {'abc' == 'ABC'}")
print("检查: 'abc' != 'abd'")
print(f"结果: {'abc' != 'abd'}")

# (3) 是否包含子串
s = "hello python"
print(f"\n原始: {s!r}")
print("检查: 'py' in s")
print(f"结果: {'py' in s}")
print("检查: 'java' in s")
print(f"结果: {'java' in s}")
print("检查: 'java' not in s")
print(f"结果: {'java' not in s}")

# (4) 是否以X开头/结尾
s = "test.py"
print(f"\n原始: {s!r}")
print("检查: s.startswith('test')")
print(f"结果: {s.startswith('test')}")
print("检查: s.endswith('.py')  （常用来判断文件类型）")
print(f"结果: {s.endswith('.py')}")
print("检查: s.endswith('.txt')")
print(f"结果: {s.endswith('.txt')}")

# (5) 内容类型判断
print(f"\n检查: '123'.isdigit()  是否全是数字")
print(f"结果: {'123'.isdigit()}")
print("检查: 'abc'.isalpha()  是否全是字母")
print(f"结果: {'abc'.isalpha()}")
print("检查: 'abc123'.isalnum()  是否全是字母或数字")
print(f"结果: {'abc123'.isalnum()}")
print("检查: 'abc 123'.isalnum()  ⚠️ 有空格不算")
print(f"结果: {'abc 123'.isalnum()}")


# ---------- 9. 字符串的"删除" ----------
# ⚠️ 字符串不可变，不能真正删除字符，只能生成新字符串实现"删除效果"
print("\n=== 9. 删除 ===")

# 切片拼接删除
s = "python"
print(f"原始: {s}")
print("操作: s[:2] + s[3:]  删掉下标2的字符't'")
new_s = s[:2] + s[3:]
print(f"结果: {new_s}")

# replace 替换为空
s = "hello world"
print(f"\n原始: {s!r}")
print("操作: s.replace(\" \", \"\")  删除所有空格")
print(f"结果: {s.replace(' ', '')!r}")

# 删左边/右边/两边
s = "000hello000"
print(f"\n原始: {s!r}")
print("操作: s.lstrip('0')  删除左边所有的'0'")
print(f"结果: {s.lstrip('0')!r}")
print("操作: s.rstrip('0')  删除右边所有的'0'")
print(f"结果: {s.rstrip('0')!r}")
print("操作: s.strip('0')   删除两边所有的'0'")
print(f"结果: {s.strip('0')!r}")


# ---------- 小抄：一眼对照表 ----------
# 操作            |  写法             |  说明
# ---------------|------------------|------------------------
# 拼接            |  "a" + "b"       |  → "ab"
# 重复            |  "ab" * 3        |  → "ababab"
# 取第i个字符     |  s[i]            |  i 从 0 开始；-1 是最后一个
# 截取一段        |  s[1:4]          |  包含 1，不包含 4
# 长度            |  len(s)          |  字符个数
# 去空格          |  s.strip()       |  去两端空格
# 大写            |  s.upper()       |  全转大写
# 小写            |  s.lower()       |  全转小写
# 替换            |  s.replace(a,b)  |  把 a 换成 b
# 分割            |  s.split(",")    |  按逗号切成列表
# 查找位置        |  s.find(x)       |  返回 x 的位置，找不到返回 -1
# 格式化(推荐)    |  f"{x}你好"      |  变量直接放在 {} 里
# 删某位置字符    |  s[:i] + s[i+1:] |  切片拼接（字符串不可变）
# 删所有匹配子串  |  s.replace(x,"") |  把 x 换成空 = 删除
# 删左边的字符    |  s.lstrip(x)     |  删左边所有 x
# 删右边的字符    |  s.rstrip(x)     |  删右边所有 x
# 删两边的字符    |  s.strip(x)      |  删两边所有 x（不填默认删空格）
# 是否相等        |  s1 == s2        |  完全一样返回 True
# 是否包含子串    |  "x" in s        |  s 里有 "x" 返回 True
# 是否为空        |  s == "" 或 not s|  空字符串当布尔值是 False
# 是否以X开头     |  s.startswith(x) |  常用来匹配前缀
# 是否以X结尾     |  s.endswith(x)   |  常用 .endswith(".py") 判断文件类型
# 是否全是数字    |  s.isdigit()     |  "123"→True
# 是否全是字母    |  s.isalpha()     |  "abc"→True
# 是否全字母/数字 |  s.isalnum()     |  "abc123"→True
