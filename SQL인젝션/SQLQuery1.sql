use mytest

select SYSTEM_USER

create table supermarket(
food_no int NULL,
category char(20) NULL,
food_name char(30) NULL,
company char(20) NULL,
price int NULL
)

insert into supermarket
values (1,'����','�ڸ�','��Ʈ',1500)
go
insert into supermarket
values (2,'�����','�����ֽ�','������',1000)
go
insert into supermarket
values (3,'�����','����','����',1000)
go
insert into supermarket
values (4,'����','�ӷ���Ű','ī��',3000)


select * from supermarket

