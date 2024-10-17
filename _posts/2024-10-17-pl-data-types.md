---
layout: post
title: "Concepts of Programming Languages 05: Data Types"
date: 2024-10-17 01:17 +0900
description: 
category: [Computer Science, Concepts of Programming Languages]
tags: [Programming Languages, Date Types]
pin: false
math: true
mermaid: true
toc: true
---

Data Type이란 무엇인가?  
이 책에선 data value와 그에 대한 predefined operation의 집합이라고 정의한다.  
자료형이란 다루는 데이터의 값과 그 연산을 정의한 것이다.  
다양한 자료형이 필요한 이유는 프로그래밍이 더 쉬워지기 때문이다. 단순하다!  
pre-90 FORTRAN 시대에는 오로지 배열로만 구현했고,  
COBOL와서야 record에 대한 structured data type (구조체와 비슷)를 지원했다.  
PL/1은 많은 데이터 타입을 지원했고, ALGOL-68은 사용자 정의 타입을 제공하기 시작했으며,  
Ada는 추상 데이터 타입을 지원한 언어이다.  

자료형에 대한 많은 변천이 있었다.  
이 게시글에서는 프로그래밍 언어에서 중요한 요소 중 하나인 자료형의 분류와 특징을 알아본다.  

<h2>1. Primitive Data Types</h2>  
원시 자료형은 프로그래밍 언어에서 기본으로 제공하는 자료형을 말한다.  
자료형의 표현과 연산들이 h/w에 의해 지원이 된다면 그 자료형을 primitive data type이라고 말한다.  
더 복잡한 구조의 자료형을 제공하기 위해 사용되는 자료형으로 이해해도 괜찮다.  

1. Numeric Type  
- Integer  
가장 흔하고, 동일한 integer여도 다양한 크기를 제공하며, 어떤 언어의 경우는 unsigned integer를 제공하기도 한다.  
컴퓨터의 CPU에 의해서 조작되는 unit인 bit 묶음을 `word`라고 표현하는데(컴퓨터 구조 초반부 내용 참고)  
보통 single memory word로 저장된다. (16-bit comp에선 2bytes로 저장되며, 32-bit comp에선 4bytes로 저장된다.)  
[구현 방식]  
이걸 고민한다면 IT 분야에 몸 담지 말자.  
모든 컴퓨터는 2의 보수법을 통해 integer type을 구현한다.(내용이 궁금하다면 역시 컴퓨터 구조 초반부 내용 참고)  
- Floating-Point(fraction + exponents)  
이것도 현재 모든 컴퓨터의 표준이 된 실수 표현 방식이다.(거의 대부분 근사값이다.)  
컴퓨터 구조 과목을 공부해보면 알겠지만, 대부분의 컴퓨터는 FPU(FP 전용 Processor Unit)이 있어 부동소수점 방식의 실수 처리를 담당한다.  
하지만, 초기 컴퓨터나 경량화된 processor에는 FPU가 존재하지 않는데,  
그럼에도 불구하고 거의 거의 모든 언어가 FP 자료형을 포함하는데 왜일까? scientific programming을 지원하도록 설계되었기 때문이다.  
대부분의 과학 분야에서는 real 이나 double precision이 중요하기 때문이다.  
[구현 방식]    
IEEE FP 표준 754 포맷이다.  
(컴퓨터 구조 과목에서 자세히 다루고 그 게시글을 참고하자.)  
- Decimal  
business분야도 지원해야 하기 때문에 대부분의 hw와 프로그래밍 언어는 10진수를 지원한다.  
BCD 방식으로 제공하는데, 이는 다음과 같다.  
매우 정확하게 decimal 값을 제공해 줄 수 있다.  
예를 들어, 20이라는 10진수가 있을 때, `0000 0010 0000 0000`으로 제공한다.  
앞의 1byte는 2를, 뒤의 1byte는 0을 표현한다.  
이를 unpacked 방식이라고 하며, 일반적인 방식이다.   
packed 방식은 메모리 공간이 아까우니, `0010 0000`과 같이 10진수 두 개의 자리를 1byte에 표현한다.  
[구현 방식]  
character string 처럼 2byte 공간에 저장하며 BCD를 사용함으로써 구현한다.  

