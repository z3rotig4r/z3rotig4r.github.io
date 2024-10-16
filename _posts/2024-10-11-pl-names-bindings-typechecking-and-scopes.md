---
layout: post
title: "Concepts of Programming Languages 04: Names, Bindings, Type Checking, and Scopes"
date: 2024-10-11 16:43 +0900
description: 
image:
  path: /assets/img/contents/pl_syntax.png
  alt: Ambiguous Expression Grammar
category: [Computer Science, Concepts of Programming Languages]
tags: [Programming Languages, Scope, Lifetime, Typechecking, Binding]
pin: false
math: true
mermaid: true
toc: true
---

> 우리가 현재 사용하는 컴퓨터는 폰노이만 구조를 채택하고 있다. 폰노이만 구조의 컴퓨터는 메모리와 CPU로 구성되어 있다.  
> Imperative Languages(명령형 언어)는 폰노이만 구조에서 사용하는 언어로, 컴퓨터 H/W를 추상화시켜 언어로 표현한 것이다. 대표적으로 프로그래밍 언어의 변수는 메모리 공간에 대한 추상화이다.  
> 또한, 변수는 데이터 타입이나, Scope, life time 등 속성의 모음으로 특정된다.  
> 언어가 현실 세계와 얼마나 잘 매칭시키는지가 가장 중요하다.  

<h2>1. Names</h2>  
> 변수, label, subprogram(함수), formal parameter 등 어떤 프로그램 내의 개체를 식별하기 위해 사용하는 문자열이다.  

**[설계 시 고려할 요소]**  

1) 이름의 최대 길이는 얼마로 정할지  
2) connect(연결 글자)를 사용 가능하게 할지  
3) 이름의 대소문자를 구분할 것인지  
4) special words나 reserved words 또는 keywords인지  

**[Name의 형태에 따라]**  
1) 이름의 길이  
초기 프로그래밍 언어는 문자 한 개로 이름을 사용하였다.  
점점 늘어나서 현재 C/C++은 이름의 길이에 제약이 없다.  

2) 대소문자 민감성  
C(C++)은 이름의 대소문자를 구분한다.  
이게 과연 좋은 언어라고 할 수 있을까?  
정답은 아니다.  
예를 들어, rose라는 이름의 변수가 있을 때, rose와 Rose와 ROSE는 전부 다른 변수로 인식된다. 즉, 인간이 동일한 'rose'라는 사물을 인식함과 달리 프로그래밍 언어를 읽을 땐 다른 변수로 인지하고 코드를 읽어야 하므로 가독성이 떨어지는 설계라고 본다.  
Writability도 떨어진다. 예를 들어, 함수명을 Add라고 정하고, add라고 호출해도 유연한 설계로 인해 오류가 발생하지 않지만, 대소문자 구분을 하게 되는 경우 오류를 호출한다. 즉, 프로그래머가 이를 인지하고 코드를 작성해야 하는 것이기 때문에 작성력을 떨어뜨리는 설계라고 본다.  

**[Special Words(특수어)]**  
Special words란, 실행되어야 하는 프로그램 내 행동들에 대해 특별한 이름을 붙여줌으로써 더 가독성 있게 프로그램을 만들게 해주며, statement의 문법적인 부분과 프로그램을 분리해주는 단어이다.  

1) Keyword(키워드)  
특정한 맥락에서만 특별해지는 단어로, 일반적으로 Special words를 재정의할 수 있는 경우를 키워드라고 말한다.  
예를 들어, FORTRAN에서 `REAL APPLE`이라고 선언하면 실수 자료형을 나타내는 특수어 REAL이 사용되었지만, 미리 정의한 특수어 REAL을 `REAL = 3.4`처럼 일반적인 변수로 사용할 수 있다.  
2) Reserved word(예약어)  
특수어를 변수로 (즉, 이름으로) 사용할 수 없는 특수어를 말한다.  
예를 들어, C언어의 `if`는 예약어로 '이름'으로 사용 불가능하다.  
또 다른 예시로, COBOL은 length, count, bottom 등 300개 가랴으이 예약어가 존재하기 때문에 작성력을 떨어뜨려 코드 작성자에게 불편함을 초래할 수 있다.  
일반적으로, 예약어가 키워드에 비해서 낫다고 평가한다.  

