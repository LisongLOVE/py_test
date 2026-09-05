# 模块的概念(Module)
# - 每一个以 .py 结尾的 Python 代码文件都是一个模块
# - "模块名"同样也是一个"标识符",需要符合标识符的命名规则
# - 在模块中定义的"全局变量"、"函数"、"类"都是提供给外界直接使用的"工具"
# - 模块就好比是工具包,要想使用这个工具包中的工具,就需要先"导入模块"
#
# 导入方式:
# - 方式一: import 导入
# - 方式二: from ... import 导入

# 获取随机数
import random
print(random.randint(1,100))


# 导入层级不同
from random import randint
print(randint(1,1000))

import 函数练习
函数练习.login_test("13488888888","123456")