2. Boolean Type  
가장 단순한 자료형이며, true / false 값 밖에 못 가진다. (readability를 위해서!)  
구현은 single bit로 하는데, 일반적으로 컴퓨터는 bit 단위로 읽지는 않는다.   
따라서 메모리 공간 상, 1byte로 저장되고 이용된다.  

3. Character Type  
일반적으로 아스키코드(0~127)과 같이 numeric으로 인코딩해서 저장된다.  
C/C++은 char를, FORTRAN은 CHARACTER라는 이름으로 이를 제공한다.  
아스키코드는 1 byte이고, 유니코드는 2bytes를 사용한다.  
비교적 최근 언어인 JAVA, JS, Python, Perl, C# 모두 유니코드 방식을 이용한다.  

<h2>2. Character String Types</h2>  
쉽게 말해서 문자열 타입이다.  
여기서 언어 설계 시에 두 가지 고민이 생긴다.  
하나는 기본 자료형으로 제공할 것인지 혹은 character array(문자 배열)로 제공할 것인지 결정해야 한다.  
또 다른 하나는 길이를 정적으로 제공할 것인지 동적으로 제공할 것인지 결정해야 한다.  
하나하나씩 살펴보도록 하자.  
1) Primitive or Char Arr  
- Character Array로 제공  
C, Pascal, C++, Ada, ...  
- Primitive Data Type으로 제공  
언어의 작성력이 좋아지고, 큰 비용 또한 들지 않기 때문에  
비교적 최근 언어에서는 거의 전부 기본 자료형으로 제공한다.  
할당, 관계 연산, concat, substring reference(예: 슬라이싱, ...)이 제공된다.

2) String Length Option  
- Static length string  
문자열의 길이가 static이고 구체적으로 선언됨으로써 명시된다.  
예) FORTRAN  
- Limited dynamic length string  
선언된 만큼의 길이까지 길이를 변화할 수 있고, maximum을 수정할 수 있는 문자열이다.  
예) C - `char str[20];` 문자열 길이가 20이 아니어도 되고 NULL 문자 위치에 따라 길이를 변경할 수 있다.  
- Dynamic length string  
maximum이 없이 문자열의 길이가 변화하는 문자열이다.  
유연하다는 장점이 있지만, dynamic storage allocation 문제가 발생한다.  
예) JAVA, C++  

**구현**  
static/dynamic strings을 위한 descriptor가 있다.  
descriptor란 변수의 attribute를 묶은 집합이다.  
- Compile-time Descriptor  
static string의 경우, 길이와 주소(attribute)를 compile-time descriptor가 관리하며, static length를 정해준다.  
- Run-time Descriptor  
Limited Dynamic String의 경우, run-time descriptor가 길이를 정해준다. (하지만, C/C++은 아님)  
Dynamic length string도 run-time descritor가 필요하다.  

**동적 할당을 위한 2가지 접근 방법**  
동적 할당은 문자열의 길이가 실행시간동안 변화하는 상황에서 메모리에 공간을 할당하는 것으로, 두 가지 방식이 존재한다.  
1. linked-list  
느리고, 더 많은 저장공간이 필요하다.(추가적으로 link를 저장하는 포인터 공간이 필요하기 때문!)  
2. adjacent storage cells  
인접한 메모리 공간에 완전한 문자열을 저장하는 것을 의미한다.  
쉽게 말해서, 메모리 공간에 문자열을 concat하려고 할 때, 있던 문자열을 밀어버리고 새로 할당하거나, 다른 메모리 공간에 할당하고 연결하거나 등의 방식을 사용해서  
빠른 참조, 적은 storage 사용량 장점을 가지지만,  
할당 및 해제에 시간 소요가 크다는 단점이 있다.  

<h2>3. User-Defined Ordinal Types</h2>  
Ordinal Type은 순서 타입으로 enum 같은 걸 생각하면 된다.  
가능한 값의 범위가 양의 정수(positive integer)와 1:1 매칭되는 자료형을 말한다.  
1) Enumerated Type  
symbolic constant(이름있는 상수)를 이용해 열거해서 가능한 값들을 정의한다.  
예를 들어, Ada에서  
type Days is (Mon, Tue, ... , Sun);  
이라는 코드가 있을 때, Mon에 0부터 시작해 Sun에 6이라는 정수가 할당된다.  

