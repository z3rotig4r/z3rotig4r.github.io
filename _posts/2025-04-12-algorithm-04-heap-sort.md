---
layout: post
title: "[Algorithm] 04. Heap Sort"
date: 2025-04-12 16:10 +0900
description: 
image:
  path: assets/img/contents/Algorithm/heap_sort.png
  alt: Heap Sort
category: [Computer Science, Algorithm]
tags: [Heap Sort, Max-heapify, Priority Queue]
pin: true
math: true
mermaid: true
toc: true
---  s

## Heap Data Structure  
### Heap Sort 란?  
> heap이라는 특수한 자료 구조를 활용하여 정보를 관리하는 정렬 알고리즘  

다음과 같은 과정을 통해 heap sort가 진행된다.  
1. Max(Min)-heap을 생성  
2. 가장 큰(가장 작은) 원소를 heap에서 추출  
3. heap 특성을 유지하도록 조정  

### Heap  
Complete Binary Tree의 일종으로 아래의 Heap Property를 만족시켜야 한다.  

**Heap Property**  
1. Max-heap property: 부모노드의 key값이 자식노드의 key 값보다 크거나 같은 성질  
  $A[Parent(i)] \geq A[i]$
2. Min-heap property: 부모노드의 key값이 자식노드의 key 값보다 크거나 같은 성질  

Heap은 배열로 구현한다.  
![heap_array](/assets/img/contents/Algorithm/heap_structure.png)  
root 노드는 A[1]에 저장된다.  
부모 노드의 인덱스는 나누기 2한 인덱스, 왼쪽 자식은 인덱스의 2배, 오른쪽은 2배에 +1한 인덱스이다.  

높이가 h인 heap의 노드 개수   
마지막 레벨의 노드가 모두 차면 최대이고, 1개만 있으면 최소이다. 결과는 아래와 같다.  
![heap_array](/assets/img/contents/Algorithm/height_of_heap.png)  
노드 개수를 구했으니, 높이 h에 대한 추정을 할 수 있다.  
$$2^h \leq n \leq 2^{h+1} - 1$$  
$$2^h \leq n < 2^{h+1}$$ 이므로,  
$$h \leq \lg n < h+1$$  
따라서, $h=\lfloor \lg n \rfloor$  (가우스 함수와 동일한 의미, 소수부분을 버린다.)  

### Heap 생성 방법  
1. Max-Heapify  

  ```
  MAX-HEAPIFY(A, i)
    l = LEFT(i)
    r = RIGHT(i)
    if l <= A.heap-size and A[l] > A[i]
      largest
  ```
1. Build-Max-Heap


## Heap Sort  


## Priority Queue  


