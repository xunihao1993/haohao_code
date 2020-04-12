# -*- coding: utf-8 -*-
class A:
    def aa(self):
        print('哈哈')
    def aa(self):
        print('这是多态')
        return 'aaa'


print(A.__all__)

# def a(x):
#     return x[1]
#
# d={'a':24,'g':52,'l':12,'k':33}
#
# print(d.items())
#
#
# a=dict(sorted(d.items(),key=a))
# print(a)