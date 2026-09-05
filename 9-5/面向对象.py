# ==================== 面向对象 OOP（讲解 + 可视化版） ====================
# 【什么是面向对象】
# 面向对象 Object Oriented Programming (OOP) 是一种编程思想
# 核心概念:用"类"和"对象"来组织代码,而不是按步骤写函数
#
# 【面向过程 vs 面向对象】
#   面向过程:按步骤写函数,简单直接,但需求一变得改很多地方
#   面向对象:围绕"对象"组织代码,每个对象各司其职,适应变化、好维护
#   例子:面向过程像写菜谱(一步步做);面向对象像造零件(坏了换哪个不影响整体)
#
# 【类和对象两个核心概念】
#   类(class)   = 图纸/类别,抽象的,不能直接用
#   对象(object) = 按图纸造出来的具体东西,能用(也叫"实例")
#   类包含:
#     属性(静态特征) → 名字、年龄
#     方法(动态行为) → 吃、喝
#
# 【设计类三要素】
#   类名:大驼峰命名法(如 LoginPage、Cat)
#   属性:同类事物具备的特征
#   方法:同类事物具备的行为
#   原则:根据需求,没提到的属性方法不用加


# ============================== 1. 定义类 + 创建对象 ==============================
# 【讲解】
# 语法:
#   class 类名:
#       def 方法名(self, 参数):
#           pass
# 说明:
#   - class 是关键字,类名用大驼峰(每个单词首字母大写)
#   - 类里的方法,第一个参数永远是 self(代表对象自己)
#   - pass 是占位符,什么都不做,让代码不报错
#   - 类是抽象的,定义后不创建对象不能直接用
# 创建对象(实例化):
#   对象变量 = 类名()
# 调用方法:
#   对象变量.方法名()
print("=== 1. 定义类 + 创建对象 ===")


class Cat:
    """猫类"""

    def eat(self):
        """吃的方法"""
        print("小猫爱吃鱼")

    def drink(self):
        """喝的方法"""
        print("小猫要喝水")


# 创建对象(实例化)
tom = Cat()
print(f"操作: tom = Cat()  创建对象")
print(f"结果: tom 的类型 = {type(tom).__name__}, id = {id(tom)}")

# 调用方法
print(f"操作: tom.eat()    对象调用方法")
tom.eat()
print(f"操作: tom.drink()")
tom.drink()

# 同一个类可以创建多个对象,每个对象互不影响
lazy = Cat()
print(f"\n操作: lazy = Cat()  再创建一个对象")
print(f"结果: lazy 的 id = {id(lazy)}")
print(f"验证: tom 和 lazy 是同一个对象吗? {tom is lazy}  ← 不同对象!")


# ============================== 2. self 参数 ==============================
# 【讲解】
# self = 对象自己
# 哪个对象调用方法,方法内的 self 就是那个对象
# 作用:在类内部,通过 self 访问对象的属性和其他方法
# 类外部:用  对象.属性  /  对象.方法()
# 类内部:用  self.属性  /  self.方法()
print("\n=== 2. self 参数 ===")


class Dog:
    """狗类"""

    def show_self(self):
        """演示 self 就是对象自己"""
        print(f"  方法内 self 的 id = {id(self)}")

    def bark(self):
        """叫"""
        print("  汪汪汪!")


d1 = Dog()
d2 = Dog()
print(f"原始: d1 的 id = {id(d1)}, d2 的 id = {id(d2)}")
print(f"操作: d1.show_self()  → d1 调用,self 就是 d1")
d1.show_self()
print(f"操作: d2.show_self()  → d2 调用,self 就是 d2")
d2.show_self()
print(f"结论: self 的 id 和调用对象一致 → self 就是对象自己")


# ============================== 3. __init__ 初始化方法 ==============================
# 【讲解】
# __init__ 是内置方法,创建对象时自动调用,用来给对象设置属性
# 语法:
#   def __init__(self, 参数):
#       self.属性名 = 参数
# 说明:
#   - 创建对象时,括号里传的实参,会传给 __init__ 的形参
#   - self.属性名 = 值  这一句就是"给对象设置属性"
#   - 创建对象后,对象就已经有属性了
# 注意:双下划线开头结尾的方法叫"内置方法/魔术方法"(如 __init__)
print("\n=== 3. __init__ 初始化方法 ===")