<h2>2. Variables</h2>  
> 변수란, 컴퓨터 메모리 셀에 대한 혹은 셀의 집합에 대한 추상화된 개념이다.  
> 변수는 name, address, value, type, lifetime, scope 총 6가지의 속성을 가지고 있다. 기억하자!  

1. Name  
변수에 대한 식별자로서 기능한다.  
2. Address  
실제 변수가 메모리 상에 어디에 저장되어 있는지를 알려주는 속성이다.  
대부분의 프로그래밍 언어는 `지역변수`를 지원하기 때문에 같은 이름의 변수가 서로 다른 위치에 매핑될 수도 있다.(서로 다른 주소를 가진다.)  
`Alias(별칭)`이란, 동일한 하나의 메모리 공간에 접근하기 위해 둘 이상의 이름을 사용할 때, 이를 Alias를 사용한다고 표현한다.  
대표적으로 FORTRAN의 EQUIVALENCE, PASCAL의 varient record, 대부분 언어의 subprogram parameters(함수 매개변수) 그리고 `Pointer`가 있다.  
3. Value  
변수가 실제로 갖는 값이다.  
추상적인 메모리 공간에 존재하는 내용(content)이다.  
l-value와 r-value가 있다.  
- l-value: 변수의 메모리 주소를 의미한다.  
- r-value: 변수의 값을 의미한다.  
4. Type  
변수의 타입은 변수가 `저장할 수 있는 값의 범위`와 `정의할 수 있는 연산의 집합`을 정의한 것이다.  
5. Lifetime  
6. Scope  

Lifetime과 Scope는 따로 후술할 예정이다.  

<h2>3. Concepts of Binding</h2>  
> 바인딩이란 operation과 symbol이나 Attribute와 Entity 같은 일종의 `연관성`을 의미한다. 쉽게 말해서 연산자와 기호 간의 역할 연결 또는 앞서 변수가 가지는 6가지의 attribute와 변수(entity)를 연결하는 것을 말한다.  

**[Binding Time]**  
변수와 속성 간에 `언제` 연관성이 생기고, 고정이 되는가? 6가지의 바인딩 타임이 존재한다.  
1) Language Design Time  
언어가 설계되는 시점에서 연관성이 정해지는 것을 의미한다. 예를 들어, `*`은 산술곱이라는 역할과 symbol이 매핑된다.  
2) Language Implementation Time  
언어가 구현되는 시점에서 연관성이 정해지는 것을 의미한다. 예를 들어, 자료형(data type)이 표현 가능한 값의 범위가 구현 시간에 정해진다.  
3) Compile Time  
언어가 컴파일 되는 시점에서 연관성이 매핑되는 것을 의미한다. 예를 들어, Pascal의 변수는 특정한 자료형으로 컴파일 타임에 매핑된다.(보통 C계열의 언어가 이때 data type을 정해 바꾸지 않는다.)  
4) Link Time  
Linking은 라이브러리를 호출하거나 헤더파일 등을 호출해 subprogram을 연결하는 작업이며, 이러한 작업으로 인한 연산 또는 변수 바인딩은 이 시간에 이뤄진다.  
5) Load Time  
메모리로 로딩되는 시간을 의미하며,   
프로그램의 machine code를 메모리에 로드했을 때, 변수가 메모리 공간에서 가지는 주소는 이때 바인딩된다.  
6) Run Time  
프로그램이 실행 중일 때 바인딩되는 것으로, 함수가 실제 호출되었을 때, 함수 내의 지역변수가 기억공간(메모리)에 이때 바인딩 된다.  

여기서 헷갈리지 말아야 할 몇 가지 사실들이 있다.  
1. C언어에서 main함수 내의 모든 변수는 지역변수이기 때문에 지역변수의 value는 실행시간에 바인딩된다.  
2. +, *와 같은 연산은 컴파일 시간에 바인딩된다.  
3. 함수의 인자는 실행시간에, 매개변수는 load time에 바인딩 된다.  

