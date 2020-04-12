# -*- coding: utf-8 -*-
class Person:
    def eat(self):
        print("麻辣时我的最爱")

    # 使用装饰器 classmethod 修饰的方法 就是类方法
    @classmethod
    def test(cls):
        # cls 表示当前类
        print('类方法 test')
        print(cls)

    @classmethod
    def create(cls):
        p=cls()
        p.age = 1
        return p

Person.test()
p=Person.create()
print(p)

class Number:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        if self.num2 ==0:
            return None
        return self.num1/ self.num2
    @classmethod
    def pingfanghe(cls,num1,num2):
        # 第一个数
        n1 = Number(num1, num1)
        # 求平方
        n12 = n1.mul()

        # 第二个数
        n2 = Number(num1, num1)
        # 求平方
        n22 = n1.mul()

        # 第三个数
        n3 = Number(n12, n22)

        return n3.add()

he = Number.pingfanghe(3,4)
print(he)