---
layout: post
title: "[FHE] Homomorphic Arithmetic Operations & CKKS's Encoding"
date: 2025-10-15 15:04 +0900
category: [Research, FHE]
tags: []
pin: true
math: true
mermaid: true
toc: true
---  

## FHE에서 실수를 다루는 방법  
FHE가 적용되고 있는 AI 분야에서는 특히나 실수 연산이 많은데,  
Floating-Point 방식이 아닌, Fixed-Point를 채택한다.(연산 Simplify)  

## 동형 산술 연산  
우선은, 실수 계수를 갖는 Polynomial Ring에서 정의되는 암호문을 다룬다고 생각한다.  
이때, coefficient encoding 스타일을 가정한다.  
이후

### Basic RLWE PKE Scheme와 Coefficient Encoding  
평문 벡터 $m \in \{0, 1\}^N$을 그대로 다항식의 계수로 간주한다.  
그리고 $m \cdot \lfloor q/2 \rceil$이 RLWE 샘플로 더해진다.  
복호화하는 동안 작은 에러가 생기지만 라운딩을 통해 높은 확률로 제거된다.  
하지만, 이 스킴은 다루는 데이터가 N비트의 값들로 제한된다는 단점이 있어, 이후 나오는 canonical embedding을 통한 Packed encoding을 적용한다.  

$$m \in \frac{\mathbb{Q}[X]}{X^N+1} \rightarrow \Delta \cdot m \in \frac{\mathbb{Q}[X]}{X^N+1} \rightarrow \lfloor \Delta \cdot m \rceil \in \frac{\mathbb{Z}[X]}{X^N+1} \rightarrow \lfloor \Delta \cdot m \rceil \in \frac{\mathbb{Z}_q[X]}{X^N+1}$$  

이때, $1 \ll \Delta \ll q$ 을 만족해야 한다.  

**Approximate Decoding**  
$(u, v) \cdot (1, s) = u + v \cdot s = r \cdot (b + a \cdot s) + e_0 + e_1 \cdot s + \lfloor \Delta \cdot m \rceil = r \cdot e + e_0 + e_1 \cdot s + \lfloor \Delta \cdot m \rceil = \lfloor \Delta \cdot m \rceil + e_{decrypt}$  
결국 복호화하면, $e_{decrypt}$가 나오는데, 디코딩에서 작은 error로 처리해 무시한다.  
해당 값 자체는 크다. 하지만 $\Delta$를 통해 scaling down을 함으로써 approximation error로 간주한다.  
$\frac{\lfloor \Delta \cdot m \rceil + e_{decrypt}}{\Delta} = \frac{\Delta \cdot m + e_{round} + e_{decrypt}}{\Delta} = m + \frac{e_{round} + e_{decrypt}}{\Delta}$  

Approximation error와 같이 복호화되기 떄문에, 이러한 인코딩 위에서 설계된 HE 스킴을 apprxoimate homomorphic encryption이라고 한다.  

### Homomorphic Addition  
$Enc(m_1) = (b_1, a_1) \cdot (1, s) = b_1 + a_1 \cdot s = \Delta \cdot m_1 + e_1 \quad (e_1 \leftarrow \chi) \\ Enc(m_2) = (b_2, a_2) \cdot (1, s) = b_2 + a_2 \cdot s = \Delta \cdot m_2 + e_2 \quad (e_2 \leftarrow \chi)$  



### Homomorphic Multiplication   

### Key-Switching  
$s_1$으로 decryption되는 $ct = (b, a)$를 $s_2$으로 decryption되는 $ct' = (b', a')$로 key 변환(secret key에 대한 정보를 보여주지 않고)  
$$Dec_{s_2}(ct') = Dec_{s_1}(ct) + e$$  
위와 같은 관계를 만족한다.  



### Rescaling  




## Data Encoding Problem & Canonical Embedding  

### 


### 



## 동형 rot, conj 연산  
