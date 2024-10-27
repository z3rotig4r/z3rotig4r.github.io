---
layout: post
title: 'Computer Architecture 03: Arithmetic for Computers (1) - add, sub, mul and div'
date: 2024-10-19 14:23 +0900
category: [Computer Science, Computer Architecture]
tags: [comp_arch, arithemetic]
pin: false
math: true
mermaid: true
toc: true
---

<h2>1. Addition & Subtraction of Integer</h2>  
1) 덧셈  
비트로 변환하여 더한다.  
1) 뺄셈  
피연산자(operand)의 부호를 바꿔 덧셈으로 연산한다.(Add negation of second operand)  

**[Overflow]**  
1) 양수와 음수의 덧셈은 오버플로우가 발생하지 않는다.  
2) 양수와 양수의 덧셈은 Sign bit가 1인 경우 오버플로우가 발생한다.  
3) 음수와 음수의 덧셈은 Sign bit가 0인 경우 오버플로우가 발생한다.  
4) 양수와 양수, 음수와 음수의 뺄셈은 오버플로우가 발생하지 않는다.  
5) (음수 - 양수)은 Sign bit가 0인 경우 오버플로우가 발생한다.  
6) (양수 - 음수)은 Sign bit가 1인 경우 오버플로우가 발생한다.  

**[오버플로우의 처리]**  
C와 같은 경우 오버플로우를 무시하고 그대로 계산을 진행한다.  
MIPS의 addu, addui, subu instructions를 사용하며,  
프로그래머가 항상 신경쓰고 주의해야 한다.  

Ada, Fortran의 경우 예외처리를 한다.  
add, addi, sub와 같은 MIPS instructions를 사용한다.  
오버플로우가 일어나면, exception handler가 작동한다.  
PC(Program Counter) 레지스터의 값을 EPC 레지스터에 저장하고,  
미리 정의된 handler address로 점프한다.  
처리를 마치고 연산을 지속하기 위해 mfc0 명령을 이용행 EPC 값을 되돌린다.  

<h2>2. Multiplication</h2>  
Multiplicand  
Multiplier  

Product  

**[]**  
multiplication은 많은 cycle을 돌기 때문에, 느리다.  
Y = 4 * X와 같이 곱셈 연산을 하지 말고, Y = X << 2 처럼 shift left 연산을 하자.  
아니면, Y = 2 * X와 같은 연산보단, Y = X + X이 훨씬 빠르다.  
따라서, multiplication은 최대한 피하는 것이 좋다.  

**[더 빠른 Multiplier]**  
1 cycle에 끝낼 수 있는 회로가 있지만, 매우 비싸기 때문에 tradeoff가 있다.  

**[MIPS Multiplication]**  
HI: 
LO:

<h2>3. Division</h2>  

<h2></h2>  
