---
layout: post
title: 'Computer Architecture 02: MIPS Instructions (1) - Types of MIPS Instructions'
date: 2024-10-02 23:43 +0900
description: 
image:
  path: /assets/img/contents/comp_arch_textbook.png
  alt: comp_arch_textbook
category: [Computer Science, Computer Architecture]
tags: [comp_arch, MIPS, ISA]
pin: false
math: true
mermaid: true
toc: true
---

> 컴퓨터구조 파트에 기술되는 모든 내용은 "Computer Organization and Design - The hardware / software interface", by Patterson and Hennessy 전공 서적에 의존하고 있습니다.  
{: .prompt-warning }  

![text_book](/assets/img/contents/comp_arch_textbook.png)

<h2>1. Instruction Set</h2>
컴퓨터의 종류가 다르면 instruction set 도 달라진다.
예를 들어, AMD CPU의 instruction과 Intel CPU의 instruction이 다른 것처럼 말이다.  

책에서 제시하는 컴퓨터 디자이너의 목표는 다음과 같다.  
> 성능은 최대화시키고, 비용 및 에너지는 최소화시키는 하드웨어와 컴파일러를 빌드하기 쉬운 언어를 찾는 것  

위 책에서는 MIPS instruction set에 대해서 다룬다.

<h2>2. MIPS Instruction Set</h2>  
MIPS instruction set은 instruction 종류에 따라 혹은 format 종류에 따라 구분한다.  

먼저, type에 따라 구분하면,  
1. Arithmetic Instructions  
2. Memory Instructions  
3. Logical Instructions  
4. Conditional Instructions  
5. Branch(or Jump) Instructions  
6. Floating Point Insturctions  
7. Pseudo Instructions  

등으로 구분된다.  

쉽게 이야기하면, 어떤 instructions인지에 대한 `특성` 또는 `용도`에 따라 구분했다고 보면 된다.  

format에 따라 구분하면  
1. R-format  
2. I-format  
3. J-format  
4. Floating-point instruction formats  
으로 구분된다. 여기서 R, I, J는 각각 Register, Immediate, Jump의 약자로, MIPS instruction의 `형식`에 따른 구분이라고 생각하면 된다.  

<h3>Arithmetic Operations</h3>  

```mips
add a, b, c
```
add는 항상 두 개의 src와 1개의 dst로 이뤄진, 총 3개의 operand로 구성된 instruction이다. (sub도 동일하게 `sub a, b, c`로 작성된다.)  
b와 c를 더해 a에 할당한다.  
예를 들어,
`a = b + c + d`라는 c코드가 있을 때, 다음과 같은 MIPS code로 컴파일된다.  
```mips
add a, b, c
add a, a, d
```  
항상 두 개의 값만 더할 수 있다.  
이렇게 만든 이유는 `Design Principle 1: Simplicity favors regularity` 때문이다.  
즉, regularity는 구현을 단순하게 하며, simplicity는 적은 비용에 높은 성능을 낼 수 있다는 뜻이고, 이런 법칙에 의해 add instruction의 설계가 이뤄진 것이다.  

<h3>Register Operands</h3>  

산술 instruction은 register operands를 이용한다.  
(여기서, register란 processor에 내장된 매우 작은 특수한 공간으로, 매우 빠른 저장공간이다. CPU가 명령어를 처리하는 과정에서 임시로 처리할 데이터를 저장하거나 메모리 주소를 저장하는 목적으로 또는 프로그램 실행 흐름을 제어하거나 상태를 저장하기 위해 사용한다.)  

__MIPS는 32 x 32-bit register이다.__  
즉, 32-bit 단위 register가 32개 존재하는 구조이다.  
(여기서 32-bit는 4bytes, 우리가 1 word라고 칭하는 단위이다.)  
레지스터의 데이터에 접근할 때 0부터 31까지 번호를 붙이고, `$` 기호를 사용한다.  

\\$t0, \\$t1, ..., \\$t9 : 보통 temporary value에 대한 register 주소 참조  
\\$s0, \\$s1, ..., \\$s7 : 보통 원래 코드에 있던 저장된 변수에 대한 register 주소 참조  
여기서 `Design Principle 2: Smaller is faster`가 등장한다.  
register의 크기를 많이 사용할 필요가 없는 이유는 작을수록 더 빠르게 처리하기 때문이다.  