설계시 고려할 부분은,  
enum 타입이 한 가지 type으로만 나타날 수 있는지(overloaded literals).  
모든 enum 타입이 정수와 매핑되어야 하는지 혹은 정수 이외의 타입과 매핑이 되는지, 된다면 타입 검사는 어떻게 할 것인지.  
와 같은 부분을 고려해야 한다.  

Pascal 언어에서는,  
하나의 열거형 타입 정의 이외의 이외의 literal constant를 허용하지 않는다.  
열거형 타입의 변수는 array scripts로 사용될 수 있고, for문 loop 변수로, 그리고 case selector로도 사용될 수 있다.  
relational operator와 비교도 가능하다. 

C 언어에서는,  
묵시적으로 integer로 바뀐다.  

`Enumerated Type이 필요한 이유는 더 좋은 가독성을 위해서이다.`  
numeric type과 비교하면,  
arithmetic operation(산술 연산)이 불가능하며,  
range errors 즉, 정의된 범위 바깥 값을 할당할 경우에 에러를 표시한다는 점에서  
굉장히 장점이 많기 때문에 많은 언어에서 이를 구현하고 있다.  

2) Subrange Type  
순서형 타입의 연속적인 subsequence이다.  
보통 정수의 부분 범위를 나타내는데 이용한다.  
가독성과 reliability를 높여주지만,  
Ada95 이후 대부분의 언어는 지원하지 않게 되었다.  

**Ordinal Type의 구현**  
Enumerated Types는 보통 음이 아닌 정수 값으로 구현된다.  
Subrange Types는 보통 rage checks는 매 할당마다 포함되어야 하기 때문에 이 기능을 제외하고 전부 Enumeration type과 동일하게 구현된다.  

<h2>4. Array Types</h2>  
배열은 데이터 요소의 동일한 집합이다.  
각각의 요소들은 첫 요소를 기준으로 집합 내의 position에 따라서 식별된다.  
프로그램 내의 내열 요소에 대한 참조는 non-constant subscript의 참조가 이뤄진다.  
이러한 참조는 실행시간에 추가적인 계산이 필요하다.  

설계 시 고려한 부분은 다음과 같다.  
subscript(첨자)에 어떤 유형이 적합한가?  
첨자에 범위 바인딩을 언제 할 것인가?  
배열의 할당은 언제 할 것인가?  
첨자는 몇 개까지 가능한가?(차원)  
배열을 초기화 하는가?  
슬라이싱을 지원하는가?  

**Array & Indices**  
Array Referencing -> 이름과 인덱스(or subscript)를 기준으로 참조한다.  
index가 하나일 필요는 없기 때문에, index_value_list와 배열 이름을 제공하면 elements가 나온다.  
mapping의 개념으로 이해해도 좋다.  
Subscript의 종류로 Parentheses 와 Bracket 방식 두 개가 있는데,  
Parentheses는 B(I)와 같이 표기된다. 이러한 경우 컴파일러가 function calling과 문법적으로 헷갈리는 경우가 발생하기 때문에,  
일반적으로는 Bracket을 이용한다.  

**Subscript Binding & Array Categories**  
subscript type이 배열 변수에 바인딩 되는 것은 보통 static 방식이다.  
subscript value range(ex. int, boolean, ...)와 배열 메모리 공간을 언제 하는지에 따라 4가지로 분류한다.  
1) Static Array  
첨자 범위 바인딩: static  
기억 공간 바인딩: static (=실행 시간 이전)  
장점은 `실행 시간 효율성`!!!  
2) Fixed stack-dynamic array  
첨자 범위 바인딩: static  
기억 공간 바인딩: run-time (실행 시간에 선언되는 시점에 할당됨)  
장점은 `기억 공간 효율성`!!!  
3) Stack dynamic array  
첨자 범위 바인딩: dynamic  
기억 공간 바인딩: dynamic  
장점은 `유연하다`!!!  
4) Heap dynamic array  
첨자 범위 바인딩과 기억 공간 바인딩 모두 dynamic이어서,  
stack dynamic array와 무슨 차이인지 감이 안 오겠지만,  
배열의 크기가 배열의 lifetime동안 언제든지 변할 수 있다.  
장점은 마찬가지로 `유연하다`!!!

