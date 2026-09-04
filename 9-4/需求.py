#需求:
#1、定义字典存储测试数据，包含账号和密码
#2、遍历数据进行测试账号和密码校验
#3、当手机号为"13488888888"且密码为"123456"时，输出"登录成功";否则"账号或密码错误"。

info = [
    {"username": "13488888888", "pwd": "123456"},   # 账号密码都正确
    {"username": "13488888888", "pwd": "111111"},   # 账号对，密码错
    {"username": "12345",       "pwd": "123456"},   # 账号错，密码对
    {"username": "",            "pwd": "123456"}    # 账号为空
]

print(f"原始: 测试数据共 {len(info)} 条:")
for i, item in enumerate(info):
    print(f"  第{i + 1}条: username={item['username']!r}, pwd={item['pwd']!r}")

print("\n操作: for item in info 遍历，校验 账号==13488888888 且 密码==123456")
print("结果:")
for i, item in enumerate(info):
    username = item["username"]
    pwd = item["pwd"]
    if username == "13488888888" and pwd == "123456":
        print(f"  第{i + 1}条({username!r}, {pwd!r}) → 登录成功")
    else:
        print(f"  第{i + 1}条({username!r}, {pwd!r}) → 账号或密码错误")
