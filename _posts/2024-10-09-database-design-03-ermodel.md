---
layout: post
title: 'Database Design 03: ERmodel'
date: 2024-10-09 16:17 +0900
description: 
image:
  path: /assets/img/contents/ER_model.png
  alt: example of ER Modeling
category: [Computer Science, DB Design]
tags: []
pin: false
math: true
mermaid: true
toc: true
---

> 데이터베이스설계 시리즈는 ERmodel부터 포스팅할 예정입니다. 앞부분은 다소 지엽적인, 상식적인, 암기성 내용들이 주를 이루고 있기 때문에 시간이 날 때 포스팅할 예정입니다.  
{: .prompt-warning } 

<h2>1. Database Design Process</h2>  

<h3>Requirements Collection & Analysis</h3>
DB Designer는 유저의 니즈를 이해하기 위해 유저 관점을 인터뷰한다.  
데이터베이스를 위한 data requirements를 수집하고 분석한다.  
유저의 디테일한 requirements의 집합이 결과물로 산출된다.  

<h3>Functional Analysis</h3>  
functional requirements(기능적 요구사항)를 명시한다.  
이 과정에서 DB에 사용자 정의 연산들이 적용된다. 

<h3>Conceptual Modeling</h3>  
데이터 요구사항을 수집하고 분석하는 과정이 끝나면, ER model 개념에 기반한 모델링을 사용해서 conceptual schema를 작성한다.  

**[COMPANY 예시]**  
1. COMPANY의 employees, departments, project를 파악한다.
2. DB Designer는 'miniworld'(=COMPANY)의 description(설명)을 제공한다.  
   - 회사(COMPANY)는 부서(DEPARTMENT)로 구성되어 있다
   - 부서(DEPARTMENT)는 여러 개의 프로젝트(PROJECT)를 관리한다.
   - 직원(EMPLOYEE)는 DB에 저장된다. (이름, 주소, 봉급, 성별, ... 의 특징을 가지고 있다.)  
   - DB는 보험 목적으로 각 직원들의 부양가족(DEPENDENT)를 파악한다. (이름, 성별, 생년월일 등에 대한 특징을 지니고 있다.)

<h2>2. Entity & Attribute</h2>  
> ER Model이란 Entity-Relationship Model의 약자이다. 즉, Entity와 그 관계에 주목해서 데이터베이스를 모델링하는 방법론이다. ER Model은 데이터를 Entity, Relationship, Attribute로 설명한다.  

<h3>Entity</h3>  
Things or Object 라고 설명한다.  
즉, 현실세계에서 독립적으로 존재하는 무언가를 Entity로 설명한다.  
예를 들어, person, car, student와 같이 물리적으로 존재하거나, company, project와 같이 개념적으로 존재하는 object를 말한다.  

<h3>Attributes</h3>  
Entity가 가지는, Entity를 설명하는 특정한 속성들이다.  
예를 들어, Person이라는 사람에 대한 attributes는 나이, 이름, 성별, 집주소, 핸드폰 번호 등이 될 수 있다.  

<h3>Types of Attributes</h3>  
> attributes의 몇 가지 종ㄹ유가 있다. 알아보도록 하자.  

1. Composite Attributes VS. Simple Attributes  
  - Composite Attributes  
    더 작은 subpart로 나눌 수 있는 attributes를 말한다.  
    예를 들어, `주소`라는 attribute가 있다고 했을 때, 시/군/구/동호수 처럼 더 자긍ㄴ 부분으로 쪼갤 수 있다.  
  - Simple Attributes
    더 이상 나눌 수 없는 attribute를 말한다. 주소에서 나뉘어진 아파트 동호수나 도시명 등을 의미한다.  

2. Single-valued Attributes VS. Multivalued Attributes  
  - Single-valued Attributes  
    무조건 값이 하나를 가지는 attribute를 말한다.  
    예를 들어, 성별은 남성 또는 여성 하나만을 가질 수 있다. 나이는 24, 32처럼 한 가지 값만 가질 수 있다.  
  - Multivalued Attributes  
    값을 여러 개 가질 수 있는 attribute를 말한다.  
    예를 들어, 핸드폰 번호나 대학 학위 등은 2개 이상 가질 수 있기에 Multivalued로 분류한다.  