**[정적 바인딩과 동적 바인딩]**  
1. 정적 바인딩  
> 실행시간 이전에 일어나며, 프로그램 실행 도중에 바뀌지 않는 바인딩  
2. 동적 바인딩  
> 실행시간에 일어나며, 프로그램 실행 도중에 바뀌는 바인딩  

<h3>Type Binding</h3>  
- Static Type Binding(변수 선언)  
1) Explicit Declaration(명시적 선언)  
변수의 타입을 명시적으로 프로그램의 Statement를 이용해 선언한다.  
예를 들어, `int num;`과 같은 C언어의 statement가 있다.  
대부분의 프로그래밍 언어는 명시적 선언을 통해 Static Type Binding을 한다.  
2) Implicit Declaration(묵시적 선언)
deafult convetion(기본 매커니즘)을 활용해 변수의 타입을 변수와 결합해주는 방법이다.  
예를 들어, FORTRAN에서는 I, J, K, ...이 무조건 정수형 자료형이다.  
Writability는 증가하지만, Reliability가 감소하는 단점이 있다.  

- Dynamic Type Binding  
JS, Python과 같은 인터프리터 언어들이 동적 타입 바인딩을 지원한다.(machine code에서 동적으로 타입을 변경하는 것이 힘들기 때문이다.)  
assignment statement(할당문)에서 값이 할당되어질 때, 타입이 바인딩된다.  

장점은 Flexibility가 증가한다는 점이지만,  
단점은 실행 시간에 계속 타입을 체크하기 때문에 매우 느리며, 메모리 cost도 꽤 높다.  
또한, 컴파일 타임에서 에러를 탐지하기 어렵고 프로그램 신뢰성도 낮다.  

<h3>Storage Binding & Lifetime</h3>  
> Lifetime이란 변수가 특정한 메모리 공간에 바인딩된 시간을 말한다. 변수가 언제 할당되고, 언제 해제되는지가 중요하다.  

변수가 Lifetime이 어떤지에 따라서 다음과 같이 네 가지 종류로 구분된다.  

1. 정적 변수(Static Variables)  
프로그램이 실행되기 전에 메모리 공간에 바인딩되어 프로그램이 종료될 때까지 동일한 메모리 공간에 바인딩되는 변수를 말한다.  
예를 들어, 전역 변수, history sensitive variable이 이에 해당한다.  
장점은 효율적이라는 것이다. (컴파일 시간에 바인딩 되어 할당 해제에 별도의 시간이 필요 없다.)  
단점은 recursion을 지원하지 않아 유연성이 감소한다는 점이다.  

2. 스택 동적 변수(Stack Dynamic Variables)  
storage binding(메모리 공간 바인딩)이 선언문에 의해 일어난다. 즉, 데이터 타입은 static binding이 이뤄지는 반면에 storage에 binding되는 것은 동적으로 이뤄진다.  
예를 들어, 지역 변수가 이에 해당한다.  
장점은 재귀를 허용하며, 서로 다른 procedure(함수)간에 동일한 메모리 공간을 공유할 수 있다. 예를 들어, `void func1(){int a;}`, `void fuc2(){int b;}` 두 함수가 있을 때 동시에 쓰일일이 없다면 정수형 타입 a, b에 대해 4bytes의 공간만 사용하면 된다.  
단점은 subprogram을 호출할 때마다 할당 및 해제가 필요하여, 실행 시간이 느려지는데 영향을 준다. 또한, 일반적으로 간접주소를 사용하기 때문에 느리다.  

3. 묵시적 힙 동적 변수(Implicit Heap Dynamic Variables)  
변수를 선언했을 때 메모리를 할당하는 것이 아닌, assignment statement(할당문)이 나오면 그때 변수를 할당하고 반환하는 과정이 일어나는 변수  
해당 값이 배정될 때 메모리 공간상 Heap에 할당된다.  
높은 유연성을 가지고 있다는 장점이 있지만,  
실행 시간에 대한 부담이 큰 것이 단점이다.  

