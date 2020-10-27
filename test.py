
from collections import Counter
import numpy as np


def a(apath):
    blist = {}
    with open(apath) as f1:
        for line in f1.readlines():
            lis = line.split( )
            key = lis[0]+lis[1]
            blist.setdefault(key, []).append(float(lis[2]))

    for k,v in blist.items():
        print(k+"成绩平均分："+str(np.mean(v)))
        print(k + "成绩最高分：" + str(np.max(v)))


apath = 'input'
#a(apath)


#1、字典值为列表的构造方法
#
# dic = {}
#
# dic.setdefault(key,[]).append(value)
#
# *********示例如下******
#
# >>dic.setdefault('a',[]).append(1)
#
# >>dic.setdefault('a',[]).append(2)
#
# >>dic
#
# >>{'a': [1, 2]}
#
# 2、字段值为字典的构造方法
#
# dic = {}
#
# dic.setdefault(key,{})[vkey] =vvalue
#
# ***********示例如下*********
#
# >>dic.setdefault('b',{})['f']=1
#
# >>dic.setdefault('b',{})['h']=1
#
# >>dic.setdefault('b',{})['g']=1
#
# >>dic
#
# >>{'b': {'h': 1, 'g': 1, 'f': 1}}
#
# clis = ['e','b','c','a','d','c','a']
#
# res = dict(Counter(clis))
# for k,v in res.items():
#     if v==1:
#         print(k)
#         break
#
# nlis = [1,3,7,3,8,92,42,7,33,40]
# def findindex(s,alist):
#     for i in alist:
#         for j in alist[alist.index(i):]:
#             if i+j==s:
#                 return (alist.index(i),alist.index(j))
#
# print( findindex(36,nlis))
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
#
# z = x.difference(y)

# print(z)
# print(x-y)
# s = "aaa","bbb"+"cc","dd"
# print("aaa","bbb"+"cc","dd")
# print(type(s))

#求最长公共字串
# s1,s2="abcdefg","abfcde"
# m=len(s1)
# n=len(s2)
# f=[[0 for i in range(m+1)] for j in range(n+1)]
# #print(f)
# sub_len=0
# str=""
# for i in range(1,m+1):
#     for j in range(1,n+1):
#         if s1[i-1]==s2[j-1]:
#             f[i][j]=f[i-1][j-1]+1
#             if sub_len<f[i][j]:
#                 sub_len=f[i][j]
#                 str = s1[(i-sub_len):i]
#
# print(sub_len, str)

#将一个列表中的元素组合成最大的数(列表中的元素全是整数)
# lis=[4,6,2,7,0,9,0,7]
#
# def maxnum(lis):
#     str1 = ""
#     lis.sort(reverse=True)
#     for i in lis:
#         str1 = str1+str(i)
#     num=int(str1)
#     return num
#
# print(maxnum(lis))
#
# #快速排序
# def qs(seq):
#     if len(seq)<2:
#         return seq
#     else:
#         base = seq[0]
#         lefts = [i for i in seq[1:] if i<base or i==base ]
#         rignts = [i for i in seq[1:] if i > base]
#         reslist = qs(lefts) + [base] + qs(rignts)
#         return reslist
#
# lis = [4,7,1,5,9,4,2,0]
# print(qs(lis))
#
# #冒泡排序 两两交换，一共拍len-1轮，遇到一轮下来排序没变化的则认为排序完成
# def maopaos(seq):
#     flag=1
#     for x in range(len(seq)-1):
#         for y in range(len(seq)-1-x):
#             if seq[y]>seq[y+1]:
#                 seq[y],seq[y+1]=seq[y+1], seq[y]
#                 flag=0
#         if flag:
#             break
#     return seq
# print(maopaos(lis))
#
# #选择排序法：从后面序列中选择最小和第一个换位置
# def findmin(seq):
#     count=0
#     min = seq[0]
#     minindex =0
#     for item in seq[1:]:
#         count+=1
#         if min> item:
#             min ,item = item, min
#             minindex = count
#     return minindex
#
# def selectsort(seq):
#     for x in range(len(seq)):
#         index=findmin(seq[x:])
#         seq[x], seq[x+index] = seq[x+index], seq[x]
#     return seq
# print(selectsort(lis))
#
# #插入排序法: 把后半部分序列的值按顺序插入到前面中
# def insertsort(seq):
#     for i in range(1,len(seq)):
#         j=i-1
#         key = seq[i]
#         while j>0:
#             if seq[j]>key:
#                 seq[j+1]= seq[j]
#                 seq[j]=key
#             j-=1
#
#     return seq
# print(insertsort(lis))

#冒泡排序：最好的情况是数据本来就有序，复杂度为O(n)；最差的情况是O(N^2),稳定算法。

#选择排序：最好的情况是数据本来就有序，复杂度为O(n)；最差的情况是O(N^2),不稳定算法

#直接插入排序：最好的情况是数据本来就有序，复杂度为O(n)；最差的情况是O(N^2),稳定算法

#希尔排序：最好的情况复杂度为O(n)；最差的情况是O(N^2),但平均复杂度要比直接插入小，不稳定算法

#快速排序：最好的情况复杂度为NlogN,最差的情况是O(N^2),快速排序将不幸退化为冒泡排序;不稳定(比如序列5 3 3 4 3 8 9 10 11，现在中枢元素5和3(第5个元素，下标从1开始计)交换就会把元素3的稳定性打乱)

#子串窗口滑动比较
def strStr(haystack: str, needle: str) -> int:
    if haystack==needle=="":
        return 0
    n = len(needle)
    for i in range(0,len(haystack)):
        if (i+n)<=len(haystack) and haystack[i:i+n] == needle:
            return i
    return -1

print(strStr('mississippi','issip'))

for i in range(3):
    print(i)


# def countAndSay(self, n):
#     s = '1'
#     for i in range(n - 1):  # 第一层，计算好需要的项数，上面已经初始化了第一项
#         s = self.cns(s)  # 不断更新上一项
#     return s


def cns(string):
    res = ''
    string += '#'
    cnt = 1
    for i in range(len(string) - 1):  # 第二层，遍历当前项
        if string[i] == string[i + 1]:  # 计算是否有重复字符
            cnt += 1
            continue
        else:
            res += str(cnt) + string[i]  # 数量和字符返回
            cnt = 1
    return res

print(cns('1'))