3. Stored Attributes VS. Derived Attributes  
  - Stored Attributes  
    실제로 DB에 저장된 attribute를 의미한다. (ex. birth date)
  - Derived Attributes  
    실제로 DB에 저장되진 않았지만 유도 가능한 attribute를 의미한다.  
    예를 들어, birth date에서 age를 유추할 수 있기 때문에 age를 derived로 분류한다.  

<h3>Entity Types & Sets</h3>  
Entity Type이란 같은 attributes로 구성된 집합을 가지고 있는 entity들의 집합이다.  
예를 들어, 직원 A, 직원 B, 직원 C가 이름, 나이, 월급 등에 대한 attribute를 가지고 있다고 할 때, Entity Type Name을 EMPLOYEE로 정한 Entity type을 정의할 수 있다.  
Entity Set은 EMPLOYEE에 속한 직원 A, B, C와 attributes로 묶인 집합을 말한다.  

<h3>Key attributes</h3>  
- Key Attributes란 다른 개별 entity와 구별되는 값을 가진 attribute를 말한다.  
다른 Entity들과 서로 중복되지 않는, 고유한 값을 가진 attribute를 말한다.  
예를 들어, `STUDENT`라는 Entity Type이 있고, `s1, s2, ..., sN`와 같이 Entity들이 존재할 때, `s1, s2, ..., sN` 간에 중복되지 않는 attribute, 즉, entity마다 고유한 값을 가지는 attribute를 key attribute라고 한다. 위에서 예로 들면, '학번'과 같은 attribute가 key attribute가 될 수 있다.  
- 복합적인 attributes의 조합은 key의 역할을 수행한다. 즉, 여러 개의 attributes의 조합으로 entity를 구별할 수 있다는 의미이다.  
- key attribute는 Entity Type 당 2개 이상을 가질 수도 있다.  

<h2>3. Relationship</h2>  

<h3>Relationship Types & Sets</h3>  
Relationship Type이란 참여하는 Entity Types 간의 관계에 대한 집합으로서 정의한다.  
Relationship Set이란 relationship instances들의 집합이다.  
이해하기 힘들 순 있는데, 예를 들어 보자.  
EMPLOYEE라는 Entity Type에 `e1, e2, e3, ...`라는 entity들이 존재하고,  
DEPARTMENT라는 Entity Type에 `d1, d2, d3, ...`라는 entity들이 존재한다고 가정해보자.  
`e1 직원은 d1이라는 부서에서 일한다`라는 entity와 entity간의 관계(relationship)가 하나 성립되었다고 하자.(relationship instance인 r1이 생성)  
e2는 d2, e3는 d3에서 일한다고 하고, 모든 직원들이 특정한 부서에서 일한다면, X직원이 Y부서에서 일하는 것과 관련된 relationship instance는 여러 개 생성될 것이다.  
이러한 relationship instance를 하나의 집합으로 묶어 표현한 것이 Relationship Set이고 Relationship Set의 이름은 WROKS_FOR이라고 지을 수 있다.  

<h3>Relationship Degree</h3>  
Relationship Degree란 몇 개의 Entity Type들이 해당 Relationship에 참여하는지를 나타낸 것으로, 어떤 것이든 될 수 있다. (Binary, Ternary, ...)  

<h3>Role name & Recursive relationship</h3>  

1. Role Name  
    관계에 참여하는 entity가 각 relationship instance에서 어떠한 역할을 하는지 표시하고 이름 붙이는 것이다.  
    위에서 제시한 EMPLOYEE, DEPARTMENT, WORK_FOR를 예시로 들 때,  
    EMPLOYEE라는 entity type에 속한 entity는 worker라는 role을 가지고 있고,  
    DEPARTMENT라는 entity type에 속한 entity는 Employer라는 role을 가지고 있다고 설명할 수 있다.  

2. Recursive Relationship  
    자기참조관계라고도 한다.  
    하나의 entity가 다른 entity가 아닌 자기 자신과 관계를 맺는 relationship 유형이다.  
    다른 말로, 동일한 entity type이 하나의 relationship type에 대해 두 번 이상 참여하는 관계를 말한다.  
    이때, role name을 명시하는 것이 중요하다.  

<h2>4. Relationship Types: Constraints & Attributes</h2>  
<h2>5. Weak Entity Types</h2>  
<h2>6. Refining Conceptual Design</h2>  
<h2>7. ER Diagram</h2>  