4. 명시적 힙 동적 변수(Explicit Heap Dynamic Variables)  
포인터나 참조를 이용해서 프로그래머에 의해 명시적으로 실행시간에 메모리가 할당 및 반환되는 변수이다.  
컴파일 타임에 데이터 타입이 바인딩되며, 명시적 힙 동적 변수가 생성되었을 때 메모리 공간에 바인딩된다.(실행시간에 메모리의 공간 할당 및 해제가 일어난다.)  
실행시간에 크기가 변경될 가능성이 있는 자료구조에 보통 쓰인다.  
장점으로는 동적 구조를 가질 수 있다는 점이고,  
단점으로는 구현이 힘들며, 참조, 할당, 해제에 대한 비용이 크다는 점이 있다.  

<h2>4. Type Checking</h2>  
Type Checking 이란 operator의 operand가 compatible한지를 보장하는 행위이다.  
추상적으로 말했는데, 연산자가 적합한지를 판단하거나, 적합한 type으로 자동 형변환(묵시적 형변환, 또는 type coersion)이 가능한 type을 compatible type이라고 하며,  
compatible type인지를 판단하는 작업이 type checking이다.  

예상하다시피, 두 가지의 type check 방식이 있다.  
(이런 거 한글로 쓰면 멋이 안 산다.... ㅋㅋㅋ)
1. Static type checking  
만약 모든 변수의 type binding이 정적이라면, type checking 또한 static하다.  
2. Dynamic type checking  
python이 이렇다. 실행시간에 type checking을 한다.  
만약, 하나의 메모리 공간에 담긴 값들이 전부 다른 data type이라면, type checking이 굉장히 복잡해진다.  
절대 컴파일 시간 내에 type checking을 할 수 없다.  
Python의 경우, 어차피 실행시간 오래 걸리는 거, 코드 유연성도 높이기 위해서 예를 들어, 배열 내에 다른 자료형을 넣어도 되는 이러한 문법을 허용하고 있기 때문에,  
동적 type checking을 할 수 밖에 없고, 그게 효율적이다.(대부분의 인터프리터 언어가 가지는 장점 아닌 장점이다.)  

<h2>5. Strong Typing</h2>  
Strongly Typed Language는 모든 데이터 타입이 static binding이며, type 오류가 compile-time에 검출되는 언어를 말한다.  
단, C/C++의 경우 type check를 하지 않기 때문에, 굉장히 strongly typed language와는 거리가 멀며, Java는 굉장히 가까운 경우에 속한다.  

<h2>6. Type Equivalence</h2>  
Type compatible은 서로 다른 두 변수 간에 서로 간에 호환이 되느냐, 즉, coersion이 일어나도 상관이 없는가를 나타낸다.  
정의가 어려우니 예시를 들어보자.  
```c
int a = 10;
double b = 20.0;
a = b;
b = a;
```
int형 data type인 a와 double형 data type인 b가 있을 때, double을 int에 할당할 수 있는가, 반대로 int를 double에 할당할 수 있는가를 판단하는 것이 Type Equivalence이다.  
C언어의 위와 같은 경우는 알아서 coercion이 일어난다. 묵시적인 형변환을 통해 할당이 된다.  

반대로, Type equivalence는 `coercion 없이` 한 변수가 다른 변수를 대체할 수 있는 경우를 말한다.  
즉, Type Compatibility의 strict한 형태이다. (= type compatibility without coercion)  
Type Equivalence를 정의하는 두 가지 방법이 있다.  
1. Name Type Equivalence  
동일한 declaration을 가지거나 동일한 type name을 declaration에 사용해야 두 변수가 equivalent하다고 정의한다.  
type의 이름까지 같아야 한다.  
예를 들어, 아래와 같은 C-like 프로그램이 있다고 가정해보자.  
```c
struct book {
  int page;
  char title[30];
}

struct ebook {
  int page;
  char title[30];
}
```
Name Type Equivalence에 따라 book과 ebook은 type equivalence하지 않다.  
구현하기 쉽지만 매우 restrictive하다.  

2. Structure Type Equivalence
반대로, structure type equivalence는 C언어 등에 많이 쓰이는 방식으로, 두 변수가 type compatible하면서 내부 구조가 동등하다면, type equivalence를 충족한다고 정의한다.  
위 C-like 프로그램의 예시를 다시 살펴볼 때, book과 ebook은 type equivalence를 충족한다고 표현할 수 있다.  
유연한 방법이지만 구현하기 힘들다.  

