# -*- coding: utf-8 -*-

class Person:
    def __init__(self,name):
        self.name=name

    def __setattr__(self, key, value):
        # 当设置对象成员属性的时候，系统会自动调用
        print(key,value)

    def __getattr__(self,item):
        #访问不存在的属性时，系统会自动调用
        print(item)
        return 123
    def __delattr__(self,item):
        # 当销毁对象的成员属性时，系统会自动调用
        print(item)



# xiaoming = Person('小明')
xiaoming = Person()
# # 每个对象都有一个成员属性：__dict__
# # 用于存放对象的属性，包括动态添加的
# print(xiaoming.__dict__)
# xiaoming.name='小明'
# print(xiaoming.name)
# print(xiaoming.__dict__)
xiaoming.age=18

del xiaoming.age
