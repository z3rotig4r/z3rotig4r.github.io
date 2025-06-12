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
pin: true
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
3. 두번째 for문(negative cycle 확인용): O(E)  


## SSSP(SSP) in DAG  