**이기종 배열**  
배열 내 요소 값의 타입이 같을 필요가 없는 배열로, 모두 heap dynamic array로 구현된다.  
대부분의 인터프리터 언어는 이를 지원한다.  ㅁ

**배열의 차원**  
FORTRAN 시절엔 있었지만, 지금은 없음  
C언어에서의 배열은 `오직 하나의 subscript(1차원)`을 제공하지만, 배열이 elements로서 배열을 가질 수 있기 때문에,  
다차원 배열을 표현하는 것이 가능하다. (이는 직교성이 높은 설계라고 볼 수 있다.)  
예를 들어, mat[5][4]가 있으면, mat[5]가 배열의 이름, [4]가 첨자로 인식해 배열의 요소를 찾는다.  

**배열의 초기화**  
FORTRAN에서는 DATA 라는 statment로 초기화를 지원했다.  
C언어는 static array의 초기화를 지원했지만, dynamic array는 지원하지 않았다.(알다시피 malloc은 할당만 해줄 뿐 초기화 하진 않는다.)  
PASCAL과 Modular-2는 배열 초기화를 허용하지 않았고, Ada는 두 가지 방식을 지원했는데, 중요한 내용은 아니니 넘어가도록 하자.  

**배열의 연산**  
FORTRAN 90에서는 elemental이라고 부르는 배열 연산자를 제공하였다. (할당, 산술연산, 관계연산, 논리 연산이 가능하였다.)  
APL에서는 array-processing language 즉, 배열 연산에 특화된 언어이기 때문에 산술 연산이 vetor와 matrices로 정의된다.  

**슬라이스**  
배열의 substructure라고 생각하면 된다.  
python의 경우 A[1:3]하면 배열 내의 2번째 요소부터 3번째 요소 (0번째 인덱스 값부터 2번째 인덱스 값까지)를 참조한다.  
하나의 유닛으로서 배열의 일부를 참고하는 방식이다.  

**배열의 구현**  
효율적인 실행 시간 액세스를 위해서 배열의 요소 접근 방식이 컴파일 시간에 끝나야 한다.  
1) 1차원 배열  
대부분 row major order를 사용하고, comptile-time descriptor를 이용한다.  
`address(list[k]) = (address(list[1]) - element_size) + k*element_size`와 같이 주소에 접근한다.  

2) 다차원 배열  
마찬가지다. 대부분 row major order를 사용하고, arr[i][j]와 같은 형식으로 나타낸다.  
여기서, access function이란, row major order로 접근할 때,  
이차원 배열을 가정할 때,  
base address + ((i - row_lb) * n + (j - col_lb)) * element_size로 계산되는데,  
이 때, i와 j만 따로 항을 분류해 (i*n+j)*(element_size)만 계산하는 계산하는 것이 access function이다.  
i, j 변수만 몰고 나머지 주소를 미리 계산해 효율적으로 요소 접근이 가능하도록 하기 위해서다.  

<h2>5. Associative Arrays</h2>  
연관 배열은 unordered collection of data elements로 동일한 개수의 key와 value로 구성되어 있다.  
JAVA, C++에서는 hashmap, Python에서는 dictionary로 표현하는 것이 바로 이 자료형이다.   
반드시 key-value 쌍으로 존재해야 하며, 직관적이고 접근 효율성이 높다는 장점이 있다.  

<h2>6. Record Types</h2>  
record 타입은 다양한 자료형의 묶음이라고 생각하면 된다.  
이 책에서는 data element가 이기종의 집합으로 구성된 자료형이라고 소개하고 있으며,  
name에 의해서 구분된다.  
C언어의 구조체를 생각하면 된다.  

**Record vs. Array**  
element (요소) 측면에서 봤을 때, record는 다른 type을 허용하지만, 배열은 반드시 동일한 type으로 구성되어야 한다.  
referencing 측면에서 봤을 때, record는 identifier(이름)을 통해 식별되지만, 배열은 인덱스로 식별한다.  

**Record 타입의 구조**  
COBOL: level number로 nested structure를 구분하며, 동일하게 이름으로 식별된다.  
Ada: Record 내부에 Record type이 들어가는, 하위 record 구성이 가능하다.  
C or FORTRAN: 중첩된 record는 먼저 선언하고 중첩된 경우 그 이름을 쓴다.  

