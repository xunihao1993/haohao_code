# -*- coding: utf-8 -*-
import os.path
import random
def aaa(a,b):
    global c
    c = 'a'
    def bb(a,b):
        global c
        c = c + 'a' + '1111'
        return c
    return bb(a,b)


# 冒泡排序
def maopao(list1):
    for i in range(0,len(list1)-1):
        for j in range(0,len(list1)-1-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]





# 快速排序 算法步骤：
# 1：从待排序序列中选择一个元素作为参照物。
# 2：遍历待排序序列，比参照物值小的拍在前面，值大的排在后面。
# 3：对每个元素递归排序。

def quick_sort(list1, start, end):
    # 递归的退出条件
    if start >= end:
        return
    # 设置起始元素为要寻找位置的基准元素
    mid = list1[start]
    # left为序列左边的由左向右移动的游标
    left = start
    # right为序列右边的由右向左移动的游标
    right = end
    while left < right:
        # 如果left和right未重合，right指向的元素不比基准元素小，
        # 则right向左移动
        while left < right and list1[right] >= mid:
            right -= 1
        # 将right指向的元素放到left的位置上
        list1[left] = list1[right]
        # 如果left于right未重合，left指向的元素比基准元素小
        # 则left向右移动
        while left < right and list1[left] < mid:
            left += 1
        # 将left指向的元素放到right的位置上
        list1[right] = list1[left]
    # 退出循环后，left与right重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    list1[left] = mid
    # 对基准元素左边的子序列进行快速排序
    quick_sort(list1, start, left-1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(list1, left+1, end)

# 闭包
def bibao(a,b):
    def test1(x):
        return(a*x+b)
    return test1



# 二分查找
# 取数组中间下标中间值进行比较，不断缩小区间，直到左标大于右标退出循环
def findlist():
    a=random.randint(0,100)
    print('需要查找的元素：',a)
    list1=[]
    for i in range(10):
        list1.append(random.randint(0,100))
    print("需要执行操作的数组",list1)
    list1.sort()
    print("对数组进行排序",list1)
    left=0 #左标
    right=len(list1)-1 #右标
    while left < right:
        mid= (right+left)//2
        print('区间为',list1[left:right+1],'查找元素为',a,'节点为',mid,'左标为',left,'右标为',right)
        if a == list1[mid]:
            print('元素已找到区间为',list1[left:right+1])
            break
        elif a>list1[mid]:
            left=mid
        elif a<list1[mid]:
            right=mid





# 股票的最佳时机
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        money = 0
        for i in range(1,len(prices)):
            if prices[i-1]<prices[i]:
                money+=prices[i]-prices[i-1]
        return money

# 题目：快速找出1~100这个列表中缺失的那个元素
def deficiency():
    a=[];
    b=[];
    for i in range (50):
        if i != 88:
            a.append(i)
    for i in range (51):
        b.append(i)
    print("方法一：求和相减",sum(b)-sum(a))
    c=set(b)
    c.add(222)
    print("方法二：求差集",c-set(a))
    print("方法三：求异否",c^set(a))




# 题目：有1，2，3，4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少
def aa():
    i=0;
    for x1 in range(1,5):
        for x2 in range(1,5):
            for x3 in range(1,5):
                if(x1 != x2 and x1 != x3 and x2 != x3):
                    i+=1
                    print(x1,x2,x3)
    print('总共出现次数',i)

# 打开内存较大的文件
def open_file(filename):
    a=[]
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            a.append(line)
    print(a)

# 过滤文件后缀			
def allowd_file(filename):
    return '.'in filename and filename.rsplit('.',1)[1] in ['docx','xls','txt']
			
			
			
if __name__=="__main__":
    # print(os.path.dirname(__file__))
    # print(os.path.dirname(__name__))
    # pass
    # aa()
    # open_file('xx.txt')
    # deficiency()
    # open_file('F:\\桌面备份\\new 3.txt')
    # print(Solution().maxProfit([5,4,3,2,1]))
    # findlist()
    # test=bibao(1,1)
    # li = [23, 94, 2, 21, 56, 6]
    # quick_sort(li, 0, len(li) - 1)
    # print(li)
    # maopao(li)
    # print(li)
    print(aaa(1,2))