class Cat2:
    """猫类,带属性"""

    def __init__(self, name):
        """初始化方法:创建对象时自动调用,给对象设置属性"""
        self.name = name        # self.name 就是对象的属性

    def eat(self):
        """吃方法,用 self.name 访问属性"""
        print(f"  {self.name} 爱吃鱼")

    def drink(self):
        """喝方法"""
        print(f"  {self.name} 要喝水")


# 创建对象,传入实参
tom = Cat2("汤姆")
lazy = Cat2("懒猫")
print(f"操作: tom = Cat2('汤姆')  创建对象时传参,自动调 __init__")
print(f"结果: tom.name = {tom.name}  ← 类外部用 对象.属性 访问")
print(f"操作: lazy = Cat2('懒猫')")
print(f"结果: lazy.name = {lazy.name}")
print(f"操作: tom.eat()  方法内用 self.name 取属性")
tom.eat()
lazy.drink()


# ============================== 4. dir() 查看对象内容 ==============================
# 【讲解】
# dir(对象) 返回对象的所有属性和方法(包括 Python 自带的)
# 应用场景:想知道对象有哪些属性方法时用
print("\n=== 4. dir() 查看对象有哪些属性方法 ===")
print(f"操作: dir(tom)")
attrs = dir(tom)
print(f"结果(前几个是Python自带的): {attrs[:5]} ...")
print(f"      自己定义的: {['name', 'eat', 'drink']}")


# ============================== 5. 面向对象术语对照 ==============================
print("\n=== 5. 面向对象术语对照 ===")
print("定义类     → class 类名:")
print("定义属性   → def __init__(self, 形参):  self.属性 = 形参")
print("创建对象   → 对象 = 类名(实参)           (也叫:实例化)")
print("使用属性   → 类内: self.属性   类外: 对象.属性")
print("使用方法   → 类内: self.方法() 类外: 对象.方法()")


# ============================== 6. 封装 ==============================
# 【讲解】
# 封装 = 把属性和方法"打包"进一个类里
# 好处:造车原理你不用管,会开就行——细节隐藏,只暴露必要接口
# 实际用途:把相关的数据和操作组织在一起,方便复用
print("\n=== 6. 封装案例:登录页 ===")


class LoginPage:
    """登录页面类:把用户名、密码、登录逻辑封装在一起"""

    def __init__(self, username, password, verify_code):
        """设置属性"""
        self.username = username
        self.password = password
        self.code = verify_code

    def login(self):
        """登录方法"""
        print(f"  请输入用户名: {self.username}")
        print(f"  请输入密码: {self.password}")
        print(f"  请输入验证码: {self.code}")
        print("  点击登录按钮")


# 创建登录对象
page = LoginPage("13488888888", "123456", "ABCD")
print(f"操作: page = LoginPage('13488888888', '123456', 'ABCD')")
print(f"结果: page 的属性 → username={page.username}, password={page.password}")
print(f"操作: page.login()  调用封装的登录方法")
page.login()
print(f"结论: 用户名/密码/验证码+登录逻辑,全打包在 LoginPage 类里")


# ============================== 7. 继承 ==============================
# 【讲解】
# 继承 = 子类拥有父类的所有属性和方法,省得重复写
# 语法: class 子类(父类名):
# 术语: 父类(基类/超类) → 子类(派生类)
# 说明:
#   - 子类自动拥有父类的属性和方法
#   - 子类可以加自己的属性和方法
#   - 多个类有相同代码,抽到父类里,子类继承 → 少写重复代码
print("\n=== 7. 继承 ===")