**References to Record Field**  
COBOL의 경우 OF 라는 키워드로 구분한다.  
MIDDLE OF EMPLOYEE-NAME OF ----  
하지만, 현대의 대부분의 언어는 `.`을 통해 구분한다.  
C언어 구조체의 멤버 접근하는 것과 동일하다.  

참조 방법은 크게 2가지가 있는데,  
완전 자격 참조와 생략 참조가 있다.  
우선, 완전 자격 참조 방식은 참조 시에 모든 중간 record name을 다 넣는 방식이다.  
생략 참조 방식은 이름에서 알 수 있다시피 중간 record name을 생략하는 방식이다.  
후자의 방식이 가독성이 더 떨어지는 단점이 있다.  

**Operations of Records**  
Pascal과 Modular-2는 assigned가 가능, 즉 복사가 가능했다.  
Ada는 record assignment와 equality, inequality 비교를 지원했다.  
COBOL은 복사가 되지만 동일한 name만을 복사하는 특이한 연산을 제공했다.  
C언어는 대입 연산만 지원한다.  

**Implementation**  
인접한 메모리 공간에 record의 field가 저장된다.  
Access method는 offset address(record의 시작과 관련된 주소)가 각 field와 관련 있도록 하는 방식이다. (word alignment)  

배열과 비교해보자.  
배열은 access function을 이용해 더 효율적인 계산을 사용하고 배열의 요소에 접근하도록 구현했다.  
하지만, record는 offset address와 word alignment 방식을 활용한다.  
record의 시작주소가 필요하다.  
그리고 아래의 예시처럼 word alignment 방식을 사용한다.  
```C
#include <stdio.h>

struct myStruct {
    char a;
    int b;
};

int main() {
    struct myStruct S1;
    printf("%d", sizeof(S1));
    
    return 0;
}
```  
위 코드의 출력 값은 8이다. 32bit 기반의 컴퓨터와 C 컴파일러는 word 단위가 32bit이고 이는 4byte이다.  
char type은 1byte도 다음 int가 4byte니 5byte의 공간을 사용할 것이라 생각하겠지만,  
word 단위로 읽고 처리하기 편하기 때문에 char을 4byte(1word) 공간에 할당한다.  
즉, 접근 속도 향상이 목표다.  

<h2>7. Union Types</h2>  
공용체로, 시간에 따라 어떤 자료형을 쓰는지 다르기 때문에 가장 큰 크기로 메모리를 할당하는 것이 큰 특징인 자료형이라 할 수 있다.  
동일한 변수에 시간에 따라 다른 자료형의 값을 할당할 수 있는 자료형인 것이다.  
type checking이 필요한지?, 레코드 자료형에 임베딩 되어야 하는지? 가 설계 포인트라고 볼 수 있다.  

FORTRAN에서는 UNION type에 대한 type checking이 없었다.  
ALGOL 68에서는 Discriminated union과 Conformity clause로 UNION Type을 나눴는데,  
Discriminated Union은 tag라 불리는 추가적인 값 또는 discriminat라고 불리는 값을 통해서 current type value를 식별했다.  
당연히, type checking은 실행시간에 일어난다.  
Conformity clause는 실행 시간에 유지되는 type tag를 테스트하여, 즉, 각 경우의 수 별로 다르게 처리하여 올바른 type 선택을 하도록 했다.  
Pascal에서는 Variant record를 제공했다.
C\C++은 Free Union 방식으로 no tag, no type checking이다.  

**구현**  
동일한 주소를 모든 가능한 variant(멤버 변수)가 사용하게 함으로써 구현하였다.  
충분한 공간을 위해 가장 크기가 큰 variant를 기준으로 할당된다.  

<h2>8. Set Types</h2>  
원소 중복이 없고 순서가 없는 집합 타입이다.  
set base type의 최대 원소 개수를 몇 개로 설정할 것인가가 설계에서의 가장 큰 이슈인데,  
Pascal에서는 implementation dependent(보통은 100개 이하)로 설계하였다.  
Pascal의 set operation은 :=, +, * -, = 가 있다.  

Set과 Array의 가장 큰 차이점은  
Set operation이 훨씬 효율적이라는 것이다.  

