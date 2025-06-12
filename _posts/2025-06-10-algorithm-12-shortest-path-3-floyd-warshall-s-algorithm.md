---
layout: post
title: "[Algorithm] 12. Shortest Path (3): APSP & Floyd-Warshall's Algorithm"
date: 2025-06-10 17:33 +0900
description: 최단경로 중 APSP 문제에 대한 플로이드 워셜 알고리즘에 대해 다룹니다.
image:
  path: assets/img/contents/Algorithm/floyd_warshall_example.png
  alt: Floyd-Warshall Algorithm
category: [Computer Science, Algorithm]
tags: [Floyd-Warshall, DP, Dynamic Programming, APSP]
pin: true
math: true
mermaid: true
toc: true
---  

## APSP(All Pairs Shortest-Paths) Problem  

### Problem Definition  
Directed graph G=(V, E)가 주어지고, 실수값의 가중치 함수 w가 주어졌을 때,  
Vertex 개수가 총 n개이고, 1부터 n까지 각 vertices가 mapping 된다고 가정하고, nxn 행렬 W로 임의의 vertex 

![apsp_example](assets/img/contents/Algorithm/apsp_example.png)  

$$W = \begin{pmatrix}
0 & 3 & 8 & \infty & -4 \\ 
\infty & 0 & \infty & 1 & 7 \\
\infty & 4 & 0 & \infty & \infty \\
2 & \infty & -5 & 0 & \infty \\
\infty & \infty & \infty & 6 & 0 \\
\end{pmatrix}$$  



### Naïve Approach 


## Floyd-Warshall's Algorithm  


```
FLOYD-WARSHALL(W)
	n = W.rows
	D⁽⁰⁾ = W
	for k=1 to n
		let D⁽ᵏ⁾ = (dᵢⱼ⁽ᵏ⁾) be a new n x n matrix
		for i=1 to n
			for j=1 to n
				dᵢⱼ⁽ᵏ⁾ = min(dᵢⱼ⁽ᵏ⁻¹⁾, dᵢₖ⁽ᵏ⁻¹⁾+dₖⱼ⁽ᵏ⁻¹⁾) // -> O(1)
	return D⁽ⁿ⁾
```  

