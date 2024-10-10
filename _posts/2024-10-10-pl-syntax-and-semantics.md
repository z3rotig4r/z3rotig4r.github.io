---
layout: post
title: "Concepts of Programming Languages 03: Describing Syntax and Semantics"
date: 2024-10-10 06:26 +0900
description: 
image:
  path: /assets/img/contents/pl_syntax.png
  alt: Ambiguous Expression Grammar
category: [Computer Science, Concepts of Programming Languages]
tags: [Programming Languages, Syntax]
pin: false
math: true
mermaid: true
toc: true
---

<h2>1. Intro</h2>  
> Syntax(구문): 프로그래밍 언어의 문법이나 구조를 의미  

> Semantics(의미론): Syntax에 대한 의미  

- Syntax와 Semantics는 언어의 정의를 제공한다.
- 잘 설계된 언어라면 그 의미는 구문으로부터 파악이 가능해야 한다.

- Sentence: alphabet으로 구성된 문자열
- Language: Sentences(문장)의 집합
- Lexeme(어휘): 가장 낮은 수준의 구문 단위 (ex. *, sum, begin)
- token: 어휘의 카테고리 (ex. identifier)  

**[Lexeme와 Token 구분 예시]**  
`index = 2 * count + 17;`  

| Lexemes |   Tokens    |
| :-----: | :---------: |
|  index  | identifier  |
|    =    | equal_sign  |
|    2    | int_literal |
|    *    |   mult_op   |
|  count  | identifier  |
|    +    |   plus_op   |
|   17    | int_literal |
|    ;    |  semicolon  |

<h2>2. BNF & Context-Free Grammers</h2>  
> BNF(Backus-Naur Form)은 Context-Free Grammers와 동일한 의미이다.  

BNF란 놈 촘스키에 의해 개발된 문맥 자유 언어이며, context에 상관 없이 동일하게 해석되는 문법을 가진 언어를 말한다.  
즉, 반드시 하나의 문장이 하나의 의미를 지녀야 한다.  

<h3>BNF Fundamentals</h3>  
1. Terminal: lexeme나 token을 칭하는 용어이다.  
2. Non-Terminal: Terminal이 아닌 것을 의미하며, '<>'(angle brackets)에 싸여있다.  
3. 규칙은 LHS(Left-Hand-Side)와 RHS(Right-Hand-Side)로 구성된다. 예를 들어, `<assign> → <id> = <expr>`이라는 규칙이 존재하면 LHS는 <assign>이며, RHS는 <id> = <expr> 이다. LHS는 무조건 Non-Terminal이 와야 하며, RHS는 하나 이상의 Non-Terminal, Terminal이 모두 올 수 있다.  
  `<stmt> → <single_stmt> | begin <stmt_list> end`와 같은 표현이 가능하다.  해당 규칙의 의미는 <stmt>이라는 nonterminal이 single_stmt라는 nonterminal로 확장되거나, begin <stmt_list> end라는 nonterminal과 terminal의 조합으로 확장될 수 있다는 의미이다.  
1. 
2. 문법은 이러한 규칙들의 공집합이 아닌 유한 집합으로 표현된다.  
3. Start Symbol은 처음 derivation이 시작되는 Non-Terminalㅇ르 말한다.  

<h2>3. Parse Tree & Ambiguity in Grammers</h2>  
<h2>4. EBNF</h2>
<h2>5. Semantics</h2>  
<h3>Operational Semantics</h3>  
<h3>Axiomatic Semantics</h3>  
<h3>Denotational Semantics</h3>  