```c
f = (g + h) - (i + j); // f, ..., j in $s0, ..., $s4
```
위와 같은 C-code가 주어졌을 때  

```mips
add $t0, $s1, $s2
add $t1, $s3, $s4
sub $s0, $t0, $t1
```  

다음과 같이 MIPS 코드로 컴파일된다.  

<h3>Memory Operands</h3>  

레지스터는 오직 32 x 32-bit 공간만을 가지고 있다.  
composite data를 전부 저장할 수는 없다.  
(cf. composite data란 쪼갤 수 있는 데이터로, 예를 들어, 배열, 구조체, 동적 데이터 등을 말한다.)  
레지스터에 모든 데이터를 저장할 수 없기에 Main Memory를 활용한다.  

그래서, Memory에 저장된 데이터를 이동시키기 위한 operands가 존재한다.  
1. Load (메모리에서 레지스터로 값을 불러옴)
2. Store (레지스터에서 연산한 결과물을 메모리에 저장)

위와 같은 2가지 연산이 필요하다.  

메모리에 접근하기 위해서는 **메모리 주소**가 필요한데,  
메모리는 byte addressed이다. 즉, byte 단위로 addressing이 이뤄진다.  
일반적으로 32 bit memory address는 1byte 단위로 최대 $2^{32}$bytes 크기를 가진다. (= 4GB)
레지스터는 위에서 설명했다시피, word(4bytes) 단위 구성이다.(= 시작 주소가 항상 4의 배수이다.)  
만약 레지스터의 연산이 끝나서 메모리에 저장을 해야 하는 경우, alignment restriction이 발생한다. 이는 words가 메모리에 align될 때 데이터는 자연스러운 경계를 지키면서 저장되어야 함을 의미한다. 

4bytes boundary는 간단한 C based code에서도 확인 가능한데,
```c
#include <stdio.h>

struct mystruct {
  char a;
  int b;
  short c;
};
```
다음과 같은 구조체가 주어졌을 때, char은 1byte, int는 4bytes, short는 2bytes이기 때문에 mystruct는 7bytes 크기라고 생각할 수 있지만, 전혀 아니다.  
char부터 순서대로 4bytes 단위로 저장되어야 한다. char의 1byte가 저장되고 int 4bytes를 저장할 때 4bytes boundary를 넘어가기 때문에 char 1개를 4bytes에 저장하고 그 다음 int를 4bytes에 short 2bytes도 4bytes boundary에 의해 4bytes 공간에 저장된다. 즉, 12bytes 크기의 구조체인 것이다.  

다시 본론으로 돌아와서, word가 메모리에 저장될 때 4bytes를 저장하는데 1byte씩 저장해줘야 한다. 이때, most significant byte부터 메모리에 저장할 것인지 (Big Endian) 혹은 least significant byte 부터 저장할 것인지 (Little Endian)에 따라 Big Endian과 Little Endian으로 나뉜다.  
MIPS는 Big Endian 방식을 채택한다.

**cf. Byte Ordering**
multi-byte 데이터를 메모리에 어떻게 저장할 것인가에 대한 방법론이다.  
1) Little Endian
2) Big Endian

향후 설명 추가 예정  

본론으로 돌아와서, memory instructions의 연산자는 두 가지가 있다.  
1. lw (load word)
2. sw (store word)

두 연산자 모두 3개의 operand를 필요로 하고, dst register와 offset, base address(of register)가 필요하다.  

```mips
lw $t0, 32($s3)
```
위 예시 mips 코드를 통해 살펴보면, $t0(temporary register)에 메모리의 값을 저장하는 명령어이다.  
이때, $s3에 있는 base register를 참고해 offset인 32를 곱한다.  
왜 32일까? 원본 C 코드를 살펴보자.  

