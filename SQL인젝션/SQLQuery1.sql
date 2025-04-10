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
values (1,'과일','자몽','마트',1500)
go
insert into supermarket
values (2,'음료수','망고주스','편의점',1000)
go
insert into supermarket
values (3,'음료수','식혜','시장',1000)
go
insert into supermarket
values (4,'과자','머랭쿠키','카페',3000)


select * from supermarket

