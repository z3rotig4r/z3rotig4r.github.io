---
layout: post
title: "[DataStructure] 02. Array"
date: 2025-04-11 00:06 +0900
description: 대표적인 자료구조인 Array(배열)에 대해서 설명합니다.
image:
  path: assets/img/contents/Data_Structure/array.png
  alt: array
category: [Computer Science, Data Structure]
tags: [Array]
pin: false
math: true
mermaid: true
toc: true
---

## Array(배열) 이란?  
> 고정된 homogeneous collection of elements => 원소들이 단일 속성을 가지는(e.g. int면 int만, char면 char만)  
> stored in a contiguous memory location => 메모리 상에서 반드시 인접한 연속된 주소에 위치한다.  
> 각 원소들은 인덱스나 키로 식별된다. 
{: .prompt-info }

### 배열과 관련된 연산


```c
int main(){
	int arr[5];		// 배열 선언 -> 20bytes 할당 + garbage value로 초기화
	int arr1[5] = {2, 4, 8, 12, 16};	// 배열 선언 및 각 원소 초기화
	int arr2[] = {1, 2, 3, 4, 5}; 		// size 지정하지 않고 초기화 가능
	int arr3[5];
	for (int i=0; i<5; i++){
		arr3[i] = arr2[i] * 2;
	}									// loop를 통한 초기화

	printf("%d", arr[2])				// 배열 내 원소 접근

	arr2[2] = 100;						// 원소 업데이트

	for (int i=0; i<5; i++){
		printf("%d ", arr[i])			// traversal
	}	
}
```

### 