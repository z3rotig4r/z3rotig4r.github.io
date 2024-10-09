---
layout: post
title: "Concepts of Programming Languages 01: Preliminaries"
date: 2024-10-08 15:00 +0900
description: 
image:
  path: /assets/img/contents/pl_preview.jpg
  alt: concepts of programming languages
category: [Computer Science, Concepts of Programming Languages]
tags: [Programming Languages, Criteria]
pin: false
math: true
mermaid: true
toc: true
---

<h2>1. Reasons for Studying Concepts of PLs</h2>  
1. 아이디어를 표현하는 능력을 기르기 위해서
2. 적절한 프로그래밍 언어 사용 배경지식을 기르기 위해서
3. 새로운 언어를 배우는 능력을 기르기 위해서
4. 구현의 중요성을 이해하기 위해서
5. 이미 알려진 언어의 사용을 이해하기 위해서
6. 전반적인 연산 향상을 위해서  

-> 지엽적인 내용, 넘어가도록 하자.  

<h2>2. Programming Domains</h2>  
1. 과학 (FORTRAN 같은 언어)
2. 사무 (COBOL 같은 언어)
3. AI (LISP, PROLOG 같은 언어)
4. 시스템 프로그래밍 (C, ...)
5. WEB S/W (perl, JS, ...)

-> 잘 알려진 내용이다. 넘어가도록 하자.  

<h2>3. Language Evaluation Criteia</h2>  
사실상 Chapter 1의 핵심이다.  
암기하도록 하자.  

<h3>Readability(가독성)</h3>  
> 프로그램 작성 후 얼마나 코드를 얼마나 쉽게 이해할 수 있는지를 평가하는 항목이다.  
> 예를 들어, 코드 리팩토링을 할 때, 한 눈에 들어오는 코드여야 쉽게 구조를 파악할 수 있다.  

1) Overall Simplicity (전반적 단순성)  
  - 언어에서 기본적으로 제공하는 기능이 많을 수록 복잡하다. 따라서, 적은 수의 elementary components를 제공하는 것이 Readability를 높일 수 있다.  
  - Feature multiplicity (특정 operation을 제공하는 방식이 여러 가지인 경우를 의미한다. 이러한 경우 Simplicity를 해친다고 본다.)  
  - Operator overloading (연산자 오버로딩, 예를 들어 '+'연산자가 수의 덧셈 뿐만 아니라, string이나 array의 concat을 담당하고 있는 경우, Simplicity를 해친다.)  
  - Assembly Language처럼 너무 단순해도 가독성을 해친다.  
  
2) Orthogonality (직교성이라 번역하고, 그냥 영어로 저렇게 부르자!)  
  - 여러 규칙이 서로 독립적인 특성을 지니는 경우 직교성이 높다고 표현한다.
  - 동일한 작업을 수행하는 기능들이 많다면, 직교성이 낮다.
  - 동일한 기능을 "하나의 명령어"를 이용해 수행한다면 직교성이 높다.
  - 직교성이 좋은 디자인은 예외가 적은 언어이다.
  - 직교성이 높을수록 좋다.
  - 다음은 대표적으로 직교성이 나쁜 예시 코드이다. (포인트형 변수가 왔을 때, 주소를 표현하기 위해서 자료형의 크기만큼 곱한 뒤 연산을 해야한다.)
```c
#include <stdio.h>
int main() {
  int *a = 10;
  int b = 10;
  printf("%d", a + b);
}
```  

3) Control Statements(제어문)
  - 일반적인 글을 읽는 때처럼 위에서부터 아래의 흐름으로 진행해야 한다.  
  - 이를 컨트롤하기 위해선 적절한 제어문이 필요하다.
  - 예를 들어, C언어의 GOTO 구문은 계속에서 코드의 흐름이 위아래로 반복하게 만드므로 Readability를 떨어뜨린다.  
  
4) Data Types & Structures
  - 가독성을 위해 적절한 데이터 타입과 자료구조를 제공해야 한다.
  - 이에 반하는(Opposite) 예시 중 C언어의 boolean 미지원이 있다. (예를 들어, sum_is_too_big = 1이라고 참, 거짓을 대체 표현했을 때, 0이 false인지 1이 false인지 모르며, 0 또는 1 이외에 다른 값도 들어갈 수 있다는 단점이 있다.)  
  
5) Syntax Consideration(구문설계)
  - 문법과 키워드를 만들 때, 그 이름에 맞는 기능이 직관적으로 이해되도록 만들어야 한다.
  - Identifier forms (ex. SUM_OF_SQUARE)
  - Special words (키워드 지원)
  ```vbscript
  If () Then
  Else
  End if.
  ```
  End if 쓰는 게 IF문의 종료를 알려주므로 가독성이 더 좋은 예시이다.
  - Form & Meaning(어떤 언어에서는 동일한 GO TO 문이여도 매개변수의 순서에 따라 달라지는 경우가 있다.)  
  
<h3>Writability(작성력)</h3>
> 얼마나 프로그래밍 언어가 프로그램을 작성하기 쉽게 쓰여졌는지를 판단하는 척도이다.  

1) Simplicity & Orthogonality  
  - primitives(기본 제공 기능의 의미로 해석하면 편하다.)를 많이 제공하는 것보다 적은 primitive를 제공하고, 높은 직교성을 제공해야 한다.  
  => Readability의 조건이었던, Simplicity와 Orthogonality를 만족시키면 Writability도 올라간다!  

