### 1. 一些最重要的 SQL 命令
```ruby 
SELECT * from table where…;

DELETE from table where…;

UPDATE table set column1=value1,column2=value2  where…;

INSERT INTO table values (a,b,c); 或指定列插入 insert into table (column1,c2) values (a,b,c);

CREATE DATABASE - 创建新数据库;

ALTER DATABASE - 修改数据库;

CREATE TABLE - 创建新表
create table student1(
id INT primary key NOT NULL AUTO_INCREMENT,
name varchar(255),
address varchar(255)
);

ALTER TABLE - 变更（改变）数据库表

DROP TABLE - 删除表

CREATE INDEX - 创建索引（搜索键）

DROP INDEX - 删除索引
``` 

INNER JOIN（内连接,或等值连接）：获取两个表中字段匹配关系的记录(多表联查中的内查询 和 `select * from 多张表 where 条件` 结果是一样的)。
```ruby 
Select * from tablea INNER JOIN tableb  ON tablea.cname = tableb.cname;
```
等价于
```ruby
Select * from tablea ，tableb  where tablea.cname = tableb.cname;
```
LEFT JOIN（左连接）：获取左表所有记录，即使右表没有对应匹配的记录。
RIGHT JOIN（右连接）： 与 LEFT JOIN 相反，用于获取右表所有记录，即使左表没有对应匹配的记录。

> 设: a表A条数据，n个字段；b-B条，m字段；c-C条，q条字段
  res: 将得到A*B*C条数据，n+m+q列数的结果集
`select * from tablea , tableb, tablec; //不使用where条件的前提下`
> 找出两门以上成绩不及格的学生的学号
`select number from sc where score < 60 grouby number having count(*) > 2 `
  
### 2. 数据库相关面试题
#### 1. 数据库事务四大特性
原子性，一致性，隔离性，持久性
#### 2. 索引
#### 3. 锁
#### 4. 范式
#### 5. mysql优化
#### 6. 数据库四种隔离状态
#### 7. 服务器架构：
        * 主从复制
        * 读写分离，负载均衡




