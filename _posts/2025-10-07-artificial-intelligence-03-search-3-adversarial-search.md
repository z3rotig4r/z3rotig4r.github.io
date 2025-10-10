---
layout: post
title: "[Artificial Intelligence] 03. Search (3): adversarial search"
date: 2025-10-07 16:31 +0900
description: 두 개 이상의 에이전트가 서로 적대적인 관계를 가정하고 탐색하는 문제에 대해서 다룹니다.  
category: [Computer Science, RL]
tags: [adversarial search, alpha-beta pruning, minimax, expectimax]
pin: false
math: true
mermaid: true
toc: true
---  
## 1. Types of Games  
인공지능이 다루는 다양한 게임들이 있고, 이를 아래와 같은 기준들(Axes)로 구분할 수 있음  
- Deterministic or Stochastic  
- Player 수  
- 제로섬 게임인지? (한 플레이어의 이득이 다른 플레이어의 손실과 정확히 일치하는 게임)  
- 완전 정보인지? (바둑처럼 모든 정보를 알고 있는지, 아니면 포커처럼 일부 정보가 가려져 있는지)  

이렇게 다양한 게임들 속에서도 목표는 한 가지  
각 state 에서 적절한 움직임을 결정하는 strategy(=policy)를 달성하기 위한 알고리즘을 찾는 것  

### Deterministic Games(결정론적 게임)  
이 포스트에서 다룰 부분은 결정론적 게임으로,  
다음과 같은 구성요소를 가진다.  
- States: S (+ start state $s_0$)  
- Players: $P = \{1, 2, \dots, N \}$ (일반적으로 턴제)  
- Actions: A (플레이어 의존적 혹은 state 의존적)  
- Transitions: $S \times A \rightarrow S$  
- Utilities: $S \times P \rightarrow R$ (특정 플레이어가 가지는 특정 상태가 그 플레이어에게 얼마나 유리한지를 나타낸 실수 값)  
- Goal test: $S \rightarrow \{T, F\}$  

Goal: Policy ($S \rightarrow A$)를 가지는 플레이어에 대한 해를 찾는 것  

### Zero-Sum Games(제로섬 게임)  
에이전트들은 서로 반대되는 유틸리티를 가지며, 한 에이전트가 유틸리티를 최대화하려고 한다면, 다른 에이전트는 유틸리티를 최소화하려 한다.  

## 2. Minimax Adversarial Search  

### Game Tree  
![single-agent-game-tree](assets/img/contents/AI/value_of_states.png)  
우선, 위와 같은 single-agent에 대한 game tree를 생각해보자.  
혼자 플레이하는 게임의 모든 가능한 진행 경로를 트리 구조로 나타낸 것이다.  
각 노드는 게임의 각 상태를 나타내며, edge(간선)은 에이전트의 action을 의미한다.  
terminal nodes는 게임이 끝나는 최종 상태를 나타내며, 각 terminal nodes는 결과에 대한 명확한 점수(=유틸리티)를 가진다.  
이때의 목표는 최상의 결과를 기준으로 판단하며, 가장 높은 최종 점수(유틸리티)를 얻는 것이다.  

**Value of a state: V(s)**  
non-terminal states (트리 상의 internal nodes) => 자식 노드들의 V(s) 중 가장 큰 값을 취한다.  
terminal states: utilities에 따라 계산한 알려진 값을 취한다.  

![adversarial game tree](assets/img/contents/AI/adv_game_trees.png)  
위처럼 적대적 게임인 경우, 상대 에이전트는 플레이어의 유틸리티를 최소화하려고 할 것, 이때 state value를 구하는 방법? => **Minimax Value**  
적대적 게임의 간단한 특성을 활용한다.  
에이전트는 유틸리티를 최대화하려 할 것이고, 반대로 상대 에이전트는 유틸리티를 최소화하려 할 것이다.  
따라서, agent's control을 받은 state들에는 successor(후임 노드)에서 max 값을 취하고, opponent's control을 받는 state들에는 successor에서 min 값을 취한다.  
위 예시의 경우 빨간색 opponent's control을 받는 state에서는 왼쪽은 -8, 오른쪽은 -10을 취하게 될 것이며,  
이에 따라 루트 노드인 start state는 -8을 state value로 취한다.  

### Minimax Adversarial Search  
**Deterministic하고, 제로섬 게임을 가정한다.**  
eg. 틱택토, 체스, 오목(Go)  
한 플레이어는 결과를 최대화하려하고, 상대 플레이어는 결과를 최소화하려 한다.  
각 플레이어는 차례를 번갈아 가진다.  

**Minimax Search**  
state-space search tree로 나타낸다.  
합리적인(=optimal) adversary를 가정하고, 그에 대항하는 가장 좋은 성취 가능한 유틸리티인 각 노드의 minimax 값을 계산한다.  

**구현**  
```python
def max_value(state):
    initialize v = - ∞  
    for each successor of state:
        v = max(v, min_value(successor))
    return v
```  
```python
def min_value(state):
    initialize v = + ∞
    for each successor of state:
        v = min(v, max_value(successor))
    return v
```  
```python
def value(state):
    if the state is terminal:
        return the utility
    if the next agent is MAX:
        return max_value(state)
    if the next agent is MIN:
        return min_value(state)
```  

## 3. Improving the efficiency of Minimax: Alpha-Beta Pruning  


## 4. Depth-limited search & Evaluation function  


## 5. Expectimax Adversarial Search  
상대방이 최적이 아닌, 확률적으로 움직이는 것을 `기대`  
