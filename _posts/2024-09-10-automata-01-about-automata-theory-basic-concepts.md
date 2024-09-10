---
layout: post
title: 'Automata 01: About Automata Theory & Basic Concepts'
date: 2024-09-10 10:56 +0900
description: 
category: [Computer Science, Automata]
tags: [automata, formal-language]
image:
    path: /assets/img/contents/automata_intro.png
    alt: automata_intro
pin: false
math: true
mermaid: true
toc: true
---

> 오토마타에 대해서 배우기 전, '집합론과 함수', '자료구조(그래프이론 및 트리구조에 대한 이해)', '귀류법 및 귀납법' 에 대한 사전 지식이 필요합니다.  
{: .prompt-info } 

# 1. Automata Theory란?
`오토마타 이론`은 계산 능력이 있는 추상 기계와 그 기계를 통해 풀 수 있는 문제들을 연구하는 분야입니다.  
여기서 `오토마타(Automata)`는 `Automaton`은 복수형으로, 계산 능력이 있는 자동화된 __추상__ 기계, __수학적__ 기계를 의미합니다.  
Wikipedia에 따르면, "대상의 어떤 기능에 주목하여 입력과 내부 출력 각 신호의 상호관계를 수학 모델로 옮기고, 이 모델을 수학적으로 고찰하여 결론을 유도하는, 내린 결론은 원래 대상에 맞는 다른 문제들을 해석하는 과정에 관여할 수 있도록 하는 학문"이라고 표현할 수 있습니다.  
`컴파일러`, `인공지능`, `컴퓨팅 이론`, `컴퓨터 구조 설계` 등 다양한 분야에 이용되는 이론입니다.  

오토마타를 이해하기 위해선 컴퓨팅 이론에서의 3가지 중요한 개념에 대해 알아볼 필요가 있습니다.
![automata_intro](/assets/img/contents/automata_intro.png)

# 2. Computation Theory 3요소
1. **Automata (오토마타)**  

    디지털 컴퓨터의 추상적 모델을 의미합니다.  

2. **Formal Language (형식 언어)**  

    심볼(Symbol)의 집합으로 구성된 알파벳(alphabet)으로 구성된 문자열의 집합을 의미합니다.  
    예를 들어, 기계어의 경우, {01, 0011, 000111, ...}이 해당한다고 볼 수 있습니다.  
    Automaton M이 언어 L의 집합 원소를 모두 포함할 때, `Automaton M이 언어 L을 인식한다`고 표현합니다.

3. **Grammer (문법)**  

    형식 언어를 정의하는 매커니즘입니다.  
    문법의 규칙 집합들을 기반으로 형식 언어가 생성됩니다.
   
# 3. (Formal) Language의 구성 요소
앞으로는 형식 언어(Formal Language)를 줄여서 그냥 `언어`라고 표현하겠습니다.  
언어를 이해하기 위해서는 아래 세 가지 요소들을 살펴봐야 합니다.

1. Symbol(심볼)  
    언어를 이루는 가장 기본적인 요소입니다. 예를 들어, 한글의 자음&모음, 영어의 알파벳 문자, 0~9까지의 숫자 등을 생각하시면 됩니다.  

2. Alphabet(알파벳)  
    심볼의 공집합이 아닌 집합입니다. 유한해야 합니다.  
    예를 들면,  
    binary alphabet으로 {0, 1};
    English alphabet으로 {a, ..., z};  
    한글의 자음을 alphabet으로 {ㄱ, ㄴ, ㄷ, ..., ㅎ};  
    생각해볼 수 있습니다. 

    \\[x+y=a\\] 

3. String(문자열)



-- 수정 중 (24.09.10.) --

# 4. 

# 5. 