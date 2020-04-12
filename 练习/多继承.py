# -*- coding: utf-8 -*-

class A:
    def eat(self):
        print('eat func of A')

class B:
    def eat(self):
        print('eat func of B')

# 多继承 多个父类使用逗号隔开
class C(B,A):
    def eat(self):
        # 当多个父类拥有相同的方法时，会按照继承时的先后顺序进行选择
        # super().eat()
        # 如果非要使用后面类的方法时，可以明确指定进行调用
        A.eat(self)
c=C()
c.eat()

