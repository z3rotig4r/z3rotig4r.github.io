---
layout: post
title: "[Artificial Intelligence] 02. Search (2): informed search"
date: 2025-10-07 13:10 +0900
description: RL(강화학습)의 토대인 탐색 알고리즘, 특히 정보가 주어진 상황(heuristic 기반) 다룹니다.
image:
  path: assets/img/contents/AI/a_star.png
  alt: A* search
category: [Computer Science, RL]
tags: [search, tree, graph, heuristics, A*, graph search]
pin: false
math: true
mermaid: true
toc: true
---  

앞서 살펴봤던 UCS를 informed search에 맞게 알고리즘을 수정해보고, graph search에 대해 알아보자.  

## 1. Informed Search: Heuristics  
**Heuristic(휴리스틱)**, $h(x)$: 하나의 상태가 goal(목표)에 얼마나 가까운지를 추정(estimate)하는 함수  
특정 탐색 문제를 위해 설계되는 함수이고, manhattan distance, euclidean distance 등이 그 예이다.  
다양한 문제에 맞게 휴리스틱 함수를 설계하는 것이 중요하다.  

## 2. Greedy Search  
`Strategy that select a node with least heuristic value`  
가장 작은 휴리스틱 값을 가지는 노드를 항상 선택하여 탐색하는 알고리즘이다.  
즉, goal state와 가장 가깝다고 **생각되는** 노드를 선택하여 **빠르게** 탐색하려는 알고리즘이다.  
하지만, 대부분 최적의 결과를 가져다 주지 않고, 최악의 경우 badly-guided DFS처럼 행동한다.  
즉, Optimality X, Completeness X  

## 3. A* Search  
**UCS의 안정성과 Greedy의 효율성을 결합한 알고리즘**  
$g(n)$: UCS를 통한 축적된 비용. 즉, 과거 비용(backward cost)를 나타냄  
$h(n)$: Greedy를 통한 휴리스틱 값이자 goal proximity(목표화 현재 상태의 거리). 즉, 미래 추정 비용(forward cost)를 나타냄  
A* search는 위 두 값의 합을 통해 최적의 경로를 탐색한다.  
$$f(n) = g(n) + h(n)$$  
두 값의 합이 작은 노드들을 선택하여 탐색하는 것이다.  

### A* search의 종료  
단순히 목표 노드(G)를 프론티어에 enqeue(추가)했을 때 멈추면 안 되고, 목표 노드를 dequeue(꺼냄) 때 종료해야 함  


### A* search의 Optimality  

### Admissible Heuristics  



## 4. Heuristics Design  


## 5. Graph Search  



