create database pdbc;

use pdbc;

create table std ( 
	id int,
	name varchar(20),
	gpa decimal(5,2)
);

insert into std values(2,"sendhil",7.8),
					  (3,"guna",7.5),
                      (4,"velu",6.7);
                      
delete from std where id = 5;

select * from std;