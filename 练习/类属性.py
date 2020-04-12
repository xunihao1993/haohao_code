# -*- coding: utf-8 -*-
class Person:
    nation = '中国'
    def __init__(self,name):
        self.name = name
        self.nation = 'china'
# 通过类名访问类属性
print(Person.nation)
p = Person('xiaoming')
# 通过对象也可访问类属性，但是不建议
# 当对象有同名的成员属性时，使用的就是成员属性
print(p.nation)
# 也可以动态添加
Person.hello ='hello'
print(Person.hello)

# 特殊的类属性
# 表示的类名的名字（字符串）
print(Person.__name__)
# 表示父类构成的元组
print(Person.__bases__)
#存储类相关的信息
print(Person.__dict__)