**구현**  
bit string으로 연산을 구현한다.  
보통 15bit로 표현하고 1bit는 현재 표현하고 있는 값을 나타낸다.  

set union : a logical OR  
member check : a logcial AND  

예를 들어, set = ['a', 'c', 'e', ....]에서 b가 있는지 찾고 있다면,  
`1010100....`(16bit)와 `0100....`(16bit)를 AND 연산해서 그 값을 얻으면 된다.  

<h2>8. Pointer & Reference Types</h2>  
포인터 타입은 변수가 메모리 주소로서 가지는 값의 범위를 연산하는 자료형으로, nil이라는 특수한 값이 존재한다.  
`nil`이란 포인터형 변수가 아무런 주소도 참조하지 않는 상태를 말한다.  
포인터 타입은 주로 간접 주소 방식이나 동적 할당에 쓰인다.  

포인터형 변수의 scope와 lifetime은 어떻게 설계할 것인지,  
동적 변수의 lifetime은 어떻게 설정할 것인지,  
포인터가 가리킬 수 있는 객체 유형에 따라 포인터가 제한되는지를 주요한 설계 포인트로 잡고 살펴보자.  

**포인터의 연산**  
두 가지 연산이 있다.  
1. 어떤 객체에 대한 주소를 포인터형 변수에 설정한다.  
`int *aa, bb, cc`에서 bb의 주소를 포인터형 변수 aa에 저장하기 위해서, `aa=&bb`와 같이 작성한다.  
2. 역참조한다.  
`cc = *aa`와 같이 역참조 한다.  

**포인터와 PL/1에서의 포인터 문제(굉장히 중요하다.)**  
1. Type checking  
포인터가 가리키고 있는 객체에 대한 type은 `domain type`이라고 부른다.  
PL/1에서는 single domain type에 엄격하지 않았다.  

2. Danglin Pointer  
허상 포인터라고도 하며, 할당되지 않은 동적 변수의 주소를 가지고 있는 포인터형 변수를 말한다.  
만약 int *i;를 선언한 뒤, 다른 함수 내에 int j; j = 5; i=&j;를 하고 함수를 탈출하면, `*i`는 이미 해제된 j의 메모리 영역을 가리키고 있다.  
이러한 상황을 dangling pointer라고 한다.  

3. Lost Objects  
garbage라고도 표현하는데, 동적 할당된 객체가 더 이상 접근이 불가능해진 상태를 말한다.(다른 용도로 사용이 불가능한 상태)  

**Pascal과 C에서의 포인터**  
1. Pascal  
포인터는 오로지 접근 하는데만 사용 가능했다. (동적으로 할당된 익명 변수들에)  
new로 할당하고, dispose로 해제했는데,  
dispose의 구현 시에 dangling pointer 문제가 발생했고,  
언어 사용자 단에서 이를 무시하거나 그냥 허용함으로써 해결하려 하였다.  

2. C  
포인터는 어셈블리어에서 사용되는 주소와 같이 사용된다.  
언어 자체에서 dangling pointer나 garbage 문제를 해결하려는 지원을 하지 않았다.  
&, * 연산은 앞서 다루었다.  
또한 포인터 산술연산이 가능했다. (ptr+index) 객체의 size 만큼을 index에 곱해서 ptr가 가리켰다.  

**참조 타입**  
포인터와 참조 타입은 명백히 다르다.  
포인터는 메모리의 주소로 참조하는 것이고,  
참조는 메모리에 있는 객체나 값에 참조를 하는 것이다.  

특별히 C++에 이러한 reference type이 잘 드러나 있다. (하지만, 내부 구현은 전부 pointer 기반이라는 거...)  
=> function calling에서 two-way communication이 가능하도록 했다.  
(cf. 참조 타입의 변수는 실제 변수의 별칭이다.)

**구현**  
포인터의 구현은 간단하다, word size에 기반해서 메모리 공간을 할당했다.  
우리가 현재 사용하고 있는 C언어는 int형 포인터 변수, double형 포인터 변수 모두 상관없이 8bytes로 제공한다.(64bit 기반 컴퓨터이기 때문이다.)  

