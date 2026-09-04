# 集合(set)：元素不重复、无序，常用来去重
# 定义方式：set() 空集合；{1,2,3} 或 set(其他序列)
list1 = [11,22,33,44,55,66,77,88,99,11]
print(f"原始: list1 = {list1}")
print(f"类型: {type(list1).__name__}")

print("\n操作: set(list1)  列表转集合（自动去掉重复的11）")
print(f"结果: {set(list1)}")

print("\n操作: list(set(list1))  去重后转回列表")
print(f"结果: {list(set(list1))}")

print(f"\n验证: 原列表 list1 = {list1}（原列表不受影响）")


str1 = "aabbccddee"
print(f"\n原始: str1 = {str1!r}")
print(f"类型: {type(str1).__name__}")

print("\n操作: set(str1)  字符串转集合（重复字母只留一个）")
print(f"结果: {set(str1)}")

aa = set(str1)
print(f"中间: aa = {aa}")

print("\n操作: '*'.join(aa)  用*把集合中的元素连接起来")
bb = "*".join(aa) # 用*连接集合中的元素
# {bb!r} 中的 !r 是f-string的格式转换说明，等价于repr(bb)：会为字符串自动加引号、显示转义字符（如\n会显示为字面量\n），便于看清变量的真实存储内容
# ⚠️ 注意: repr 必须写在 {} 里面才会被执行;写在 {} 外面只是普通文字
print(f"结果: {repr(bb)}, 类型 = {type(bb).__name__}")