```c
g = h + A[8]; // g in $s1, h in $s2 base address of A in $s3
```
위 C 코드는 다음과 같이 컴파일된다.  
```mips
lw $t0, 32($s3)
add $s1, $s2, $t0
```
여기서 감이 잘힐 것이다. A는 $s3에 위치한 포인터이다. 해당 포인터를 기준으로 8번째 인덱스에 위치한 값을 참조해야 한다. 1 word (= 4bytes) 단위로 처리하므로 8번째 인덱스의 주소는 4를 곱한 32의 offset을 가지는 것이다.  
여담으로, char array여도 똑같은 offset인가? 를 생각해본 적이 있는데,  
MIPS에선 동일한 offset으로 컴파일된다.

```c
A[12] = h + A[8];
```
위와 같은 코드는
```mips
lw $t0, 32($s3)
add $t0, $s2, $t0
sw $t0, 48($s3)
```
로 컴파일 된다.

<h3>Immediate Operands</h3>

상수 연산자이다.  
addi가 대표적인데, subi는 없다.(대신 음수인 상수로 대체한다.)  
필요한 것만 만들자는 MIPS의 취지이다.  
```
addi $s3, $s3, 4
addi $s2, $s1, -1
```
위와 같이 쓰인다.  

상수 연산을 통해 특이한 MIPS 코드를 짜는 것도 가능한데,  
```
add $t2, $s1, $zero
```
위 코드는 s1에 저장된 값을 t2로 이동하는 코드이다.

여기서, `Design Principle 3: Make the common case fast`가 등장한다.  
상수 연산자를 만든 이유이다. 당장 C언어의 for문을 봐도 인덱스 증감에 얼마나 많은 MIPS의 상수 연산이 필요한지를 알 수 있다.  
매우 작은 상수를 더하는 행위는 흔하기 때문에, 자주 사용하기 때문에 만든 것이다.  

<h3>2's Complement & Integer Wrapping</h3>

1. Unsigned Binary Integers  
    $x_{(10)} = x_{n-1}2^{n-1}+x_{n-2}2^{n-2}+\cdots+x_{1}2^1+x_{0}2^0$  
    2진수의 10진수 변환은 간단하다.  
    <앞으로 비트 단위의 숫자를 적어야 할 땐, 8bit를 한 묶음으로 표현하겠다.>  
    예를 들어,  
    8-bit에서는 0 ~ 255
    16-bit에서는 0 ~ 65535  
    32-bit에서는 0 ~ $2^{32}-1$  
    범위의 수를 표현할 수 있다.  

    $10_{(10)}$은 8bit-unsiged-int로 변환하면 $00001010_2$ 이다.

2. 2's Complement Signed Integers  

    2의 보수법이다. 부호가 있는 정수를 표현하기 위해서 만든 방식으로, +0과 -0이 다른 비트값으로 표현되는 문제와, 연산시 올바르지 않은 결과가 나오는 문제를 해결해준 방식이다.  
    원리는 간단하다. `Flip all bits & add 1`  
    $x_{(10)} = -x_{n-1}2^{n-1}+x_{n-2}2^{n-2}+\cdots+x_{1}2^1+x_{0}2^0$  
    n-bit의 정수가 주어졌을 때, 위의 연산으로 상호 변환할 수 있다. unsigned와는 맨 앞 비트의 부호만 달라졌음을 확인할 수 있다.  

    몇 가지 특징을 살펴볼 수 있는데,  
    1. 맨 앞 비트가 1이면 음수이다.
    2. 맨 앞 비트가 0이면 양수이다.
    3. $2^{(n-1)}$은 표현되지 못한다. 즉, 표현 범위는 $-2^{(n-1)} ~ 2^{(n-1)}-1$
    4. 0 based 10은 00000000....0000의 형태로 표현
    5. 1 based 10은 11111111....1111의 형태로 표현
    6. 가장 큰 음수는 10000000....0000의 형태로 표현
    7. 가장 큰 양수는 01111111....1111의 형태로 표현  
   
    아래 사항은 암기하자.  
    8bit에서는 -128 ~ +127  
    16bit에서는 -32768 ~ + 32767  
    의 범위를 가진다.  

