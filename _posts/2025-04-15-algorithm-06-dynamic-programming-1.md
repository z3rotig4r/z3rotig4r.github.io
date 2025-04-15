---
layout: post
title: "[Algorithm] 06. Dynamic Programming (1)"
date: 2025-04-15 00:01 +0900
description: 
image:
  path: assets/img/contents/Algorithm/dynamic_programming.png
  alt: dynamic_programming
category: [Computer Science, Algorithm]
tags: [Dynamic Programming, Rod Cutting, Matrix-Chain Multiplication, Memoization, Tabulation]
pin: true
math: true
mermaid: true
toc: true
---

## Introduction to Dynamic Programming  
> Subproblem에 대한 Solution을 결합함으로써 복잡한 문제를 풀어나가는 것  
{: .prompt-info}  

### D&Q vs DP  
1. D&Q(Divide & Conquer)  
	**subproblem이 독립적임**  
	subproblem에 대한 solution이 공유되지 않음!!  
2. DP(Dynamic Programming)  
	**subproblem이 독립적이지 않음**  
	subproblem을 오로지 한번만 해결하고, solution을 저장해서 재사용함  
	-> 불필요한 연산 피함(avoid redundant computations)  

### Example of DP: Computing n-th Fibonacci Number  
$\mathrm{Fibo}[n] = \mathrm{Fibo}[n-1] + \mathrm{Fibo}[n-2]$  
e.g. 0, 1, 1, 2, 3, 5, 8, ...  

1. D&Q 구현  
	```python
	def fibo_recursion(n):
	if n <= 1:	# base case
		return n
	return fibo_recursion(n-1) + fibo_recursion(n-2)
	```  
	Time Complexity: $T(n) = T(n-1) + T(n-2) + 1$, 결국 $O(2^n)$  
	각 함수가 재귀적으로 다른 두 함수를 호출하는 형태  
	![dnq_fibo_structure](assets/img/contents/Algorithm/dnq_fibo_structure.png)  
	위 그림과 같이 중복되는 불필요한 subproblem들이 너무 많다.  
2. DP - Memoization  
	```python
	def fibo_memoization(n, cache):
		if n in cache:
			return cache[n]
		
		if n <=1:
			cache[n] = n
		else:
			cache[n] = fibo_memoization(n-1, cache) + fibo_memoization(n-2, cache)

		return cache[n]
	```  
	원래 problem을 재귀적으로 subproblem으로 쪼개면서 해결해 나가는 부분은 동일하다.  
	하지만, **cache라는 배열에 subproblem의 solution을 저장한다**.  
	만약 solution이 저장된 게 있으면, 즉, 동일한 subproblem을 맞닥뜨렸을 때 그 값을 재사용한다.  
	그래서, 각 subproblem은 `한번만` 수행된다.  
	Time Complexity: $O(n)$ => 엄청난 시간복잡도 감소를 만든다.  
	![dp_fibo_structure](assets/img/contents/Algorithm/dp_fibo_structure.png)
	위 그림처럼 중복되는 subproblem들은 cache에 저장된 값으로 처리한다.  

### Goal of Dynamic Programming  
DP는 최적화 문제에 적용한다.  
아래 예시를 간략하게 소개하며, 후술할 예정이다.  
예1) 막대기를 여러 개로 자르고 팔게 되면서 생기는 이익을 최대화하는 문제(막대기를 몇 개로, 얼마의 길이로 자르면 수익이 최대가 되는지)  
예2) 행렬의 곱연산에서 연산 비용을 최소화하는 문제(어느 행렬부터 연산해야 가장 적게 연산하는지)  

최적화 문제에 정답은 많지만, 그 중에서도 Maximum/Minimum인 최적의 값을 구하는 것이 목표이다.  
최적화 문제의 solution은 한 가지가 아니기에 `the optimal solution`이 아닌 `an optimal solution`이라 부른다. (예를 들어, 막대기 수익을 최대화하는 커팅 방법이 2~3개 있을 때, 우리는 어쨌든 그 중 하나만 구하면 되기 때문에)  

### Applying Dynamic Programming  
1. 최적해의 구조적 특성을 파악하기  
	= 전체 문제의 최적해가 부분 문제의 최적해로 어떻게 이뤄지는지 파악하기  
2. 최적해의 값을 재귀적으로 구하기  
	= 부분 문제를 기반으로 전체 문제의 최적해의 값을 재귀적으로 계산할 수 있는 관계식 세우기  
3. 각 부분 문제(subproblem)에 대한 최적해의 값을 계산하고 저장하기(중복 계산 피하기)  
	- Top-down (Memoization)  
	- Bottom-up (Tabulation)
4. 계산된 정보(=저장된 최적해의 값들)로부터 원래 문제에 대한 최적해를 구하기  
	- Top-down => 메모이제이션 된 값들을 따라가면서 최적해 재구성 (=traceback)  
	- Bottom-up => 테이블을 채워나가면서 마지막 cell에 최적해 도달  
	=> 각 subproblem은 오직 한번만!!!  

## Rod Cutting Problem  

### Problem Definition & Optimal Solution  
길이가 n인 막대와 $i = 1,2,3,\cdots,n$에 대한 가격 $p_i$의 표가 주어지면 해당 막대를 잘라서 판매했을떄 얻을 수 있는 최대수익 $r_n$을 결정하는 것  
(길이가 n인 막대의 가격 $p_n$이 충분히 비싸면 최적해는 자르지 않은 것일 수도 있음)  
![rod_cutting](assets/img/contents/Algorithm/rod_cutting_table.png)  

