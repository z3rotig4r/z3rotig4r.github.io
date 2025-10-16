---
layout: post
title: "[Artificial Intelligence] 04. Search (4): MDPs(Markov Decision Processes)"
date: 2025-10-10 16:41 +0900
description: 비결정론적 게임을 가정하고, 상대 에이전트에 대한 불확실성을 기대하는 탐색 알고리즘인 MDPs에 대해 알아봅니다.  
category: [Computer Science, Reinforcement Learning]
tags: [adversarial search, alpha-beta pruning, minimax, expectimax]
pin: false
math: true
mermaid: true
toc: true
---

## 1. Uncertainty & What is MDPs?  



Non-deterministic => Expectimax Search로도 가능  

### What is MDPs  
Markov: the future and the past are independent given the present  
Future is only affected by a current state.  
$$P(s_{t+1} | s_t) = P(s_{t+1} | s_t, s_{t-1}, \dots, s_1)$$  


Expectimax는 policy를 연산? 반은 맞고 반은 틀림 (완전한 policy 연산 하지는 않음)  

optimal policy는 given mdp design에 영향 받음

## 2. Components of MDP  


## 3. Policy  


## 4. Discount Factor  


## 5. Value Iteration  