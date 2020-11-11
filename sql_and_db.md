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
alter table tbltest add column_name int [after column_name1]; #[在column_name1列后]添加一列 column_name
alter table taltest drop column_name; #删除字段
alter table tbltest modify column_name char(10);修改字段类型
alter table tbltest change column_old column_new type;修改字段名和类型或者只修改字段类型

DROP TABLE - 删除表

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


```ruby
DROP TABLE IF EXISTS `tblCourseAttend`;
CREATE TABLE `tblCourseAttend` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `uid` bigint(20) unsigned NOT NULL COMMENT '用户id',
  `courseId` bigint(20) unsigned NOT NULL COMMENT '课程id',
  `classId` varchar(50) NOT NULL DEFAULT '' COMMENT '班级id，预留',
  `sectionId` bigint(20) unsigned NOT NULL COMMENT '章节id',
  `sectionNum` int(10) unsigned NOT NULL COMMENT '章节顺序id',
  `attendTime` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '章节上课时间',
  `uploadId` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '作业上传id',
  `uploadTime` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '作业上传时间',
  `updateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `ext` varchar(1000) NOT NULL DEFAULT '[]' COMMENT '其他扩展信息',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniqUidSection` (`uid`,`courseId`,`classId`,`sectionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户上课记录表';

LOCK TABLES `tblCourseAttend` WRITE;
/*!40000 ALTER TABLE `tblCourseAttend` DISABLE KEYS */;

INSERT INTO `tblCourseAttend` (`id`, `uid`, `courseId`, `classId`, `sectionId`, `sectionNum`, `attendTime`, `uploadId`, `uploadTime`, `updateTime`, `ext`)
VALUES
	(1,1000000000,1,'',1,1,1581423621,0,0,'2020-02-11 20:19:20','[]'),
	(2,2257286384,1,'',1,1,1581506546,4,1581506546,'2020-02-12 19:21:24','[]');

/*!40000 ALTER TABLE `tblCourseAttend` ENABLE KEYS */;
UNLOCK TABLES;
```
  
### 2. 数据库相关面试题
#### 1. 数据库事务四大特性
mysql事务：  
MySQL 中只有使用了 Innodb 数据库引擎的数据库或表才支持事务；  
事务处理可以用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行。事务用来管理 insert,update,delete 语句  
原子性 - 一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。  
一致性 - 在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。  
隔离性 - 数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）  
持久性 - 事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。
###### 事务测试
```ruby
mysql> use RUNOOB;
Database changed
mysql> CREATE TABLE runoob_transaction_test( id int(5)) engine=innodb;  # 创建数据表
Query OK, 0 rows affected (0.04 sec)
 
mysql> select * from runoob_transaction_test;
Empty set (0.01 sec)
 
mysql> begin;  # 开始事务
Query OK, 0 rows affected (0.00 sec)
 
mysql> insert into runoob_transaction_test value(5);
Query OK, 1 rows affected (0.01 sec)
 
mysql> insert into runoob_transaction_test value(6);
Query OK, 1 rows affected (0.00 sec)
 
mysql> commit; # 提交事务
Query OK, 0 rows affected (0.01 sec)
 
mysql>  select * from runoob_transaction_test;
+------+
| id   |
+------+
| 5    |
| 6    |
+------+
2 rows in set (0.01 sec)
 
mysql> begin;    # 开始事务
Query OK, 0 rows affected (0.00 sec)
 
mysql>  insert into runoob_transaction_test values(7);
Query OK, 1 rows affected (0.00 sec)
 
mysql> rollback;   # 回滚
Query OK, 0 rows affected (0.00 sec)
 
mysql>   select * from runoob_transaction_test;   # 因为回滚所以数据没有插入
+------+
| id   |
+------+
| 5    |
| 6    |
+------+
2 rows in set (0.01 sec)
 
mysql>

#PHP中使用事务实例
<?php
$dbhost = 'localhost';  // mysql服务器主机地址
$dbuser = 'root';            // mysql用户名
$dbpass = '123456';          // mysql用户名密码
$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
    die('连接失败: ' . mysqli_error($conn));
}
// 设置编码，防止中文乱码
mysqli_query($conn, "set names utf8");
mysqli_select_db( $conn, 'RUNOOB' );
mysqli_query($conn, "SET AUTOCOMMIT=0"); // 设置为不自动提交，因为MYSQL默认立即执行
mysqli_begin_transaction($conn);            // 开始事务定义
 
if(!mysqli_query($conn, "insert into runoob_transaction_test (id) values(8)"))
{
    mysqli_query($conn, "ROLLBACK");     // 判断当执行失败时回滚
}
 
if(!mysqli_query($conn, "insert into runoob_transaction_test (id) values(9)"))
{
    mysqli_query($conn, "ROLLBACK");      // 判断执行失败时回滚
}
mysqli_commit($conn);            //执行事务
mysqli_close($conn);
?>
```
#### 2. 索引
#### 3. 锁
#### 4. 范式
#### 5. mysql优化
#### 6. 数据库四种隔离状态
#### 7. 服务器架构：
        * 主从复制
        * 读写分离，负载均衡
#### 8. 服务器架构      




