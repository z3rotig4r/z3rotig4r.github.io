---
layout: post
title: "[Algorithm] 10. Minimum Spanning Tree"
date: 2025-06-05 15:05 +0900
description: Minimum Spanning Tree와 대표적인 알고리즘인, Kruskal과 Prim 알고리즘을 다룹니다.
image:
  path: assets/img/contents/Algorithm/mst.png
  alt: Minimum Spanning Tree
category: [Computer Science, Algorithm]
tags: [MST, Kruskal's Algorithm, Prim's Algorithm]
pin: false
math: true
mermaid: true
toc: true
---

## Minimum Spanning Tree(MST)  
**Spanning Tree란?**  
> `Acyclic`하고 그래프 내의 `모든 정점들이 연결`된 트리  
{: .prompt-info}  
Spanning Tree는 그래프를 `span`한다고 표현한다.  

n개의 정점이 그래프에 있다면, n-1개의 edge를 가지는 spanning tree가 생성된다.  

**그러면, MST란?**  
> 모든 spanning tree 중에서 가중치의 합이 최소가 되는 spanning tree를 말한다.  
{: .prompt-info}  

edge (u,v)의 가중치는 $w(u, v)$로 표현하며,  
MST는 unique한 값이 아닐 수 있다. (= MST는 여러 개의 다른 모양으로 나올 수 있다.)  

**사용 예시**  
실생활에서 Network 설계 시에 많이 사용한다.  
Cable network에서 설치 및 유지보수 비용을 최소화할 수 있는지,  
Transportation network나 Water Supply network 등도 이에 해당한다.  

### Problem Definition  
G=(V, E)는 E에 가중치 함수 w가 실함수인 undirected graph라고 하고,  
G 상에서 모든 정점들이 연결된 MST를 찾는 것이 목표이다.  

### Properties of MST  
MST는 항상 `|V|-1`개의 edge를 가진다.  
절대 Cycle을 가지지 않는다.  
Unique할 필요는 없다.  

### Generic Solution to the MST Problem  
목표는 MST를 구성하는 Edge 집합 A를 만드는 것임.  
A를 empty set으로 설정하여 초기화 해주고, 각 반복(iteration)에 Safe Edge인 (u, v)를 추가한다.  
edge (u,v)가 safe 하다는 말은, A ∪ {(u, v)}가 MST인 T의 subset인 것과 동치이다.  
A는 MST인 T를 형성하는 하나의 edge에 의해서 하나의 edge를 만들어 내면서 집합을 키워나간다.  
따라서, A는 항상 MST인 T의 subset이다.  

```
GENERIC-MST(G, w)
  A = ∅
  while A does not form a spanning tree
    find a edge (u, v) that is safe for A
    A = A ∪ {(u, v)}
  return A
```  

그러면 Safe Edge를 어떻게 찾을까?  
edge (u, v)가 그래프 상의 모든 edge 중에서 가장 최소의 weight를 가지는 간선이라고 하고, S를 정점 u를 포함하지만 v를 포함하지 않는 부분집합이라고 하자.  
MST를 만들기 위해서, 집합 S와 V-S는 적어도 하나의 edge로 연결되어야 하는데, 이때 당연히 (u, v)가 연결되어야 하고, 이건 safe하다고 말한다.  

즉, Safe Edge(안전 간선)은 그래프 전체 정점을 포함하는 두 개의 부분집합을 잇는 가장 작은 가중치를 가진 간선이다.  

### Terminologies of MST  
- Cut: 그래프에서 정점들을 두 개의 부분집합인 (S, V-S)로 나누는 행위를 말한다.  
- Cross: edge(u, v)가 cut(S, V-S)에서 S에서 V-S로 edge를 연결하는 것을 말한다. 두 집합이 교차한다고 표현한다.   
- Respect: 어떤 간선에 대한 부분집합 A가 `Respect`이라는 것은 cut에서 A가 cross하는 간선이 존재하지 않는 상황을 말한다.  
- Light: edge가 `light`하다는 것은 cut을 crossing하는 모든 간선 중 가중치가 최소인 간선을 말한다.  

## Theorm & Corollary of MST  

### Theorem
정리 1. 연결된 undirected graph G=(V, E)와 가중치 함수 w가 있을 때, A가 어떤 MST에 포함된 간선 집합이고, cut(S, V-S)가 A를 respect한다면, cut을 넘는 light edge (u, v)는 A에 safe하다. 즉, A ∪ {(u, v)}는 어떤 MST의 부분집합이 됨.  

MST를 점진적으로 만들 때, cut을 넘는 가장 최소 가중치를 가진 간선은 항상 MST에 포함됨  

그렇다면, 어떤 간선이 A에 대해 safe하다면, 그 간선은 cut을 crossing하는 light edge일까?  
답은 항상 참이 아니다.  

### Corollary
G=(V, E), A가 어떤 MST의 부분집합일 때, $G_A = (V, A)$에서 연결 성분 $C=(V_c, E_c)$가 있고, C와 다른 성분을 연결하는 light edge(u, v)는 A에 안전  


## Kruskal's Algorithm  
**한줄요약**  
> 그래프 내의 모든 edge에 대한 weight를 오름차순으로 정렬해서, acyclic한 상태를 유지하도록 edge를 작은 것부터 하나씩 선택해 MST를 만드는 알고리즘이다.  
{: .prompt-danger}  

```
MST-KRUSKAL(G, w)
  A = ∅
  for each vertex v ∈ G.V
    MAKE-SET(v)
  sort the edges of G.E into nondecreasing order by weight w
  for each edge (u,v) ∈ G.E, taken in nondecreasing order by weight
    if FIND-SET(u) ≠ FIND-SET(v)
      A = A ∪ {(u, v)}
      UNION(u, v)
  return A 
```  
이때도 마찬가지로, |A|(= edge 집합 원소 개수)는 |V|-1과 같다.  

## Prim's Algorithm  
**한줄요약**  
> 임의의 root r에서 시작해서 set A (edge 집합)에 대해 cut($V_A, V-V_A$)를 crossing하는 light edge를 추가해 나가면서 MST를 만드는 알고리즘이다.
{: .prompt-danger}  

```
MST-PRIM(G, u, r)
  for each u ∈ G.V
    u.key = ∞
    u.π = NIL
  r.key = 0
  Q = G.V
  while Q ≠ ∅
    u = EXTRACT-MIN(Q)
    for each v ∈ G.Adj[u]
      if v ∈ Q and w(u, v) < v.key
        v.π = u
        v.key = w(u, v)
```  