Markdown 语法速查表 
1 标题与文字格式 
标题 
# 这是 H1 <一级标题> 
## 这是 H2 <二级标题> 
###### 这是 H6 <六级标题> 
文字格式 
**这是文字粗体格式** 
*这是文字斜体格式* 
~~在文字上添加删除线~~ 
2 列表 
无序列表 
* 项目1 
* 项目2 
* 项目3 
有序列表 
1. 项目1 
2. 项目2 
3. 项目3 
   * 项目1 
   * 项目2 
3 其它 
图片 
![图片名称](http://gitcafe.com/image.png) 
链接 
[链接名称](http://gitcafe.com) 
引用 
> 第一行引用文字 
> 第二行引用文字 
水平线 
*** 
代码 
`<hello world>` 
代码块高亮 
```ruby 
  def add(a, b) 
    return a + b 
  end 
``` 
表格 
  表头  | 表头 
  ------------- | ------------- 
 单元格内容  | 单元格内容 
 单元格内容l  | 单元格内容 
 
*** 
*** 
 # Markdown使用

## Markdown标题

    1.使用 = 和 - 标记一级和二级标题
    2.使用 # 号标记
	使用 # 号可表示 1-6 级标题，一级标题对应一个 # 号，二级标题对应两个 # 号，以此类推。

## Markdown 段落

    Markdown 段落没有特殊的格式，直接编写文字就好，段落的换行是使用两个以上空格加上回车。
    当然也可以在段落后面使用一个空行来表示重新开始一个段落。

## 字体
    
    Markdown 可以使用以下几种字体：

```
	*斜体文本*
	_斜体文本_
	**粗体文本**
	__粗体文本__
	***粗斜体文本***
	___粗斜体文本___
```

## 分割线

    你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线：
```
        ***

	* * *

	*****

	- - -

	----------
```

## 删除线

    如果段落上的文字要添加删除线，只需要在文字的两端加上两个波浪线 ~~ 即可，实例如下：

```
~~BAIDU.COM~~ 
```

## 下划线

    下划线可以通过 HTML 的 <u> 标签来实现：

```
	<u>带下划线文本</u>
```

## 脚注

    脚注是对文本的补充说明。

    Markdown 脚注的格式如下:

	[^要注明的文本]
	以下实例演示了脚注的用法：

```
	创建脚注格式类似这样 [^qq]。

	[^qq]: 梦与想
```

## 列表

    Markdown 支持有序列表和无序列表。

    无序列表使用星号(*)、加号(+)或是减号(-)作为列表标记

## 区块

    Markdown 区块引用是在段落开头使用 > 符号 ，然后后面紧跟一个空格符号

## 代码
	
    如果是段落上的一个函数或片段的代码可以用反引号把它包起来（`）

    代码区块使用 4 个空格或者一个制表符（Tab 键）,也可以用 ``` 包裹一段代码，并指定一种语言（也可以不指定）

## 链接

    链接使用方法如下：

	[链接名称](链接地址)

	或者

	<链接地址>

## 图片
    
    ![图片描述（选填）](图片地址)

## 图片&链接

    [![图片描述（选填）](图片地址)](链接地址)

## 表格

    Markdown 制作表格使用 | 来分隔不同的单元格，使用 - 来分隔表头和其他行
    语法格式如下：

```
    |  表头   | 表头  |
    |  ----  | ----  |
    | 单元格  | 单元格 |
    | 单元格  | 单元格 |
```

    对齐方式

    我们可以设置表格的对齐方式：

    -: 设置内容和标题栏居右对齐。
    :- 设置内容和标题栏居左对齐。
    :-: 设置内容和标题栏居中对齐。
## 链接

- [目录](directory.md)