1. Dangling Pointer의 해결  
1) Tombstone Approach  
heap 공간의 tombstone이라는 하나의 특별한 cell을 이용해서,   
모든 포인터형 변수가 tomestone을 가리키고, 이 tombstone이 동적 변수를 가리켜 접근하는 방식이다.  
포인터 해제할 때는 tombstone은 남아있고, nil을 저장해서 동적 변수가 더이상 존재하지 않도록 한다.  
시간과 비용이 굉장히 많이 들어 잘 사용하지 않는다.  
왜냐하면, 동적 변수의 개수만큼 낭비되기 때문이다.  
2) Locks-and-key Approache  
포인터 값이 key(integer value), address의 순서가 있는 쌍으로 표현된다.  
포인터형 변수는 key를 가지고 있고, heap 공간의 동적 변수는 lock을 가지고 있으며, 현재 참조되는 환경의 key 값과 동일한 값이 lock에 저장되어 있다.  
매번 동적 변수에 접근할 때마다 포인터의 key 값과 동적 변수의 lock 값을 비교한다.  
새로운 포인터형 변수가 동적 변수를 참조하도록 바뀐다면 새로운 포인터형 변수의 key 값과 동일하게 동적 변수의 lock이 변경된다.  

2. Garbage의 해결  
Garbage는 heap에 저장되기 때문에 heap management의 개선이 곧 garbage의 개선이 된다.  
고정된 크기가 heap에 할당된다고 가정하자.(LISP)  
모든 메모리 셀은 가능한 공간의 리스트 형성 방식으로 서로 연결될 수 있다.  
해제는 보통 묵시적이지만, 언제 할당된 기억공간을 회수하는지에 따라 두 가지 방식을 ㅗ나뉜다.  
1) Reference Counter Approach  
동적 변수의 해제가 발생할 때마다 collection 한다.  
heap 공간의 동적 변수에 counter라는 값을 유지하고, 현재 그 셀(동적 변수)를 포인팅하는 포인터형 변수의 개수를 카운팅한다.  
참조하는 counter가 0이 되면 즉시 반환하는 방식이다.  
명백한 단점이 존재하는데, counter 차지 공간이 전체 셀에서 생각보다 높은 비율을 차지하며,  
counter를 유지하는 것이 실행시간에 매우 큰 부담이 되고,  
a->b->c->a와 같이 circular reference인 경우 counter가 항상 1이기 때문에 영원히 해제 불가능한 동적 변수가 되어버린다.  
2) Garbage Collection Approach  
일단 heap의 가용 공간을 다 쓰기 전까지 garbage를 신경 쓰지 않다가,  
더 이상 가용 공간이 남아있지 않을 때 heap을 떠도는 garbage를 한번에 회수하는 방식이다.  
이러한 garbage collection을 위해 추가적인 indicator bit나 field가 필요하다.  
단순한 알고리즘을 garbage algorithm을 소개한다.  
먼저, heap에 위치한 모든 cell은 그들이 garbage인지 아닌지에 대한 indicator를 가지고 있다.  
모든 포인터는 heap을 따라가소, 모든 가능한 셀들은 garbage로 인식되지 않는다.  
명확하게 garbage로 표시되지 않은 heap 공간의 모든 셀은 가용 곤간의 list로 회수된다.  
하지만, garbage collection의 가장 큰 문제는 `가장 필요로 할 때, 가장 최악이라는 것이다.`  
가용공간이 필요할 때, heap 메모리를 전수조사하기 때문에, heap을 스캔하는 시간이나 프로그램 실행을 위한 대기 시간이 길어지면서,  
시간에 대한 cost도 많이 생긴다.  
추가적으로, 다른 문제도 있다.  
heap에 있는 모든 셀들에 indicator를 표시하는 것이 매우 힘든 작업이라는 문제가 있는데,  
이는 시작과 끝 위치를 저장함으로써 해결한다.  
포인터를 쓰지 않고 힙 공간에 확장된 경우 중요한 문제가 발생하는데,  
이에 대한 가짜 포인터를 하나 만들어 주면 해결된다.  
또한, 사용 가능한 기억 공간 리스트가 파편화되어 있으면 할당할 공간에 비해 가용공간이 작은 경우, 가용공간을 병합해서 줄지, 셀 위치를 바꿔서 할당할지 결정하기도 쉽지 않을 뿐더러,  
가용공간 병합이 가능하더라도 시간 소요가 굉장히 크다는 문제가 있다.  