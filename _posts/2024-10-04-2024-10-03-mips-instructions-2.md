---
layout: post
title: 'Computer Architecture 02: MIPS Instructions (2) - Formats of MIPS Instructions & Procedures Calling'
date: 2024-10-04 15:43 +0900
description: 
image:
  path: /assets/img/contents/mips_green_card.jpg
  alt: mips_green_card
category: [Computer Science, Computer Architecture]
tags: [comp_arch, MIPS, ISA]
pin: false
math: true
mermaid: true
toc: true
---
> 여기서부터 굉장히 어려움을 느꼈었는데, 포기하지 말자.  
{: .prompt-danger } 
![준비하자:)](https://i.namu.wiki/i/6WKpzGYj_XEUdVcTikh2U7CvQhl_X4W-UXUrXveWVWYP3wl7_KjT2-9lu6Dk3_MtMXAmSuyD6ZX6e2RBG9_6ww.webp)

Instructions는 binary 기반의 machine code로 인코딩된다.  
모든 MIPS의 instructions는 32-bit 기반으로 인코딩된다.  
instruction format은 오직 4가지 밖에 없는데, 이는 Instruction format이 단순해야 단순한 HW 구성이 가능해지기 때문이다.  
명령어의 종류마다 해당 32bit가 가진 형식이 정해져 있다.  
산술의 용도와는 전혀 관련이 없으니 주의하자.  

<h2>1. R-format Instructions</h2>
두 개의 피연산자와 목적지가 하나인 명령어에 쓰인다. (e.g. add, sub, and, ...)  

|   op   |   rs   |   rt   |   rd   | shamt  | funct  |
| :----: | :----: | :----: | :----: | :----: | :----: |
| 6 bits | 5 bits | 5 bits | 5 bits | 5 bits | 6 bits |


1. op: Operation Code, 명령어가 실행할 연산의 종류를 나타낸다. R-format은 000000이라는 6bit로 나타내는데, 이는 암기할 사항이 아니며, 포스팅 이미지에 적힌 MIPS Green Card를 참고하면 된다. 일반적으로 opcode를 통해 R-format인지, I-format인지, J-format인지 등을 결정한다.  
2. rs: first source register number
3. rt: second source register number
4. rd: destination register number
5. shamt: shift amount (shift 연산 시 shift 양을 나타내며, 없을 땐 00000으로 채워둔다.)  
6. funct: function code (extends opcode) (opcode에서 format이나 연산 종류를 일부 표시하였는데, 해당 format에서 사용할 연산(function)을 저장하는 공간이다.)  

추가적으로, 32개의 register 중에서  
\\$s0 ~ \\$s7 은 레지스터 16~23번  
\\$t0 ~ \\$t7 은 레지스터 8~15번에 매핑된다.  

```mips
add $t0, $s1, $s2
```
위와 같은 mips가 주어졌을 때, 기계어로는 다음과 같이 번역된다.  
R-format 이므로 최초 6bit는 `000000`으로 채워진다.  
rs에는 \\$s1 17번 register에 매핑되므로 `10001`으로 채워진다.  
rt에는 \\$s2 18번 register에 매핑되므로 `10010`으로 채워진다.  
rd에는 \\$t0 8번 register에 매핑되므로 `01000`으로 채워진다.  
shamt에는 현재 shift 연산이 없으므로 `00000`으로 채워진다.  
add는 MIPS Green Card를 참조하면, `100000`으로 채워짐을 알 수 있다.  

따라서,  
$$00000010 \; 00110010 \; 01000000 \; 00100000 _{(2)}$$ 이고,  
이를 hexdecimal(16진수)로 바꾸면  
`0x02324020`이다.  
이와 같은 형태로 machine code가 생성되면서, add 연산을 수행한다.  

<h2>2. I-format Instructions</h2>  
앞서 살펴본 addi의 경우 상수 연산을 수행하는데, 앞선 R-format으로는 5bit 공간에서 0~31의 값만 나타낼 수 있어 불충분한 상황이고, lw, sw 명령어도 형식이 많이 다르다.  
여기서 `Design Principle 04: Good Design Demands Good Compromises`가 등장한다.  
모든 명령어의 길이는 같게 하나, 명령어의 종류에 따라 형식은 다르게 취하는,  
좋은 설계에는 적당한 절충을 적용한 부분이라고 할 수 있다.  

|   op   |   rs   |   rt   | constant or address |
| :----: | :----: | :----: | :-----------------: |
| 6 bits | 5 bits | 5 bits |       16 bits       |

1. op: R-format 과 동일
2. rs: source register number
3. rt: 둘 중 하나이다. (destination register number / second source register number)
4. constant or address:  상수가 들어가거나 lw/sw에서의 offset이 들어간다.  

constant의 경우 $-2^{16} $ ~ $ + 2^{15} - 1$ 범위의 상수를 다룰 수 있다.  

```c
A[300] = h + A[300]
```
다음과 같은 c코드를

```mips
lw $t0, 1200($t1) // 알다시피 src는 t1, dst가 t0이다.
add $t0, $s0, $t0
sw $t0, 1200($t1)
```
이러한 mips 코드로 변환한다고 하자.  

위와 같은 mips가 주어졌을 때, 기계어로는 다음과 같이 번역된다.  
I-format에 lw 연산이므로 최초 6bit는 `100011`으로 채워진다.  
rs에는 \\$t1 9번 register에 매핑되므로 `01001`으로 채워진다.  
rt에는 \\$t0 8번 register에 매핑되므로 `01000`으로 채워진다.  
offset에는 상수 1200이 매핑되므로 `0000 0100 1011 0000`으로 채워진다.  


따라서,  
$$10001101 \; 00101000 \; 00000100 \; 10110000 _{(2)}$$ 이고,  
이를 hexdecimal(16진수)로 바꾸면  
`0x8d2804b0`이다.  
이와 같은 형태로 machine code가 생성되면서, lw 연산을 수행한다.  
나머지 mips 코드도 마찬가지로 machine code로 번역해주면 된다.  


<h2>3. Logical Operations</h2>  

앞선 Operations 포스트에서 설명 안 한 부분이 있다. 바로 논리 연산이다.  
논리 연산은 다른 고급 언어들과 비슷하다. 하지만, 비트 단위의 논리를 다룬 다는 것이 큰 특징이다. 다음 다섯 가지로 구성되어 있다.   
1. sll
    shift left이다. C와 JAVA에서 모두 '<<' 기호로 사용된다. logical shift left를 하면 `특수한 케이스(unsigned)`에서는 10진수 기준 2배가 된다는 사실은 자명하니 넘어가도록 하자. 일반적으로는 오버플로우가 나기도, 음수로 변환되기도 한다.(signed) 하지만, 일반적으로 logical left shift를 쓰는 이유는 빠른 곱셈을 위해서이다. 덧셈의 loop로 구현된 곱셈은 매우 느리기에 비트 연산을 통해 곱셈을 구현하는 경우가 많다.  
    ```mips
    sll $t2, $s0, 4
    ```
    위 예시 코드는 \\$s0에 저장된 값을 4bit shift left해서 \\$t2에 저장하라는 의미이다.  
    R-format instructions이기 때문에,  
    op - rs - rt - rd - shamt- funct 기준으로 나누면,  
    `000000 00000 10000 01010 00010 000000`와 같은 32bit의 instruction이고, 이를 machine code로 변환하면, `0x00105080`과 같은 값을 얻을 수 있다.  
2. srl
    shift right이다. 여기서의 shift right는 logical shift right를 의미한다. 왜 굳이 logical shift 라고 말하느냐, shift의 종류에는 logical과 arithmetic이 있기 때문이다.  
    우선, shift right를 하면 `특수한 케이스(unsigned)`에서는 10진수 기준 절반이 되는 사실은 저명하니 넘어가도록 하자. 그런데, 앞서 우리는 signed int에 대해서 다뤘었다. 만약, 음의 정수를 1회 right shift를 할 때, 우리는 일반적인 left shift 방식과 동일하게 0을 맨 앞에 채워넣을 수 있다. 이걸 logical right shift라고 한다. 하지만, 음수였던 값을 logical right shift를 하는 순간 무조건 양수가 된다는 사실은 자명하다. 따라서, 부호 보정을 위해 1을 채워넣는 shift를 arithmetic right shift라고 한다.  
    C와 JAVA에서는 logical shift right를 각각 '>>'와 '>>>'로 표기하며, MIPS는 위 연산자를 통해 shift right를 수행한다.  
3. and, andi
    Bitwise AND이다. C와 JAVA에서 모두 '&'로 구현되는 연산자로, 비트의 AND 연산이다.  
    무조건 모두 1이어야 1이라는 결과가 나오는 연산이고, 0이 하나라도 있으면 0이 결과이다.  
    ```mips
    and $t0, $t1, $t2
    ```
    위와 같은 예시로 작성할 수 있다.  
4. or, ori
    Bitwise OR이다. C와 JAVA에서 모두 '|'으로 구현되는 연산자로, 비트의 OR 연산이다.  
    1이 하나라도 있으면 1, 모두 0이어야 0이 나오는 연산이다.  
    andi나 ori는 모두 immediate operand와 함께 쓰이는 연산자이다.  
5. nor
    개인적으로, and나 or 연산과 동일한 operand 개수를 맞추기 위해 만든 instruction이 아닌가 생각을 하는데, NOT이 아니라 NOR인 이유는 NOT (a OR b) 연산이기 때문이다.  
    이는 완전히 not과 동일하다. 왜일까?  
    ```mips
    nor $t0, $t1, $zero
    ```
    nor 연산에 따라 정리하면, NOT (\\$t1 OR \\$zero) == NOT (\$t1)  
    그냥 t1을 bit flip한 값(not 처리한 값)과 완전히 동일한 결과를 도출할 수 있다.  

<h2>4. Program & Instuctions</h2> 
 
1. 일반적으로 instructions는 데이터처럼 binary로 표현되고, instructions나 data는 메모리에 저장된다.  
2. 일반적으로 우리가 의식하지 않지만, 프로그램이 프로그램을 operation한다. 즉, OS위에 compiler를 띄우고 compiler를 이용해 우리의 코드를 컴파일하고 실제 프로그램을 실행하는 걸 생각하면, 그다지 놀라울 일은 아니다.  
3. Binary compatibility(이진 호환성)이라는 것은 명령어를 binary로 취급하게 됨으로써, 동일한 명령어 집합을 사용하는 컴퓨터라면 다른 컴퓨터에서도 해당 프로그램을 컴파일하고 사용할 수 있게 되는 것을 의미한다.  
4. `프로그램을 실행한다는 것은 메모리 상에서 움직인다`는 사실은 저명하며, 가까운 예시로 우리가 C 코드를 짜서 if문을 사용하고, for-loop를 사용하고 function calling을 하는 것 조차 메모리상에서 움직이는 행위가 일어나고 있다. 이를 기계가 이해할 수 있으려면 컴파일러가 Instruction set으로 변환하고 이는 machine-code와 매칭되야 한다. 즉, 우리는 프로그램을 돌려서 우리의 프로그램이 메모리 상에서 어떻게 처리되는지 알아야 하는 것이다. (당장 가벼운 리버싱 경험이 있는 나로서는 굉장히 무서운 말 중 하나이다. ㅎㅎ) 
하지만, 우리가 짠 코드가 메모리 상에서 어떻게 돌아가는지도 모르는 개발자, 컴퓨터 공학자는 화성학도 모르고 작곡하는 작곡가, 엡실론 델타 논법도 모르고 미적분을 하는 수학 전공생과 다를 바가 없다...  
뻘 소리 그만하고 같이 알아보자.  

<h3>Conditional branch instructions</h3>
조건을 분기하는 데 사용하는 MIPS instructions를 소개한다.  
1. beq
    명령어 그대로 받아들이자. branch-if-equal이다.
    ```mips
    beq rs, rt, L1
    ```
    다음과 같은 예시처럼 사용할 수 있다. 여기서 rs와 rt는 레지스터 rs와 rt를 가리키며, rs와 rt가 같으면 L1으로 가라는 의미이다. (MIPS 코드를 앞으로 보다보면, L1: ~~~ 하면서 라벨링된 부분이 있다. 이 부분에 해당하는 문장으로 가라는 뜻이다.)
2. bne
    beq의 반대 버전이다. branch-if-not-equal이다.
    ```mips
    bne rs, rt, L1
    ```
    쉽다. rs와 rt가 다르면 L1으로 가라는 의미이다.

연산자 format을 보면 알겠지만, I-format을 따르는 연산자들이다.  

<h3>Unconditional branch instruction</h3>
조건이 없이 프로그램 흐름을 분기시킬 수 있는 상황이 필요한데,   
이를 위해서 사용하는 mip instruction이 존재한다.  
```mips
j L1
```
말 그대로, L1으로 jump하라는 의미이다.

<h3>Compiling If Statements & Loop Statements</h3>
조건 분기에 사용하는 mips instructions을 배웠으니, 실제 if문과 loop문에 써보자.  
C코드 두 가지를 MIPS instructions로 컴파일해보자.

#### Case1)
```c
if (i == j)
    f = g + h;
else
    f = g - h;

// f, g, h, i, j in $s0, ..., $s4
```
다음과 같은 코드를 직접 컴파일해보자.
```mips
        bne $s3, $s4, ELSE
        add $s0, $s1, $s2
        j   EXIT
ELSE:   sub $s0, $s1, $s2
EXIT: ...
```
J EXIT으로 분기를 직접적으로 빠져나오도록 MIPS 코드가 짜져야 완벽하다!  
첫 코드를 beq로 두고 `IF:`로 이동하도록 컴파일한 코드가 생성될 수도 있다.  

#### Case2)
```c
while (save[i] == k)
    i += 1;
// i in $s3, k in $s5, address of save in $s6
```
MIPS Instructions를 만들어보자.
```mips
LOOP:   sll  $t1, $s3, 2 (i값을 4배)
        add  $t1, $t1, $s6 (save 포인터 주소 + offset($t1) 하면 save[i]의 주소 나옴)
        lw   $t0, 0($t1)
        bne  $t0, $s5, EXIT
        addi $s3, $s3, 1
        j    LOOP
EXIT:   ... 
```
쉽다.  

추가적으로 대소 비교와 관련된 Conditional Operations도 살펴보자.  
```mips
slt rd, rs, rt
slti rd, rs, constant
```
slt는 set-on-less-than이라는 의미로, rs가 rt보다 작을 때, rd에 1을 할당하고 아니면 0을 할당한다. slti는 보이는 것처럼 constant 연산에 쓰인다.  
근데, 왜 beq, bne, slt만 있을까?  
위 조합으로 모든 relative conditions를 나타낼 수 있기 때문이다.  
필요하지 않으면 굳이 만들지 않고 전반적인 성능을 향상시키는 MIPS의 디자인 법칙이 담겨있다.  

추가적으로 unsigned 비교를 하는 sltu와 sltui라는 연산도 있다.  

<h2>5. Procedure Calling & J-Format Instructions</h2> 

<h3>Procedure Calling</h3>  

J-Format을 다루기 전에 꼭 거쳐야 할 관문이다. 앞선 설명을 보고 쉬운데라고 생각했다가, 여기서 큰 코 다칠 수도 있다. 여기서 던질 뻔했다.   

Prodecure란 제공되는 parameter에 따라 특정 작업을 수행하는 서브루틴을 말한다.  
그냥 함수를 다룬다고 생각하면 된다.  

**[Procedure Calling 6단계]**  
1. Caller는 Callee가 접근 할 수 있는 레지스터에 인수를 추가한다.  
2. Caller는 Callee에게 제어를 넘긴다. (=> PC를 이용!)  
3. Callee가 필요로 하는 메모리 자원(stack or register)을 요청하여 얻는다.  
4. Calle가 필요한 연산을 수행한다.  
5. Caller가 접근 가능한 레지스터에 Callee가 연산한 결과 값을 넣는다.  
6. Callee는 Caller에게 제어를 돌려준다.

Procedure에서 Register를 사용하는데, MIPS에서는 32개를 할당한다.  

\\$v0, \\$v1: result value (반환값을 갖게 되는 레지스터 값이다.) - reg #2, #3  
(여기서 반환값이 왜 2개가 필요한 이유는 일반적으로 C언어의 경우 무조건 반환값이 0~1개이므로
레지스터 1개만 필요할 것 같지만, 64-bit 결과값이 return될 수도 있으므로 2개를 만들어 놓았다.)  
\\$a0 ~ \\$a3: arguments (전달할 인수를 저장하는 인수 레지스터 4개이다.) - reg#4~7  
(arguement가 5개, 6개도 가능한데, 4개만 만든 이유는 "Stack Call" 때문이다.)  
\\$t0 ~ \\$t9: temporary registers로, callee가 임시로 쓰는 레지스터이다.  
\\$s0 ~ \\$s7: callee에 의해 저장 용도로 쓰는 레지스터이다.  
\\$gp: static data에 대한 global pointer 용도로 쓰는 레지스터이다.  
\\$sp: stack pointer 용도의 레지스터이다.  
\\$fp: frame pointer 용도의 레지스터이다.  
\\$ra: 호출한 곳으로 되돌아가기 위한 복귀 주소를 가지고 있는 레지스터이다.  

**[Stack]**  
컴파일러가 procedure를 번역하는데 레지스터의 개수가 부족한 경우가 있을 것이다.  
앞서 설명했다시피, argument 관련한 레지스터는 4개 뿐이기에, 추가적으로 프로그램에서 사용하는 변수도 있기에,  
자주 사용되는 변수는 레지스터에, 나머지는 메모리에 저장했다가 필요할 때 꺼내서 레지스터에 넣어 사용하도록 설계되었다.  
이때, 메모리에서 사용하는 LIFO 구조인 Stack을 통해 "Register Spilling"을 한다.  
Register Spilling이란, 자주 사용하지 않는 변수를 메모리에 저장하는 것을 의미한다.  

스택에는 "Stack Pointer"가 존재한다. 이는 가장 최근에 할당도니 주소를 가리키는 포인터로, 
레지스터 값 하나가 스택에 저장되거나 꺼내질 때마다 1 word(4 bytes)씩 조정되는 특징을 가지고 있다.  
스택은 높은 주소에서 낮은 주소 방향으로 성장(?)하므로, 레지스터 값을 넣을 때 \\$sp는 감소, 꺼낼 땐 \\$sp는 증가시켜야 한다.  
```mips
addi $sp, $sp, -4 // push stack
addi $sp, $sp, 4  // pop stack
```

**[MIPS Instructions of Procedure Call & Return]**  
```mips
jal ProcedureLabel
```
해당 프로시져로 이동하기 위해서 mips는 다음과 같은 instruction을 사용한다.  
jump-and-link의 약자로, 지정된 주소로 점프하면서 다음 명령어의 주소를 $ra에 저장하는 명령어이다.  
즉, \\$ra에 PC + 4 값을 저장한다.  
jal은 특이하게 J-Format Instruction이다.(J-Format은 후술할 예정)  

cf. PC란?  
PC란 Program Counter의 약자로, 현재 실행되고 있는 프로그램의 instruction의 메모리 주소를 가지고 있는 레지스터이다.  

```mips
jr $ra
```
jump-register의 약자로, 레지스터에 저장된 주소로 무조건 점프하라는 명령어이다.  
다시 원래 process로 돌아가기 위해, $ra에 저장된 PC+4로 복귀한다.  
(jr은 특이하게도 R-Format을 따른다.)  
\\$ra는 31번째 register를 사용하므로 rs에 31을 넣고 나머지는 0으로 채운다. jr는 func 파트에 8을 넣으므로, `000000 11111 00000 00000 00000 001000`과 같은 기계어로 치환된다.  

**[Leaf Procedure Practice]**  
```c
int leaf_example (int g, int h, int i, int j) {
    int f;
    f = (g + h) - (i + j);
    return f;
}
```
위와 같은 C코드를 MIPS로 번역해보자.  
인수는 위에서 다뤘다시피, \\$a0~\\$a3을 이용하고, f는 \\$s0를 이용한다고 가정해보자.  
당연히, result는 \\$v0를 이용할 것이다.  
```mips
leaf_example:   addi $sp, $sp, -4
                sw   $s0, 0($sp)    //stack 상 만든 공간에 callee에서 사용하는 변수를 저장한다.
                add  $t0, $a0, $a1
                add  $t1, $a2, $a3
                sub  $s0, $t0, $t1
                add  $v0, $s0, $zero  // f를 return 주소에 저장
                lw   $s0, 0($sp)
                addi $sp, $sp, 4
                jr   $ra  // PC+4로 이동하자.
```
**[Non-Leaf Procedure Practice]**  
```c
int fact (int n) {
    if (n < 1) return 1;
    else return n * fact(n - 1);
}
```
위와 같은 C코드를 MIPS로 번역해보자.  
```mips
fact:   addi $sp, $sp, -8
        sw   $ra, 4($sp)
        sw   $a0, 0($sp)
        slti  $t0, $a0,  1
        beq  $t0, $zero, L1
        addi $v0, $zero, 1
        addi $sp, $sp, 8
        jr   $ra
L1:     addi $a0, $a0, -1
        jal  fact
        lw   $a0, 0($sp)
        lw   $ra, 4($sp)
        addi $sp, $sp, 8
        mul  $v0, $a0, $v0
        jr   $ra
```

**[MIPS's Byte/Halfword Operations]**  
C언어에서 string을 처리할 때, 어떻게 처리하는가?  
배열, 포인터, 1byte가 핵심이다.  
바이트와 halfword의 load와 store를 위해서, lb, lbu, sb 같은 연산자를 제공한다.  
```mips
lb rt, offset(rs)  // 32bit sign extend을 수행한다.
lh rt, offset(rs)  // lb의 halfword(=2bytes) 버전이다.
lbu rt, offset(rs) // 32bit zero extend를 수행한다.
lhu rt, offset(rs)
sb rt, offset(rs)  // rightmsot 바이트나 halfword를 offset(rs)에 저장한다.
```  

**[String Copy Practice]**
```c
void strcpy (char x[], char y[])
{
    int i;
    i = 0;
    while ((x[i]=y[i]) != '\0')
        i += 1;
}
```
다음 C코드를 MIPS로 번역해보자.  
```mips
strcpy:     addi $sp, $sp, -4
            sw   $s0, 0($sp)
            add  $s0, $zero, $zero
L1:         add  $t1, $s0, $a1
            lbu  $t2, 0($t1)
            add  $t3, $s0, $a0
            sb   $t2, 0($t3)
            beq  $t2, $zero, L2
            addi $s0, $s0, 1
            j    L1
L2:         lw   $s0, 0($sp)
            addi $sp, $sp, 4
            jr   $ra
```

cf. 32-bit Constants  
대부분의 상수들은 I-format의 16비트만으로도 충분하다.  
가끔 32비트 크기의 큰 상수들을 저장해야 할 때, 다음 연산자들을 활용한다.  
```mips
lui $s0, 61
ori $s0, $s0, 2304
```
다음과 같은 mips 코드가 있다고 했을 때,  
\\$s0에는, `00000000 01111101 00000000 00000000`가 저장되며 왼쪽 16bit만을 사용해 저장했다.  
2304는 `00001001 00000000`으로 16비트에서 나타낼 수 있고, \\$s0의 오른쪽 16bit를 ori 연산을 활용해 추가하면,  
`00000000 01111101 00001001 00000000`이 되며, 큰 상수를 다룰 수 있다.  

**[Branch Addressing]**

지금까지 살펴봤던 MIPS 명령어 중 beq, bne는 비교하고서 L1, L2 등으로 이동하는 형태였다.  
beq, bne는 I-format instruction이기 때문에 알다시피 아래와 같은 형식을 가지고 있다.  

|   op   |   rs   |   rt   | constant or address |
| :----: | :----: | :----: | :-----------------: |
| 6 bits | 5 bits | 5 bits |       16 bits       |

여기서 알아둬야 할 branch addressing과 관련된 몇 가지 사실들이 있다.  
1. 대부분의 분기의 목적지는 분기 명령 근처에 위치하도록 설계되어있다.  
   더 정확히 말하자면, 현재 명령의 PC 근처 앞/뒤에 존재한다.  
   위와 같은 방식을 PC-relative-addressing이라고 한다.  
   분기의 목적지인 target address는 `PC + offset * 4`와 같다.  
   여기서, offset은 16bits로 구성된 I-format의 address 부분이다.  
   16비트로 구성되었고 signed 이기 때문에 $±2^{15}$ words, 즉, $±2^{15}$ instructions 범위 내에서 분기될 수 있다.  
   즉, $±2^{17}$bytes, `±128KB` 범위 내에서 분기될 수 있다.  
> 사실, PC는 현재 명령어 기준으로 +4 된 PC+4 값이 PC에 저장되어 있기 때문에,  
실제 Target Address = (PC+4) + offset*4이다.  

<h3>J-Format Instructions</h3>  

J-Format Instruction의 대표 명령어는 j와 jal이다.  
점프의 목적지는 text segment 내의 어디든 될 수 있다.  
PC에서 멀리 떨어져 있을 수도 있고, J-Format을 활용해 정확한 전체 주소를 instruction에 표현할 수 있다.  
$2^{26}$ words (= $2^{28}$ bytes) 내에서 어디로든 jump 할 수 있다.  

|   op   | constant or address |
| :----: | :-----------------: |
| 6 bits |       26 bits       |

주소를 저장할 때, 오른쪽으로 두 번 쉬프트된 값이 저장되기 때문에, 주소의 28비트를 기억하고 있는셈이다.  
**[Pseudo Direct Jump Addressing]**
- `J-Format 상에서 26bit만으로 어떻게 32bit 주소체계에 접근하는가`에 대한 답변이 바로 Pseudo Direct Jump Addressing이다.  
- Target Address = address * 4 이다. 즉, address 값에 left shit 두 번을 한다.  
- 이렇게 해서, 28bit를 채웠다면, 나머지 4bit는 어떻게 채우는가?  
- 나머지 4bit는 PC의 bits에서 Top 4 bits(PC_31, 30, 29, 28 bit)를 가져온다. 
- 예시를 통해 설명하면 다음과 같다. address에 LOOP의 주소값/4인 20000를 저장하면,  
    `000010 00 00000000 01001110 00100000`과 같은 J-Format instruction이 만들어진다.  
    이때, 주소인 `00 00000000 01001110 00100000`에 left shift 두 번을 하면,  
    `0000 0000 0001 0011 1000 1000 0000`와 같이 28bit가 만들어지며,  
    PC를 `00000000 00000001 00111000 10011000`이라고 할 때, 상위 4bits인 0000을 주소에 가져온다.  
    최종적으로 `address = 00000000 00000001 00111000 10000000`이 jump할 주소인 것이다.  

cf. bne, beq의 PC-relative-addressing과 비교해서 공부할 필요가 있다.  
PC-relative-addressing은 I-Format Instruction의 offset에 저장된 값을 이용하며,  
target address = `PC + offset * 4`  

**[Branching Far Away]**  
만약, 분기의 목적지가 16bit offset(I-format such as bne, beq)을 표현하기에 너무 멀리 있다면,  
컴파일러가 코드를 재작성한다. 예를 들어,  
```mips
beq $s0, $s1, L1
```
L1이 너무 멀리 있으면,  
```mips
    bne $s0, $s1, L2
    j   L1
L2: 
```
다음과 같이 변환되기도 한다.  

<h3>[Addressing Mode 총정리]</h3>  
그림 추가 예정!!!