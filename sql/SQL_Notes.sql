--Chapter 5: Example Databases and Tables
/*
--5.1: Database for an auto shop business, we have a list of departments, employees,
--customers and customer cars. We are using foreign keys to create relationships between the various tables.
-----------------DDL------------------------------
--Data Definition Language (DDL): to create and modify the structure of the database;
create table [dbo].[Departments] (
    Id INT NOT NULL IDENTITY(1,1),
    Dept_name VARCHAR(25) NOT NULL,
    PRIMARY KEY(Id)
);

create table dbo.Employees (
    Id INT NOT NULL IDENTITY(1,1),
    FName VARCHAR(35) NOT NULL,
    LName VARCHAR(35) NOT NULL,
    PhoneNumber VARCHAR(11),
    ManagerId INT,
    DepartmentId INT NOT NULL,
    Salary INT NOT NULL,
    HireDate DATETIME NOT NULL,
    PRIMARY KEY(Id),
    FOREIGN KEY (ManagerId) REFERENCES Employees(Id),
    FOREIGN KEY (DepartmentId) REFERENCES Departments(Id)
);

CREATE TABLE dbo.Customers (
Id INT NOT NULL IDENTITY(1,1),
FName VARCHAR(35) NOT NULL,
LName VARCHAR(35) NOT NULL,
Email varchar(100) NOT NULL,
PhoneNumber VARCHAR(11),
PreferredContact VARCHAR(5) NOT NULL,
PRIMARY KEY(Id)
);

CREATE TABLE dbo.Cars (
Id INT NOT NULL IDENTITY(1,1),
CustomerId INT NOT NULL,
EmployeeId INT NOT NULL,
Model varchar(50) NOT NULL,
Status varchar(25) NOT NULL,
TotalCost INT NOT NULL,
PRIMARY KEY(Id),
FOREIGN KEY (CustomerId) REFERENCES dbo.Customers(Id),
FOREIGN KEY (EmployeeId) REFERENCES dbo.Employees(Id)
);

-----------------DML------------------------------
--Data Manipulation Language (DML): to perform Read, Insert, Update and Delete operations on the data of
--the database;
use mySQLDatabase;
select * from Departments;

SET IDENTITY_INSERT dbo.Departments ON;
INSERT INTO Departments ([Id], [Dept_name])
VALUES
    (1, 'HR'),
    (2, 'Sales'),
    (3, 'Tech')
;
SET IDENTITY_INSERT dbo.Departments OFF;

--Or to run following query omitting the Id column:
INSERT INTO [dbo].[Departments] ([Dept_name])
VALUES
    ('HR'),
    ('Sales'),
    ('Tech');

select * from dbo.Employees;
set IDENTITY_INSERT dbo.Employees ON;
insert into dbo.Employees
([Id], [FName], [LName], [PhoneNumber], [ManagerId], [DepartmentId], [Salary], [HireDate])
VALUES
(1, 'James', 'Smith', 1234567890, NULL, 1, 1000, '2002-01-01'),
(2, 'John', 'Johnson', 2468101214, '1', 1, 400, '2005-03-23'),
(3, 'Michael', 'Williams', 1357911131, '1', 2, 600, '2009-05-12'),
(4, 'Johnathon', 'Smith', 1212121212, '2', 1, 500, '2016-07-24')
;
set IDENTITY_INSERT dbo.Employees OFF;

select * from dbo.Customers;
set IDENTITY_INSERT dbo.Customers ON;
INSERT INTO dbo.Customers
([Id], [FName], [LName], [Email], [PhoneNumber], [PreferredContact])
VALUES
(1, 'William', 'Jones', 'william.jones@example.com', '3347927472', 'PHONE'),
(2, 'David', 'Miller', 'dmiller@example.net', '2137921892', 'EMAIL'),
(3, 'Richard', 'Davis', 'richard0123@example.com', NULL, 'EMAIL')
;
set IDENTITY_INSERT dbo.Customers OFF;

set IDENTITY_INSERT dbo.Cars ON;
INSERT INTO Cars
([Id], [CustomerId], [EmployeeId], [Model], [Status], [TotalCost])
VALUES
('1', '1', '2', 'Ford F-150', 'READY', '230'),
('2', '1', '2', 'Ford F-150', 'READY', '200'),
('3', '2', '1', 'Ford Mustang', 'WAITING', '100'),
('4', '3', '3', 'Toyota Prius', 'WORKING', '1254')
;
set IDENTITY_INSERT dbo.Cars OFF;

-----------------DCL------------------------------
--Data Control Language (DCL): to control the access of the data stored in the database.

----------------Tools---------------------------
use mySQLDatabase;

SELECT * 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_NAME = 'Departments';

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Departments';

--------------select-----------------------
--1. offset/fetch:
select 
    FullName = emp.Fname + ' ' + emp.LName,
    dep.Dept_name
FROM
    Employees emp
join
    Departments dep
    on dep.Id = emp.DepartmentId
order by FullName
offset 1 rows
fetch first 2 rows only
;

--results without offset/fetch:
--James Smith	HR
--John Johnson	HR
--Michael Williams	Sales
--Johnathon Smith	HR

--results with offset/fetch:
--John Johnson	HR
--Johnathon Smith	HR

--2. CASE
SELECT
    CASE WHEN TotalCost < 200 THEN 0
    ELSE
        CASE WHEN TotalCost >= 200 AND TotalCost <400 THEN TotalCost
        ELSE 3000 
        END
    END threshold
FROM Cars;

--3. group by and having:
--Full table of Cars:
--1	1	2	Ford F-150	READY	230
--2	1	2	Ford F-150	READY	200
--3	2	1	Ford Mustang	WAITING	100
--4	3	3	Toyota Prius	WORKING	1254

select Model, avg(TotalCost) AS avg_cost
from Cars
group by Model
having avg(TotalCost) >100;

--results:
--Ford F-150	215
--Toyota Prius	1254

--Chapter 8: ORDER BY
select * from Employees left join Departments on Employees.DepartmentId = Departments.Id;

--1. Customized sorting order
select FName, LName, Dept_name
from Employees left join Departments on Employees.DepartmentId = Departments.Id
order by
    case Dept_name
        when 'HR'       then 2
        when 'Sales'    then 1
        else            3
    end;

--Results:
--Michael	Williams	Sales
--Johnathon	Smith	HR
--James	Smith	HR
--John	Johnson	HR

--Chapter 10: CASE
--CASE can be used in conjunction with SUM to return a count of only those items matching a pre-defined condition.
--(This is similar to COUNTIF in Excel.)
--The trick is to return binary results indicating matches, so the "1"s returned for matching entries can be summed
--for a count of the total number of matches.

select count(*) as employee_count,
sum(case
    when Dept_name = 'Sales'   then 1
    else    0
    end) as emp_sales_count  
from Employees left join Departments on Employees.DepartmentId = Departments.Id

--results:
--4	1

-- CASE in ORDER BY
select *
from Employees left join Departments on Employees.DepartmentId = Departments.Id
order by (
    case Dept_name 
        when 'HR' then 1
        when 'Sales' then 2
        else    3
    end
)

--Chapter 11: LIKE
select * from Employees where FName like 'John%';
select * from Employees where PhoneNumber like '%121%';

--All records where Fname 3rd character is 'n' from Employees.
SELECT * FROM Employees WHERE FName LIKE '__n%';
--(two underscores are used before 'n' to skip first 2 characters)
--Id FName LName PhoneNumber ManagerId DepartmentId Salary Hire_date
--3 Ronny Smith 2462544026 2 1 600 06-08-2015
--4 Jon Sanchez 2454124602 1 1 400 23-03-2005

--The _ (underscore) character can be used as a wildcard for any single character in a pattern match.
--Find all employees whose Fname start with 'j' and end with 'n' and has exactly 3 characters in Fname.
SELECT * FROM Employees WHERE FName LIKE 'j_n'
--_ (underscore) character can also be used more than once as a wild card to match patterns.
--For example, this pattern would match "jon", "jan", "jen", etc.

SELECT * FROM Employees WHERE FName LIKE '[A-F]%'
SELECT * FROM Employees WHERE Fname LIKE '[lmnop]ary'
SELECT * FROM Employees WHERE Fname LIKE '[^lmnop]ary'

--Chapter 11: IN clause

SELECT *
FROM customers
WHERE id IN (
SELECT DISTINCT customer_id
FROM orders
);

--Chapter 13: Filter results using WHERE and HAVING

SELECT * From ItemSales
WHERE SaleDate BETWEEN '2013-07-11' AND '2013-05-24'

--When comparing datetime values instead of dates, you may need to convert the datetime values into a
--date values, or add or subtract 24 hours to get the correct results.

--WHERE EXISTS: Will select records in TableName that have records matching in TableName1.

SELECT * FROM Employees t WHERE EXISTS (
SELECT 1 FROM Departments t1 where t.DepartmentId = t1.Id and t1.Dept_name in ('Sales'))

--Use HAVING to check for multiple conditions in a group

select DepartmentId
from Employees
where FName like 'John%'
group by DepartmentId
having count(distinct ManagerId) = 2

--Chapter 14: SKIP TAKE (Pagination)
--SQL Server: top n; MySQL: limit n
SELECT top 2 * FROM Employees;

--offset 1, fetch next 2
-- You need to define a subquery in this example using row_number().
-- The WHERE clause does not recognize the alias RN directly because it is defined in the SELECT clause. 
-- SQL Server processes the WHERE clause before the SELECT clause, 
-- so it cannot reference an alias like RN there.
-- Another solution is to use CTE (Common Table Expression)

SELECT *
from
    (select 
        Id,
        DepartmentId,
        row_number() over (order by Id) As RN
    FROM Employees
    ) AS subquery
where 
    RN BETWEEN 2 AND 4;

-- CTE:
WITH CTE AS (
    SELECT Id,
           DepartmentId,
           ROW_NUMBER() OVER (ORDER BY Id) AS RN
    FROM Employees
)
SELECT *
FROM CTE
WHERE RN BETWEEN 2 AND 4;

--Chapter 16: EXPLAIN and DESCRIBE
--But it shows error messages in SQL Server: stored procedure not found.
explain select * from Employees join Departments on Employees.DepartmentId=Departments.Id;
DESCRIBE Customers;

--Chapter 17: EXISTS CLAUSE
select * from Employees where exists (
    select * from Departments where Employees.DepartmentId=Departments.Id
);

--Chapter 18: JOIN
or instance there are two tables as below :
A B
- -
1 3
2 4
3 5
4 6
Note that (1,2) are unique to A, (3,4) are common, and (5,6) are unique to B.
Inner Join
An inner join using either of the equivalent queries gives the intersection of the two tables, i.e. the two rows they
have in common:
select * from a INNER JOIN b on a.a = b.b;
select a.*,b.* from a,b where a.a = b.b;
a | b
--+--
3 | 3
4 | 4
Left outer join
A left outer join will give all rows in A, plus any common rows in B:
select * from a LEFT OUTER JOIN b on a.a = b.b;
a | b
--+-----
1 | null
2 | null
3 | 3
4 | 4
Right outer join
Similarly, a right outer join will give all rows in B, plus any common rows in A:
select * from a RIGHT OUTER JOIN b on a.a = b.b;
a | b
-----+----
3 | 3
4 | 4
null | 5
null | 6
Full outer join
A full outer join will give you the union of A and B, i.e., all the rows in A and all the rows in B. If something in A
doesn't have a corresponding datum in B, then the B portion is null, and vice versa.
select * from a FULL OUTER JOIN b on a.a = b.b;
a | b
-----+-----
1 | null
2 | null
3 | 3
4 | 4
null | 6
null | 5

Cross Join
A Cartesian product of all left with all right rows.
SELECT * FROM A CROSS JOIN B;
X Y
----- -------
Amy Lisa
John Lisa
Lisa Lisa
Marco Lisa
Phil Lisa
Amy Marco
John Marco
Lisa Marco
Marco Marco
Phil Marco
Amy Phil
John Phil
Lisa Phil
Marco Phil
Phil Phil
Amy Tim
John Tim
Lisa Tim
Marco Tim
Phil Tim
Amy Vincent
John Vincent
Lisa Vincent
Marco Vincent
Phil Vincent

*/