<h2>7. Scope</h2>  
프로그램 변수의 scope는 그 변수가 어떤 statement 범위 내에서 visible한지를 파악하는 것이다.  
변수가 visible하다는 것은 해당 statement에서 참조되어질 수 있다는 의미이다.  
알다시피, scoping도 두 가지 종류가 있다.  
1. Static Scoping  
동적 스코핑은 쉽게 말해서 코드의 구조만을 보고 참조 환경을 판단한다.  
지역 변수는 당연히 현재 실행되고 있는 프로시져에서 참조할 수 있다.  
하지만, 비지역변수의 경우 코드 구조에 따라 컴파일 시간에 어느 변수에 바인딩될지가 결정된다.  

```c
void main(){
  int a, b, c;
...
}
void fun1(void){
  int b, c, d;
...
  void fun2(void){
    int c, d, e;
    ...	//<-------------- (*)
  }
  void fun3(void){
    int d, e, f;
    ...
  }
}

```

`*`위치에서 만약 정적 scoping을 따른다고 할 때, 참조 환경은 다음과 같다.  
fun2의 c, d, e와 fun1의 b 이다. (fun2의 c, d는 hidden variable이다. 참조 환경에 포함하지 않음)

참고로, 언어에 따라 블록 안에서도 scoping rule이 적용되는 경우도 있다.  

**static scoping의 단점**  
컴파일러가 상위 parent의 호출 안 되는 프로시저 내의 scope를 참조하는 오류를 발생시킬 수 있다.  
따라서, 너무 많은 데이터 접근이 생기고, 프로그램을 구조를 수정하기 매우 힘들어진다.  

2. Dynamic Scoping  
Dynamic Scoping은 오로지 함수 호출 순서에 따라 결정된다.  
이러한 특성에 따라 Runtime이 되어서야 참조 환경을 알 수 밖에 없다.  
program unit 간의 parameter passing의 방법을 이용하여 communication을 하기에 편하다.  

**[Dynamic Scoping의 단점]**  
1. 실행 내내 변수가 참조하는 변수의 값이 계속 바뀌기 때문에 코드의 흐름을 따라가기 어렵고, 디버깅이 어려워진다.  
2. subprogram의 지역 변수들은 실행 중인 다른 subprogram에 visible한 상태이기 때문에 지역 변수의 값을 믿을 수 없게 된다.  

<h2>8. Scope & Lifetime</h2>  
- Scope: 변수가 어디에서 접근 가능한지, 즉, 어디서 visibl한지를 제공하는 지표이다.  
- Lifetime: 변수가 얼마나 오랫동안 유지되는지를 말하며, 메모리에 바인딩된 시간을 말한다.  

예를 들어, 프로시져 A를 호출 했을 때, 지역 변수 a가 있다면,  
a의 scope는 호출한 프로시져 내, 혹은 (static or dynamic에 따라 다르지만) 상위 프로시져라고 표현한다.  
a의 lifetime은 반면, A가 호출된 시점부터 해당 프로시져(A)가 끝날 때까지라고 표현한다.  

<h2>9. Referencing Enviornment</h2>  
참조환경은 위에서 Static Scoping / Dynamic Scoping을 설명할 때 넘어가듯이 설명했지만,  
특정 statement에서 볼 수 있는 모든 변수의 집합이라고 정의한다.  

hidden variable: 상위 프로시져에서 동일한 이름의 변수지만 지역변수 우선 또는 프로시져 호출 순위나 구조적 우선 순위에 의해 밀려나 참조되지 못한 변수를 의미한다.  
active procedure: 이미 실행되었지만 아직 끝나지 않은 프로시져를 말한다.  

<h2>10. Named Constants & Variable Initialization</h2>  
1) Named Constant  
한 번 값이 바인딩 되면 절대 안 바뀌는 변수를 말한다.  
C언어의 const  
JAVA의 final 이 그 예시이다.  

2) Variable Initialization  
기억 공간에 바인딩되는 시점에 값이 같이 바인딩되는 상황을 초기화라고 한다.  
WELL-KNOWN이니 넘어가도록 하자.  