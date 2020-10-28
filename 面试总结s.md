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
