create database Todo;
use Todo;
create table Todo (id INT NOT NULL AUTO_INCREMENT, Name NVARCHAR(30),Comment NVARCHAR(50),DeadLineDate DATE, Priority NVARCHAR(8), PRIMARY KEY (id));
LOAD DATA LOCAL INFILE '/home/sashavoin5/Downloads/TodoLex.tsv'
INTO TABLE Todo
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(Name,Comment,DeadLineDate,Priority);
insert into Todo (Name,Comment,DeadLineDate,Priority) VALUES ('Купить на день рождения пиццу','Можно взять также напитки','2023-06-03','HDGCHG');
DELETE FROM Todo WHERE ID =5 ;


SELECT Name,Comment, DeadLineDate,Priority INTO OUTFILE '/var/lib/mysql/TodoLex1.tsv' FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' FROM Todo;

SELECT Name,Comment, DeadLineDate,Priority INTO OUTFILE '/var/lib/mysql/TodoLex.json' FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' FROM Todo;


