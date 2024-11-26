---
layout: post
title: dbdesign-SQL-intro
date: 2024-11-13 14:27 +0900
description: 
image:
  path: /assets/img/contents/DBDesign/sql_intro.png
  alt: sql_intro
category: [Computer Science, DB Design]
tags: [SQL]
pin: false
math: true
mermaid: true
toc: true
---

> SQL에 대한 Intro 파트입니다. 다음 게시글부터 등장할 내용을 가볍게 훑는 게시글입니다.    
{: .prompt-warning } 

<h2>1. SQL Data Definition</h2>  

CREATE TABLE 명령어를 이용해 새로운 relation을 생성한다.  
이때, 아래 4가지, attributes와 initial constraints를 명시해주어야 한다.  
1. Basic date types(ex. numeric, char, bit string, boolean, ...)  
2. domains(도메인)  
3. attribute constraints와 defaults  
4. key와 referential integrity constraints  

예를 들어 아래와 같은 Relation이 있을 때,  
![example_of_create](/assets/img/contents/DBDesign/Example_of_CREATE.png)  
PROJECT Relation에 대하여 테이블을 생성하고 싶을 때, 다음과 같이 작성한다.  

```sql
CREATE TABLE PROJECT
(
  Pname VARCHAR(15) NOT NULL,
  Pnumber INT NOT NULL,
  Plocation VARCHAR(15) ,
  Dnum INT NOT NULL,
  PRIMARY KEY (Pnumber),
  UNIQUE (Pname),
  FOREIGN KEY (Dnum) REFERENCES DEPARTMENT(Dnumber));
```  
- Pname, Pnumber 등과 같이 Attributes를 명시해준다.  
- VARCHAR(15)와 같이 Basic data type과 domain을 명시한다.  
- NOT NULL: 절대 NULL 값을 가질 수 없도록 하는 조건, column에 반드시 값이 들어가야 한다.    
- UNIQUE: 특정 열에 중복된 값이 입력되는 것을 방지하는 구문으로, 여러 개의 UNIQUE를 정의할 수 있으며, NULL 값이 허용된다.  
- FOREIGN KEY 지정 방법 -> FOREIGN KEY (Attr) REFERENCES RELATION(R_Attr)  



<h2>2. Data Retrieval & Update</h2>  

<h3>SELECT 구문</h3>  

기본적으로 SELECT ... FROM ... WHERE block을 활용해 DB 내의 정보를 retrieve한다.  

```sql
SELECT <attribute list>
FROM <table list>
WHERE <condition>;
```

**예시 1)**  
이름이 `John B. Smith`인 employee의 생일(birth date)와 주소(address)를 Retrieve하는 상황을 가정할 때 다음과 같이 SQL문을 작성할 수 있다.  

```sql
SELECT Bdate, Address
FROM EMPLOYEE
WHERE Fname = 'John' AND Minit = 'B' AND Lname = 'Smith';
```  
와 같이 작성할 수 있다.  
이는 매우 기초적인 SQL문 예제이고, 조금 더 어렵게 들어가보자.  

**예시 2)**  
'Research' 부서에서 일하는 모든 직원들의 이름과 주소를 Retrieve하는 상황을 가정할 때 아래와 같이 SQL문을 작성할 수 있다.  

```sql
SELECT Fname, Lname, Address
FROM EMPLOYEE, DEPARTMENT
WHERE Dname = 'Research' AND Dnumber = Dno;
```  
와 같이 작성할 수 있다.  
`Dnumber = Dno` 조건이 필요한 이유는 간단하다.  
직원의 Attribute에는 Dnum(소속 부서 코드)가 있고, 이는 곧 DEPARTMENT RELATION의 Dname과 연결되기 때문이다.  

**예시 3)**  
Stafford에 위치한 모든 프로젝트에 대해서, project number, controlling department number, department manager의 last name과 주소, Bdate를 리스팅하는 SQL 구문을 짜보자.  

```sql
SELECT Pnum, Dnum, Lname, Address, Bdate
FROM PROJECT, DEPARTMENT, EMPLOYEE
WHERE Dnum = Dnumber AND Mgr_ssn = Ssn AND Plocation = 'Stafford';
```  
와 같이 작성할 수 있다.  

사실 일반적으로 예시 2와 3처럼 SQL문을 작성하지는 않는다.  
다다음 게시글에서 자세히 다루겠지만, Fully qualified attribute name 방법과 Alias를 활용해서 작성하는 것이 일반적이다.  

**예시 2**를 다시 작성해보면, 아래와 같다.  
```sql
SELECT E.Fname, E.Lname, E.Address
FROM EMPLOYEE AS E, DEPARTMENT AS D
WHERE D.Dname = 'Research' AND D.Dnumber = E.Dno;
```  

<h3>UPDATE 쿼리(INSERT, DELETE, UPDATE)</h3>  

1) INSERT  
  하나의 Relation(=table)에 하나의 tuple(=row)을 추가한다.  
2) DELETE  
  하나의 Relation(=table)에 여러 개의 tuple(=row)을 삭제한다.  
3) UPDATE  
  하나 또는 여러 개의 tuple(=row)의 attribute 값을 수정한다.  




<h2>3. </h2>


