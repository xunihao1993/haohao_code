# -*- coding: utf-8 -*-

class Person:
    @classmethod
    def test(cls):
        print("我是类方法")
    def test(self):
        print("我是成员方法")
    @staticmethod
    def test():
        print("我是静态方法")

a=Person.test()