3. Integer Wrapping  

    ```c
    #include <stdio.h>
    #include <stdint.h>

    int main() {
        char a = 100;
        char b = a + 300;
        char c = a - 300;
        printf("%d %d %d\n", a, b, c);

        return 0;
    }
    ```  
    다음 연산의 결과는 무엇일까?  
    100을 8bit에 나타내보자. $01100100_{(2)}$  

    100이 전부 char(8bits) 안에 표현된다. 즉, decimal format으로 출력하면 100 그대로 나온다.  
    a + 300 = 400이다. 왜 400인지는 C언어의 Type Casting을 공부하면 쉽게 알 수 있다. (C언어는 char과 short의 연산이든 short와 int의 연산이든 정수 연산에서 int 자료형으로의 implicit한 형변환이 일어난다.)(Sign Extension과 결합해서 설명하면 좋은데, a는 100이지만, int(4bytes)형인 300과 계산하기 위해 sign extension을 해야 한다. 동일한 맥락이다. $$00000000 \; 00000000 \; 00000000 \; 01100100_{(2)}$$ 2진수로 변환한 32bit의 300, $$00000000 \; 00000000 \; 00000001 \; 00101100_{(2)}$$ 과 연산하면 아래 400과 같은 값이 나온다.)  
    400을 2진수로 표현해보자. $00000000 \; 00000000 \; 00000001 \; 10010000_{(2)}$  
    
    b에 할당할 때, char(8-bit)의 범위를 넘어간다. 이 때 등장하는 것이 Overflow이자, Integer Wrapping이다.  
    넘어간 비트 '1'은 버려지고 뒤의 8bit만 인식한다.  

    따라서, $10010000_{(2)}$의 값이 되는데, 여기서 char의 특성을 적용해야 한다.  

    C언어 기초를 떼면서, char에 대해서 잘못 알고 있는 경우가 많다. 나도 그랬다.  
    char은 '문자'를 저장하기 위한 변수가 아니다. 1byte의 정수를 저장하기 위해 사용하는 자료형일 뿐이다. 일반적으로 char에 저장하는 값이 ASC2이며, 7bit 체계를 가지고 있기 때문에 문자 전부를 나타낼 수 있어 사용하는 것 뿐이다. (이때, 1bit는 통신 확인용 페리티 비트)  
    다시 본론으로 돌아와서, 여기서 char은 부호가 존재하는 1byte의 정수 자료형이라고 판단하면 된다. 따라서, $10010000_{(2)}$는 144가 아닌, 음수 형태, 즉, `-128+16 = -112`의 값을 출력하게 된다. 

    그렇다면, c의 결과를 살펴보자.  
    a-300의 결과인 -200은 2진수로 표현하였을 때, $11111111 \; 11111111 \; 11111111 \; 00111000_{(2)}$이다. (위에서 설명한 sign extension 참고)  
    하지만 c는 char이므로, 00111000만 저장하여, 10진수로 표현하면 56이다.  

    아래 경우도 살펴보자.  
    ```c
    #include <stdio.h>
    #include <stdint.h>

    int main() {
        unsigned char a = 100;
        unsigned char b = a + 300;
        unsigned char c = a - 300;
        printf("%d %d %d\n", a, b, c);

        return 0;
    }
    ```
    1. a는 $$01100100_{(2)}$$의 형태로 a에 저장되어있다. (int형의 100이 a에 저장되는 과정 생략)  
    2. a의 sign extension이 일어나 $$00000000 \; 00000000 \; 00000001 \; 01100100_{(2)}$$ 의 형태로 존재하며, 300은 $$00000000 \; 00000000 \; 00000001 \; 00101100_{(2)}$$ 와 같은 형태로 존재하는데, 이를 더하면 당연히 400이 나온다. $$00000000 \; 00000000 \; 00000001 \; 10010000_{(2)}$$  
    이를 unsigned char에 저장하면 $$10010000_{(2)}$$ 이런 형태로 저장되고, 10진수 기준으로 `128+16=144`가 b에 저장될 것이다.
    3. c가 56인 건 저명하므로 패스!  

    여기서 문제,  
    char b = a + 300;  
    printf("%u", b);  
    의 결과는 놀랍게도 `4294967184`이다.  
    %u는 unsigned int를 가정한다는 사실을 알면 쉽게 이해될 것이다.  

    결론은 sign extension(음수든 양수든 top bit 기준으로 확장)과 자료형 크기 제한을 잘 써먹어야 한다는 것이다!



