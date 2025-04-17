---
layout: post
title: "[Algorithm] 05. Non-comparison-based sorting"
date: 2025-04-12 16:11 +0900
description: 
image:
  path: assets/img/contents/Algorithm/non_comparison_based_sort.png
  alt: Non-Comparison-based Sort
category: [Computer Science, Algorithm]
tags: [Counting Sort, Radix Sort, Non-comparison-base sorting, Stability]
pin: false
math: true
mermaid: true
toc: true
---

## Comparison-based Sorting  
오로지 원소들 간의 비교를 기반으로 정렬하는 알고리즘이다.  
하지만, 아무리 optimal한 sorting 알고리즘이여도, worst case에서 $\Omega(n \lg n)$이다.  
즉, 머지소트나 힙소트가 점근적으로 최적화된 comparison sort 방식이라는 것이다.  

그렇다면, 비교를 사용하지 않고, 선형 시간($O(n)$)에 정렬을 수행할 수 있는 알고리즘이 있을지 생각해볼 수 있다.  

## Counting Sort  
> 각 원소의 빈도를 카운팅하여 input array를 정렬하는 non-comparison 알고리즘이다.  

A: input array, B: output array, C: temporary array 로 가정한다.  
 
1. 배열 C를 모두 0으로 초기화한다.  
2. 각 원소들의 빈도를 계산한다.  
3. 얼마나 많은 원소들이 특정 원소에 대해 작거나 같은지를 결정한다.  
4. 적절한 위치에 각 원소들을 놓는다.  

```
COUNTING-SORT(A, B, k)
  let C[0 .. k] be a new array
  for i=0 to k
    C[i] = 0
  for j=1 to A.length
    C[A[j]] = C[A[j]] + 1
  // 위 코드를 수행하게 되면, C[i]에는 i와 동일한 원소에 대한 개수가 저장된다.   
  // 말이 모호한데, 만약 A에 4가 2개 있으면, C[4]=2라는 것이다.  
  for i=1 to k
    C[i] = C[i] + C[i-1]
  // C[i]에는 i와 동일하거나 작은 원소의 개수가 저장된다.  
  for j=A.length downto 1
    B[C[A[j]]] = A[j]
    C[A[j]] = C[A[j]] - 1
```  

어떻게 굴러가는지는 단순한 반복이 많아서 생략한다.  
위 코드대로 따라만 가보면 된다.  

그래서 시간복잡도는 $\Theta(n+k)$이다.  
여기서 k는 temporary 배열의 크기로, input array A 원소의 최대값이 된다.  
즉, k 값에 따라 성능이 달라지는데, $O(n)$에 마찬가지로 근사하므로, 최종적으로 $\Theta(n)$을 따른다.  
선형시간을 가지는 정렬 알고리즘이다.  
문제는, k 값이 너무 커지게 된다면, 불필요한 메모리 공간을 사용하게 된다.  
예를 들면, A에 1000000이 저장되어 있어서, k가 1000000이면 temporary 배열 C의 공간도 1000000로 설정되며, 비효율적인 메모리 사용이 지속된다.  
따라서, k 값이 작은 경우에 한하여 굉장히 효율적인 선형 시간 정렬 알고리즘이라고 말할 수 있다.  

**Stability(안정성)**  
정렬 알고리즘이 `stable`하다는 말은, 입력 데이터셋에서 드러낸 그대로, 정렬된 output 데이터셋에서도 동일한 순서로 두 원소가 드러나는 것.  
쉽게 말해서, 40 20 30 30 20 40 50 이라는 배열이 정렬되었을 때, 앞에 나온 40과 뒤에 나온 40이 정렬되고서도 앞에 나온 40이 뒤에 나온 40보다 앞에 배치하게 되는 결과가 나온다면, stable 하다고 할 수 있다.  
위처럼 key가 한 개로 구성된 자료구조에서는 큰 의미가 없지만, multiple key 또는 key-value 쌍으로 이뤄진 데이터에 대한 정렬을 수행할 때 relative order(순서)를 유지하는 것이 굉장히 중요할 때가 많다.  

당연히 counting sort는 stability를 만족한다.  
input array의 맨 뒤 원소부터 정렬에 참여하고, output array에서도 뒷부분에 먼저 원소가 추가되서, stability는 만족하는 정렬 알고리즘이라고 말할 수 있다.  

## Radix Sort  
> 쉽게 말하면 digit by digit으로 정렬하는 알고리즘이다.  

예를 들면, 312 456 이렇게 주어졌을 때, 일의 자리 먼저 정렬하고, 그 다음 십의 자리, 그 다음 백의 자리 순으로 정렬을 하는 것이다.  
이 때 stability 는 유지되어야 한다.  

```
RADIX-SORT(A, d)
  for i=1 to d
    use a stable sort to sort array A on digit i
```  

반드시 stable sort algorithm을 사용하도록 하며, least significant digit부터 시작해 most significant digit까지 차례로 정렬한다.  

최종적으로 시간복잡도는 $\Theta(d(n+k))$를 따른다.  
d는 digit의 개수, n은 input array의 크기, k는 input integer의 범위이다.  
d는 상수이고, k는 $O(n)$을 따르니, 결국 $\Theta(n)$을 따른다.  