막대 길이가 n일 때, 자르는 경우의 수는 $2^{n-1}$가지가 존재하므로, naive한 방식으로 해결하려 한다면, 저 경우의 수를 전부 비교해 $O(2^n)$의 시간복잡도를 가진다. 너무 오래 걸린다.  

간단한 예시를 들어보자. 만약 4-inchj 막대기가 있다면, $2^3=8$가지의 경우의 수가 존재한다.  
4 | 1+3 | 2+2 | 3+1 | 1+1+2 | 1+2+1 | 1+2+1 | 1+1+1+1 |  
위 표를 통해서 최적해를 찾아보면, (2+2)일 때, 10달러로 최적해를 도출함을 알 수 있다.  

Optimal Solution을 조금 더 일반화해보면,  
만약 최적해가 k개의 조각으로 잘리는 상황이라고 했을 때($1 \leq k \leq n $),  
$n = i_1 + i_2 + \cdots + i_k$  
여기서 i는 k번째 막대기의 길이다.  
$r_n = p_{i_1} + p_{i_2} + \cdots + p_{i+k}$  
최적해를 구할 수 있다.  

조금 더 일반화해보면,  
$$r_n = max(p_n, r_1+r_{n-1}, r_2+r_{n-2}, \cdots, r_{n-1}+r_1)$$  
$p_n$은 no cut. 즉, 잘리지 않은 상태도 최대 수익이 가능하므로, 별개로 구하고, 나머지는 크기가 각각 $i$와 $n-i$인 두 개의 잘린 막대기의 최대 수익을 구하는 것과 동일하다.  
즉, subproblem을 2개의 막대기를 분할함으로써 만들어낸 것이다.  
쉽게 생각해보면, 7 = 1 + 1 + 2 + 3 이 될 수 있지만, 2 + 5가 될 수도 있다. 어? 이러면 수익이 달라지는 것 아닌가? 생각할 수 있지만 이미 우리는 막대기 길이가 5인 혹은 2인 막대기의 최대 수익을 알 수 있다고 가정한다. (subproblem으로 나눠서 그 때 계산하면 됨)  

즉, 전체 최적해는 2개의 subproblem에서의 최적해를 합쳐서 얻을 수 있고, rod-cutting problem은 `optimal substructure`를 가진다.  

뿐만 아니라, 막대기를 처음에 $i$ 길이로 자르고, 나머지 길이 $n-i$가 생기는데 이것도 같은 방식으로 자를 수 있다. 즉, 길이가 n인 막대기 자르는 문제를 i + (n-i)로 나누고 (n-i) 또한 새로운 subproblem으로 쪼개져 재귀적인 방식으로 최적해를 찾는다.  
즉, 전체 자르기(Decomposition)은 처음 자른 조각 + 남은 막대 자르기이고, 간결한 식으로 나타내면,  
$$r_n = \displaystyle \max_{1 \leq i \leq n} (p_i + r_{n-i})$$  
$p_i$는 first piece고 $r_{n-i}$는 remainder고 여기의 최적해에 집중하면 된다.  

### Applying dynamic programming  
1. Naïve Solution(DP X)  
	```
	CUT-ROD(p, n)
		if n==0
			return 0
		q = -∞
		for i=1 to n
			q = max(q, p[i]+CUT-ROD(p, n-i))
		return q
	```  
	![naive](/assets/img/contents/Algorithm/cut_rod_naive.png)  
	보다시피, 불필요한 연산이 중복되고,  
	T(0)=1, T(1)=2, T(2)=4, ...  
	$T(n)=2^n$ 길이 n에 대해 exponential한 형태로 시간복잡도를 가지게 된다.  

2. Dynamic Programming  
	각 subproblem이 한번만 풀어지게 arrange하고, 각각의 subproblem에 대한 해를 테이블에 저장하며, 나중에 그 해가 필요할 때 테이블을 보고서 필요한 값을 사용한다.  
	Time Complexity가 $O(2^n)$ -> $O(n)$이 되는 대신에, 그만큼 추가적인 메모리가 필요하다.  
	- Memoization  
	각 subproblem의 해를 저장하고, 이미 풀었던 subproblem에 대한 solution 값이 있으면 그 값을 불러와 사용한다.  
	```
	MEMOIZED-CUT-ROD(p, n)
		let r[0 .. n] be a new array	# For memo
		for i=0 to n
			r[i] = -∞
		return MEMOIZED-CUT-ROD-AUX(p, n, r)
	```  
	```
	MEMOIZED-CUT-ROD-AUX(p, n, r)
		if r[n] >= 0
			return r[n]
		if n == 0
			q = 0
		else q = -∞
			for i=1 to n
				q = max(q, p[i]+MEMOIZED-CUT-ROD-AUX(p, n-i, r))
		r[n] = q
		return q
	```
   - Tabulation  
	가장 작은 subproblem부터 시작해, 크기 순으로 해결해나간다.  
	특정 subproblem을 풀 때, 더 작은 subproblem에서 이미 구했던 해를 사용해 시간을 줄인다.  


## Matrix-Chain Multiplication Problem  


## Element of DP  