2) Support for Abstraction
  - 복잡한 구조나 연산을 정의하고 사용할 때, 세부적인 디테일을 무시하고 사용할 수 있도록 만드는 것이 Abstraction(추상화)이며, 이를 제공해야 Writability가 좋아진다. 왜냐면, 내부의 어려운 로직에 매몰되지 않고 보다 쉬운 코드로 프로그램을 작성할 수 있기 때문이다. 
  -  Process를 Abstraction하는 방법으로 subprogram을 사용 (예: 함수)  
  -  Data Abstraction 방법으로 Record type을 사용  
  
3) Expressivity
  - 표현력이 좋을수록 작성력이 좋다.  
  - 예를 들어, `count++` 이 `count = count + 1` 보다 코드도 더 짧고 편리해서 작성력이 더 높다고 평가할 수 있다.  

<h3>Reliability(신뢰성)</h3>
> 말 그대로, 해당 프로그래밍 언어가 제공하는 기능이 항상 일관되며, 기대한 기능을 수행한다는 믿음을 주는 것이다.  

1) Type Checking  
  - 두 변수 간 혹은 하나의 변수와 상수 간에 type compatibility를 테스트하는 것이다.  
  - 일반적으로 컴파일 시간에 type check를 하는 것이 비용적인 측면에서 바람직하다.
  - C에서는 타입 검사가 없는 반면, Pascal에서는 런타임 type check이긴 하지만, subscript range checking을 한다.  
  
2) Exception Handling  
  - run-time 에러를 잡아내는 능력은 적절한 reliability를 높여준다.  

3) Aliasing  
  - 동일한 메모리 셀에 대해서 다른 참조 방법 또는 이름을 제공하는 것을 별칭이라고 한다.
  - 별칭 존재는 신뢰성에 악영향을 준다.  

4) Readability & Writability  
  - 당연하게도 가독성이 높고, 작성력이 높은 언어는 신뢰성 또한 높다.  

<h3>Cost</h3>  
- 프로그래머를 육성하는 비용 (극단적인 예시: C++, 진짜 어려움;;)
- 코드 작성 비용 (극단적인 예시: Assembly Language, 몇 천 줄 써야 되니까)
- 프로그램 컴파일 비용
- 프로그램 실행 비용 (Compiled Language vs. Interpreter Languages)
- 프로그램 유지 비용

<h2>4. Influences on Language Design</h2>  
1) 컴퓨터 구조
  - von-Neumann Computer => Imperative Languages  
    명령형 언어는 하드웨어 구조와 연산을 높은 수준의 추상화를 통해 구축한 언어이다.  
    변수는 메모리 셀과,  
    할당은 fetching & storing,  
    표현은 수학적 연산,  
    루프는 조건에 의한 jump로 구현한다.  
    가장 큰 단점은 메모리와 CPU 간의 bottleneck(병목 현상)이다. => 이는 Cache로 해결하는 걸 컴퓨터 구조 시간에 배울 것이다.  

  - non von-Neumann Computer => Declarative Languages  
    선언형 언어는 비폰노이만 구조의 컴퓨터에서 사용한다.  
    할당도 없고, statements도 없고, 반복도 없다.  
    프로그램의 효율적인 실행을 추구하는 함수형 언어이다. 하지만, 비폰노이만 구조 구현의 한계로 쓰이지 않고 있다.  

2) 프로그래밍 방법론
  - Structured Programming
  - Data-Oriented Programming
  - Object-Oriented Programming
  - Process-Oriented Programming

3) 언어 설계 Trade-offs 
=> 신뢰성과 실행 비용은 상충관계
=> 간결한 표현(수학적으로 잘 짜여진 표현)과 이해하기 쉬운 표현은 상충관계
=> 유연성과 안전성은 상충관계
=> 유연성과 효율성은 상충관계

<h2>5. Implementation Methods</h2>
> 기계어로 컴퓨터가 이해할 수 있도록 번역해야 한다.  

1) 컴파일러 - 기계어로 번역을 미리 해놓고 컴퓨터에서 바로 실행하도록 만든다. 빠른 프로그램 실행이 가능하다.  

2) 인터프리터 - 특별한 컴파일 과정없이, 실행 시에 코드를 한 줄씩 읽어가며, 기계어로 번역한다. 디버깅이 용이하고 구현이 더 간단하지만, 실행시간이 느리고, 메모리 공간을 많이 차지한다는 단점이 있다.  

3) 하이브리드 구현 시스템 - 대표적인 JAVA의 JVM이 이러한 역할을 수행한다. JAVA는 OS 상관없이 bytecode로의 컴파일을 수행하고, OS마다 다른 JVM을 설치하여 bytecode를 interpret한다.  

4) Preprocessor(전처리기) - 대표적으로 C언어의 #include <stdio.h>이 있는데, macro expander라고 생각하면 된다. 소스코드에 추가적인 코드를 붙여주는 방식이라고 이해하면 편하다.  

<h2>6. Program Environments</h2>  
> 프로그래밍 언어는 파일시스템, 코드 에디터, 링커, 컴파일러, 디버거, UI 등 다양한 프로그램 환경을 제공해줘야 한다.