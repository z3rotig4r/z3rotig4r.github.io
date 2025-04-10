---
layout: post
title: "[Algorithm] 03. Divide & Conquer(2)-QuickSort"
date: 2025-04-10 11:47 +0900
description: 분할/정복 알고리즘 중 퀵 소트에 대해서 다룹니다.
image:
  path: assets/img/contents/Algorithm/quick_sort.png
  alt: quick_sort
category: [Computer Science, Algorithm]
tags: [quick sort, DnQ]
pin: true
math: true
mermaid: true
toc: true
---

## Quick Sort  

### Description of Quick Sort  
> 1. 두 개의 subarray로 배열을 partitioning 한다. [Divide]  
> 2. Quicksort() 함수를 재귀적으로 호출하여 두 subarray를 정렬한다. [Conquer]  
> 3. subarray가 이미 정렬되었다면, combine할 게 없다. [X Combinde]  

일반적인 퀵 소트에서 PIVOT을 마지막 또는 첫 번째 element로 선택한다.  
cf. PIVOT(피벗)이란 기준이 되는 element로, 피벗 앞에는 피벗보다 작은 element들이, 피벗 뒤에는 피벗보다 큰 element들이 오도록 subarray를 나누는 기준이 된다. 피벗 자체는 subarray이 모두 채워지고 나서야 움직인다.  

p: start index  
r: end index  
i: last index of the left subarray  
j: current index  

만약, A = [2, 8, 7, 1, 3, 5, 6, 4] 와 같은 배열이 있고, 마지막 원소인 4를 PIVOT으로 설정한다고 가정해보자.  
p=0, j=0, r=7, i=-1 (i는 아직 left subarray가 생성이 안 되었기 때문에 -1로 두고, 모든 quick sort 코드에는 i=p-1로 설정한다.)  

1) 첫 번째 원소인 2와 PIVOT 4를 비교한다. PIVOT보다 더 작으므로 left subarray에 해당 원소를 넣어줘야 하는데, 이 과정이 특이하다. i를 1 증가시키고, A[i]와 A[j]를 swap 해줌으로써 PIVOT보다 작은 값들의 subarray를 형성하고 키워나간다. 첫 번째 원소이므로, 2가 그대로 원래 자리에 위치하게 되며, p=i=0이 된다.  
2) j를 1 증가시켜서 원소 8에 접근한다. PIVOT보다 크므로, 오른쪽 subarray에 포함되어야 한다. 하지만, 이때는 아무 원소도 움직이지 않는다. 그냥 current index인 j만 1 증가시킨다. 왜? i를 통해서 partition이 구분된다. 굳이 구분할 index 변수를 더 둘 필요도 없고, 다른 연산을 할 필요도 없다. 나중에 PIVOT 움직일 때도, 그냥 (i+1) 번째 원소랑 swap하면 된다.  
3) j를 1 증가시켜서 원소 7에 접근한다. 마찬가지로 PIVOT보다 크므로 right subarray에 포함시킬 것이고, 추가적 연산없이 두면 된다.  
4) j를 1 증가시켜서 원소 1에 접근한다. 1에서의 상황과 마찬가지로 PIVOT보다 작기 때문에 i를 1 증가시켜서 left subarray의 공간을 크기 1만큼 확장시키고, 그 자리에 존재하는 right subarray 소속의 원소와 swap한다. 당연히 right subarray 소속의 원소는 i가 1 증가해서 left subarray에 포함되었었지만 swap하면서 right subarray 오른쪽 끝으로 옮겨진다. 당연히 1증가된 i index 위치에는 1이 위치할 것이다.  
5) 이런 과정을 나머지 원소들에 전부 거쳐 진행해주면, A = [2, 1, 3, 8, 7, 5, 6, 4]인 원소 배열 상태가 되며, p=0, i=2, r=7 (j는 loop문과 함께 이미 배열 index 범위를 넘어갔다.)  
6) 마지막으로 PIVOT을 (i+1) 번째 원소인 8과 swap 함으로써 퀵 소트 정렬을 한다. 그 결과는 A = [2, 1, 3, 4, 7, 5, 6, 8]이다.  

```psuedocode
QUICKSORT(A, p, r)
  if p<r
    q = PARTITION(A, q, r) // 여기서 q는 i+1번째 index를 반환한다.  
    QUICKSORT(A, p, q-1)
    QUICKSORT(A, q+1, r)
```  

```psuedocode
PARTITION(A, p, r)
  x = A[r]
  i = p-1
  for j=p to r-1
    if A[j] <= x
      i = i + 1
      swap(A[j], A[i])
  swap(A[i+1], A[r])
  return i+1
```  


### Correctness of Quick Sort  
![correctness_of_qs](assets/img/contents/Algorithm/correctness_of_qs.png)  
잘 sorting 되는 걸 알 수 있다.  

### Complexity Analysis of Quick Sort  
> Quick Sort의 Time Complexity는 오로지 partitioning이 balance 한지 아닌지에 의존한다.  

그러면 Partitioning의 worst-case와 best-case는 어떻게 될까?  



### Improving Quick Sort: Tail-Recursive Quick Sort & Randomized Quick Sort  

