# -*- coding UTF-8 -*-
# This is a test function to swap values of two variables.

x = eval(input("请输入变量x："))
y = eval(input("请输入变量y："))
# 加了eval之后，input输入不再是字符串类型
print(type(x))
print(type(y))
# 打印以这种方式输入的变量类型


# 交换x与y指向的对象
def swapvalues(x, y):
    t = x
    x = y
    y = t
    if type(x) == list:
        x.append(4)  # 改变x指向的对象，这个改变在函数外依然有效
    print('函数内x为:',x)
    print('函数内y为:',y)


swapvalues(x, y)
print("函数外x为：",x)
# 函数外，x指向的对象还是输入时的对象，虽然在函数中可能被改变。说明函数中对变量x,y的值改变并不能传递到函数外
print("函数外y为：",y)
