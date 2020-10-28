1. 冒泡排序
```ruby 
def maopao1(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-i-1):
            if lis[j]>lis[j+1]:
                lis[j+1], lis[j] = lis[j], lis[j+1]
    return lis
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
