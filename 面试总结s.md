1. 冒泡排序
```ruby 
def maopao1(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-i-1):
            if lis[j]>lis[j+1]:
                lis[j+1], lis[j] = lis[j], lis[j+1]
    return lis
``` 
1.1 二分查找
```ruby 
def search(nums, target):
    left,right=0,len(nums)-1
    while(left<=right):
        p=left+int((right-left)/2)
        if nums[p]<target:
            left=p+1
        elif nums[p]>target:
            right=p-1
        elif nums[p]==target:
            return p
        else:
            return -1
    return -1
print(search([-1,0,3,5,9,12],12))
``` 
2. 链表
```ruby 
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

n1=ListNode(1)
n2=ListNode(2,n1)
n3=ListNode(3,n2)
n4=ListNode(4,n3)
n5=ListNode(5,n4)

#2.1 链表查中间节点
def midnode(l:ListNode):
    p1=p2=l
    while p2.next and p2.next.next:
        p1=p1.next
        p2=p2.next.next
    return p1

print(midnode(n5).val)

#2.2 判断链表是否带环
def iscir(l:ListNode):
    p1=p2=l
    while p2 and p2.next:
        p1=p1.next
        p2=p2.next.next
        if p1==p2:
            return True
    return False
```
3. 有一个json，{'a':'aa', 'b':'bb', 'c':{'d':'dd','e':'ee','f':{'g':'gg','h':'hh'}}}，找到h这个key对应的value
```ruby 
def get_value(dic, target):
    res=""
    for k,v in dic.items():
        if k==str(target):
            res = dic[target]
            break
        elif type(v) is type({}):
            res = get_value(v,target)
    return res
js={'a':'aa', 'b':'bb', 'c':{'d':'dd','e':'ee','f':{'g':'gg','h':'hh'}}}
print(get_value(js,'h'))
``` 
`types模块，dir(types), types.DictType`

4. 一个英文文件，计算文件中出现次数最多的前三个单词
```ruby 
import re
def times(lis):
    dic = {}
    for s in lis:
        dic.setdefault(s,0)
        dic[s]+=1
    return dic
def findwords(fp):
    s=""
    with open(fp,'r') as f:
        for line in f:
            s+=line
    lis=re.findall(r'[a-zA-Z]+',s)
    dic=times(lis)
    res=sorted(dic.items(),key=lambda x:x[1], reverse=True)
    return res[:3]
filepath="./word.txt"
print(findwords(filepath))
```
  * 打开文件：`**with open('filepath','r') as f:**`
    直接打开文件后读，最后调用f.close():读取文件不存在或者异常时，直接出现错误，close无法执行
    而with语句会自动关闭文件，即使出现异常
    也可以try--except--finally实现：
    ```ruby 
    f = open(filepath,'r')
    try:
        s = f.read()
    except:
        ...
    finally:
        f.colse()

    读取文件内容方法：
    `read() #一次性读取文件全部内容，返回个str`
    `readline() #读取文件一行内容`
    `readlines() 按行读取文件所有内容，返回一个列表，列表元素为一行`
    `readable() 打开的文件是否可读，返回值bool`
    ```
  * re模块
    ```ruby
    s=re.match( r'(.*) are (.*?) .*', "Cats are smarter than dogs").group()  #返回被 RE 匹配的字符串。
    s=re.match( r'(.*) are (.*?) .*', "Cats are smarter than dogs").groups() #返回被 RE 匹配的字符串子串元组
    s=re.search( r'(.*) are (.*?) .*', "Cats are smarter than dogs").span()  #返回一个元组包含匹配 (开始,结束) 的位置
    #start() 返回匹配开始的位置
    #end() 返回匹配结束的位置
    lis = re.findall(r'\d+','runoob 123 google 456')  #返回被 RE 匹配的字符串子串组成的列表，如果没有找到匹配的，则返回空列表。
    it = re.finditer(r"\d+","12a32bc43jf3")  #在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
    ```
    正则表达式实例
    ```ruby
    [0-9] 或 \d ：匹配任何数字，类似于 [0123456789]
    [^0-9] 或 \D ：匹配除了数字外的字符
    [a-zA-Z0-9] 或 \w ：匹配任何字母及数字
    [^aeiou]	除了aeiou字母以外的所有字符
    \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
    \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
    ^	匹配字符串的开头
    $	匹配字符串的末尾。
    .	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
    ```
6. 输入字符串“123+23456”，整型间的加操作，求结果，追问如果里面的数值非常大超过了int的范围怎么办
7. 输入一个整形数组，数组里有正数也有负数。数组中连续的一个或多个整数组成一个子数组，每个子数组都有一个和。求所有子数组的和的最大值，考虑时间复杂度
8. 输入整形数组，对数组进行排序，左侧放奇数，右侧放偶数
```ruby
def customsort(lis):
    l,leftl,rightl=[],[],[]
    for i in lis:
        if i%2 == 1:
            leftl.append(i)
        else:
            rightl.append(i)
    l=leftl+rightl
    return l
print(customsort([3,6,1,6,87,9,2,4,0,-3,-10]))
```
9. 一个数组[“flower ”，“flow ”，“flight ”]，找出三个字符串的共有子串fl‘
10. 子串
```ruby
#(1). 求字符串中的所有子串
def allsubs(str):
    res = []
    for i in range(1,len(str)):
        for j in range(0,len(str)):
            if str[j:j+i] not in res:
                res.append(str[j:j+i])
    return res
print(allsubs('abcd'))
#(2). 一个字符串，找到不重复字符的最大子串的长度s='abcdafedsabc'
def maxsub(s):
    sub=sub1=""
    n=0
    for c in s:
        if c in sub:
            i = sub.index(c)
            sub = sub[i + 1:]
        sub+=c
        if n<len(sub):
            n=len(sub)
            sub1=sub
    return (sub1,n)
s='abcdafedsabc'
print(maxsub(s))
#(3). 最长重复子串
#(4). 单字符最长重复子串
#(5). 最长回文串
#(6). 最长回文子序列
#(7). 求2个字符串的最长公共子串
def ggsubs(str1,str2):
    f=[[0 for x in range(len(str2)+1)] for j in range(len(str1)+1)]
    maxsub=''
    maxlen=0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i]==str2[j]:
                f[i+1][j+1]=f[i][j]+1
            if maxlen<f[i+1][j+1]:
                maxlen=f[i+1][j+1]
                maxsub=str1[i+1-maxlen:i+1]
    return maxsub
print(ggsubs('abcdefg','defgabcd'))
#(8). 最长公共子序列
#(9). 最长定差子序列,

```
11. 领红包：
  > 入参：金额、人数
    输出：输出所有金额
    逻辑：
    1.所有人抢到金额之和等于红包金额，不能超过，也不能少于。
    2.每个人至少抢到一分钱。
    #3.要保证所有人抢到金额的几率相等。   
```ruby
#领红包，不考虑概率
import random
def redpackage(money,num):
m=money=money*100
everyperson=0
res=[]
money = money-num
for n in range(num-1):
    everyperson = random.randint(1, money)
    res.append(everyperson)
    money = money - everyperson
last = m-sum(res)
res.append(last)
res = [x/100 for x in res]
return res
print(redpackage(100,6))
```

