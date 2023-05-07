# 默认值参数
def fun1(a, b=10):  # b为默认值参数
    print(a, b)


fun1(100)  # 100给a，b用默认值
fun1(20, 30)  # 30将替换默认值10

print('hello', end='\t')  # 默认end是换行
print('hello')


# 个数可变的位置参数，只能定义一个*
def fun2(*args):  # *表示参数个数可变
    print(args)


fun2(10)
fun2(10, 20, 30)


# 个数可变的关键字形参，只能定义一个**
def fun3(**args):  # **表示关键字形参，不知道个数多少
    print(args)


fun3(a=10)
fun3(a=10, b=20, c=30)  # 结果为字典


print('hello', 'world', 'java')  # eg


# *和**可以各有一个，*必须在**之前