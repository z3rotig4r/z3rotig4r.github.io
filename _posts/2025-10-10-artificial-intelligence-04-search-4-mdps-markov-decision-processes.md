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



 

### What is MDPs  

상태(s) 집합: S  
action(a) 집합: A  
transition function T(s, a, s') = P(s' | s, a): 상태 s에서의 행동 a가 상태 s'으로 바꾸는 확률을 나타냄  
reward function R(s, a, s')  
start state  
Dicount factor, horizon 등  

위의 요소들은 MDP를 구성한다.  

MDP는 noisy movement를 가정한다.  
이는 non-deterministic한 상황을 가정하는 것으로, Transition function 값이 1.0이 아닌 확률  ($0 \leq P < 1$)을 갖는다.  

Reward function R(s, a, s')는 어떤 Transition이 발생했을 때의 Reward로,  
어떤 미로 게임에서 terminal state에 도달했을 때, R((4,3), any action, terminal) = +1.0 처럼 목표지점에 도달 시에 보상을 주거나, R(s, any action, s') = -0.1 처럼 매 움직임에 패널티를 부여하는 Reward function도 가능하다.  

이러한 non-deterministic search problem에서는 Expectimax Search도 가능하나, 차이점이 존재한다.  
Expectimax는 현재 상태에서의 최적의 행동을 탐색하는 것이고, MDPs는 모든 상태에 대한 최적의 Policy를 계산한다.  

`Markov Property`: the future and the past are independent given the present  
Future is only affected by a current state.  
이 말인 즉슨, 현재는 모든 과거를 온전히 표현한다(history를 가짐)는 말과 동일하며,  
미래 transition에 영향을 주지 않는다는 말이기도 하다.  
아래 수식으로 표기된다.  
$$P(s_{t+1} | s_t) = P(s_{t+1} | s_t, s_{t-1}, \dots, s_1)$$  

Deterministic search(A*/BFS/DFS/...)는 optimal plan(행동의 순서)을 찾는 것이 목표이다.  
이와 달리, MDP는 최적의 policy를 원한다.($\pi^{*}: S \rightarrow A$)  
각 state마다 policy가 존재하는데 policy는 모든 상태(S)에 대해 어떤 행동(A)를 해야 할지 알려주는 것으로, optimal policy는 기대되는 utility값을 최대화하는 policy를 말한다.  

Expectimax는 policy를 구하지 않는다.(현재 상태에서 어떤 행동을 하는지에 대해 기대값이 가장 높은지만을 판단)  
이와 달리 MDP는 모든 상태 s에 대해 optimal policy를 전부 계산해서 policy를 만든다.   

optimal policy는 주어진 mdp 설계 방식에 영향을 받는다.  

## 2. Components of MDP  
MDP는 MDP Search Tree를 통해 구조화할 수 있다.  



## 3. Policy  


## 4. Discount Factor  


## 5. Value Iteration  