class Animal:
    """动物类(父类)"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"  {self.name} 吃东西")

    def sleep(self):
        print(f"  {self.name} 要睡觉")


class CatSub(Animal):
    """猫类(子类),自动拥有 Animal 的属性和方法"""

    def catch(self):
        """猫类自己的方法"""
        print(f"  {self.name} 会抓老鼠")


class XiaoTianQuan(Animal):
    """哮天犬类(子类)"""

    def fly(self):
        print(f"  {self.name} 会飞")


# 创建子类对象
tom = CatSub("汤姆", 3)
print(f"操作: tom = CatSub('汤姆', 3)  子类对象")
print(f"操作: tom.eat()      ← 父类的方法,子类直接用")
tom.eat()
print(f"操作: tom.catch()    ← 子类自己的方法")
tom.catch()
print(f"操作: tom.sleep()    ← 父类方法也能用")
tom.sleep()

xtq = XiaoTianQuan("天神", 100)
print(f"\n操作: xtq = XiaoTianQuan('天神', 100)")
print(f"操作: xtq.fly()")
xtq.fly()
print(f"结论: 子类拥有父类的所有属性和方法")


# ============================== 8. 方法重写 ==============================
# 【讲解】
# 重写(override):父类方法满足不了子类需求时,在子类里重新定义同名方法
# 两种方式:
#   覆盖式:子类定义同名方法,完全替代父类的
#   扩展式:super().方法名() 先调父类,再加自己的逻辑
print("\n=== 8. 方法重写(覆盖式 vs 扩展式) ===")


class AnimalEat:
    def eat(self):
        print(f"  {self.name} 吃东西(父类版本)")


class OverrideCat(AnimalEat):
    """覆盖式重写:完全替代"""

    def eat(self):
        print(f"  {self.name} 只爱吃鱼(覆盖了父类)")


class ExtendCat(AnimalEat):
    """扩展式重写:先调父类,再加自己的"""

    def eat(self):
        super().eat()              # 先执行父类的 eat
        print(f"  {self.name} 更喜欢吃鱼(在父类基础上扩展)")


# 覆盖式演示
oc = OverrideCat()
oc.name = "覆盖猫"
print(f"操作: OverrideCat.eat()  → 覆盖式(父类不执行)")
oc.eat()

# 扩展式演示
ec = ExtendCat()
ec.name = "扩展猫"
print(f"\n操作: ExtendCat.eat()   → 扩展式(父类+子类都执行)")
ec.eat()
print(f"结论: 覆盖式=只走子类;扩展式=super()调父类再补充")


# ============================== 9. 多态(了解) ==============================
# 【讲解】
# 多态 = 不同子类对象调用相同的父类方法,产生不同的结果
# 条件:有继承 + 子类重写父类方法
# 好处:同一个调用接口,传不同对象就有不同行为,代码灵活
print("\n=== 9. 多态(了解) ===")


class DogPlay:
    """狗类"""

    def game(self):
        print("  在地上玩耍")


class XiaoTianDog(DogPlay):
    """哮天犬,重写 game"""

    def game(self):
        print("  在天上玩耍")


class Person:
    """人类,和狗玩"""

    def play_with_dog(self, dog):
        # 不管传普通狗还是哮天犬,都调用 game()
        dog.game()


dog1 = DogPlay()
xtq = XiaoTianDog()
p = Person()
print(f"操作: p.play_with_dog(dog1)   传普通狗")
p.play_with_dog(dog1)
print(f"操作: p.play_with_dog(xtq)  传哮天犬")
p.play_with_dog(xtq)
print(f"结论: 同一个方法 game(),不同对象 → 不同结果 = 多态")


# ============================== 10. 类属性 vs 实例属性 ==============================
# 【讲解】
# 类属性:所有对象共有的属性,定义在类里方法外,用 类名.属性 访问
# 实例属性:每个对象独有的属性,在 __init__ 里用 self.属性 定义
# 区分:
#   类属性   → 该类所有对象共享一份
#   实例属性 → 每个对象各有一份,互不影响
print("\n=== 10. 类属性 vs 实例属性 ===")


class Tools:
    """工具类"""

    count = 0                   # 类属性(所有对象共有)

    def __init__(self, name):
        self.name = name        # 实例属性(每个对象独有)
        Tools.count += 1        # 每创建一个对象,count +1

    @classmethod                # 装饰器:告诉 Python 这是类方法
    def show_count(cls):
        """类方法:用 cls(不是 self),cls 代表类本身"""
        print(f"  工具总数: {cls.count}")


print(f"操作: print(Tools.count)  访问类属性(还没创建对象)")
print(f"结果: {Tools.count}")

t1 = Tools("锤子")
t2 = Tools("斧头")
t3 = Tools("钳子")
print(f"\n操作: 创建 3 个工具对象后")
print(f"结果: Tools.count = {Tools.count}  ← 类属性,所有对象共享")
print(f"      t1.name = {t1.name}  t2.name = {t2.name}  ← 实例属性,各自独有")
print(f"操作: Tools.show_count()  调用类方法")
Tools.show_count()
# 总结：类属性的【数量】实例化后的对象调用都是一个数字，
# 实例属性【名称】每个对象（实例）都有一个不同的值


# ============================== 11. 私有属性和私有方法 ==============================
# 【讲解】
# 私有 = 类外部访问不到,只有类内部能访问(用来保护敏感数据,如密码)
# 定义:名字前加两个下划线 __
#   私有属性: self.__属性名 = 值
#   私有方法: def __方法名(self):
#
# 关键:先分清"类内部"和"类外部"的边界!
#   ┌───────────────────────────────┐
#   │ class Women:                  │
#   │     def __init__(self, ...):  │  ← 缩进在 class 块里的 = 【类内部】
#   │         self.__age            │     这里能用 self.__age / self.__secret()
#   │     def tell_friend(self):    │
#   │         self.__secret()       │
#   └───────────────────────────────┘
#   w = Women("小美", 18)           │  ← 创建对象之后、没缩进在 class 里 = 【类外部】
#   w.__age                         │     这里直接碰私有成员就会报错!
print("\n=== 11. 私有属性和私有方法 ===")


class Women:
    """女人类:年龄是私有的"""

    def __init__(self, name, age):
        self.name = name            # 公有属性(没有下划线)
        self.__age = age            # 私有属性(两个下划线开头)

    def __secret(self):
        """私有方法(两个下划线开头)——只有类内部能调"""
        print(f"      [类内部] 私有方法 __secret 被调用,能拿到 self.__age = {self.__age}")

    def tell_friend(self):
        """公有方法:它本身在类内部,所以可以访问私有成员"""
        print(f"      [类内部] tell_friend 访问私有属性 self.__age = {self.__age}  ← 内部能拿")
        self.__secret()             # 类内部调私有方法:可以!


w = Women("小美", 18)
# ============ 下面从这行开始都是【类外部】(对象 w 创建之后) ============

# ① 类外部访问"公有属性" → 成功
print(f"① 类外部访问公有属性 w.name = {w.name}   ✅ 成功")

# ② 类外部直接访问"私有属性" → 报错 AttributeError
print(f"② 类外部直接访问私有属性 w.__age :")
try:
    print(w.__age)                  # 这行在类外部,会报错
except AttributeError as e:
    print(f"      ❌ 报错 {type(e).__name__}: {e}")

# ③ 类外部直接调用"私有方法" → 报错 AttributeError
print(f"③ 类外部直接调用私有方法 w.__secret() :")
try:
    w.__secret()                    # 这行在类外部,会报错
except AttributeError as e:
    print(f"      ❌ 报错 {type(e).__name__}: {e}")

# ④ 类外部调用"公有方法",由这个方法在【类内部】去访问私有成员 → 成功
print(f"④ 类外部调用公有方法 w.tell_friend()(让它在类内部去碰私有成员):")
w.tell_friend()
print(f"      ✅ 成功!说明私有成员在类内部可以自由访问")

print(f"结论: __开头的成员,类外部直接碰 → 报错;类内部用 self. → 正常")
print(f"      对外只暴露 tell_friend 这种公有方法,把内部细节藏起来 = 封装")


# ============================== 12. 面向对象三大特征总结 ==============================
print("\n=== 12. 面向对象三大特征总结 ===")
print("封装  → 把属性和方法打包进类,隐藏细节,暴露接口")
print("继承  → 子类拥有父类的属性方法,少写重复代码")
print("多态  → 不同对象调同一方法,产生不同结果")


# ---------- 小抄 ----------
# 语法                 |  写法                          |  说明
# --------------------|--------------------------------|--------------------------
# 定义类               |  class 类名:                   |  类名大驼峰
# 设置属性             |  def __init__(self, 参数):     |  创建对象时自动调用
#                     |      self.属性 = 参数           |
# 创建对象(实例化)     |  对象 = 类名(实参)              |
# 调方法(类外)         |  对象.方法()                   |
# 取属性(类外)         |  对象.属性                     |
# 类内访问             |  self.属性 / self.方法()       |  self = 对象自己
# 继承                 |  class 子类(父类):             |  子类拥有父类的一切
# 重写(覆盖)           |  子类定义同名方法              |  完全替代父类
# 重写(扩展)           |  super().方法() + 自己的逻辑    |  父类+子类都执行
# 类属性               |  类名.属性                     |  所有对象共有
# 类方法               |  @classmethod + cls           |  cls 代表类本身
# 私有                 |  __属性名 / __方法名           |  类外部访问不到
#
# 三大特征:
#   封装 → 属性方法打包进类
#   继承 → 子类白拿父类
#   多态 → 同一调用,不同对象不同结果
#
# 记住: 类是图纸(抽象),对象是按图纸造的具体东西(能直接用)
#       self 就是"对象自己",__init__ 是"创建对象时自动调的初始化方法"
