---
layout: post
title: "[Algorithm] 12. Shortest Path (2): Bellman-Ford's Algorithm & DAG"
date: 2025-06-05 15:06 +0900
description: Bellman-Ford 알고리즘에 대해서 다룹니다.
image:
  path: assets/img/contents/Algorithm/bell-fordman_algorithm.png
  alt: Bellman-Ford Algorithm
category: [Computer Science, Algorithm]
tags: [Bellman-Ford, SSSP]
pin: false
math: true
mermaid: true
toc: true
---

## Bellman-Ford's Algorithm  
SSP (혹은 SSSP) 문제를 푸는데, 가장 일반적인 알고리즘이다.  
edge의 weight가 음수여도 된다.  

```
BELLMAN-FORD(G, w, s)
  INIT-SINGLE-SOURCE(G, s)
  for i=1 to |G.V|-1
    for each edge (u, v) ∈ G.E
      RELAX(u, v, w)
  for each edge (u, v) ∈ G.E
    if v.d > u.d + w(u, v)
      return FALSE
  return TRUE
```   

### Time Complexity of Bellman-Ford's Algorithm  
1. INIT-SINGLE-SOURCE: $O(V)$
2. 첫번째 for문: $O(VE)$
3. 두번째 for문(negative-weight cycle 확인용): O(E)  

### Correctness  
Directed Graph `G=(V, E)`와 source vertex `s`, weight function `w`가 주어졌을 때,  
제대로 된 Bellman-Ford라면, s로부터 reachable한 `negative-wegiht cylcle`이 없을 때, TRUE를 반환하고,  
반대로 s로부터 reachable한 `negative-weight cycle`이 있다면, FALSE를 반환해야 한다.  

Lemma 1. 만약 s에서 reachable한 negative-weight cycle이 없다면, for loop |V|-1 번 돌렸을 때, $\delta(s, v)$ 즉, 모든 정점 v에 대해 최단 거리가 정확히 저장된다.  
p를 최단경로라고 가정하고, 최단경로는 simple path이기 때문에 최대 |V|-1 개의 간선만 포함한다.  
|V|-1번 모든 간선을 Relaxing하면, 최단 경로가 완성된다. (=> Path Relaxation Property)  

## SSSP(SSP) in DAG  
DAG(Directed Acyclic Graphs)에서도 SSSP 문제를 만들 수 있다.  

```
DAG-SHORTEST-PATHS(G, w, s)
  topologically sort the vertices of G
  INITIALIZE-SINGLE-SOURCE(G, s)
  for each vertex u, taken in topologically sorted order
    for each vertex v ∈ G.Adj[u]
      RELAX(u, v, w)
```  

topology sort 는 DFS에 따라 $O(V+E)$의 시간복잡도를 가지고,  
INITIALIZE-SINGLE-SOURCE(G, s)는 $O(V)$의 시간복잡도를 가지며,  
중첩된 for문은 $O(V+E)$의 시간복잡도를 가진다.  

### PERT 차트  
간선은 수행해야 하는 작업을 나타내고,  
간선의 가중치는 특정한 작업을 수행하는데 필요한 시간을 나타낸다.  
DAG를 통한 path는 특정 순서에 따라 수행해야하는 일련의 작업들을 나타낼 수 있고,  
critical path는 DAG에서 가장 긴 path이다.  
모든 작업을 수행하는데 필요한 총 시간의 lower bound이다.  
여기선 longest path를 찾기 때문에 shortest path 문제가 아니지 않나 생각하겠지만,  
가중치의 부호를 바꾸면 shortest path 문제로 바뀐다.  
단순하게 생각하면 된다.  