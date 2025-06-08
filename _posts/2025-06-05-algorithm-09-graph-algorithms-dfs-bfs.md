---
layout: post
title: "[Algorithm] 09. Graph Algorithms(DFS, BFS)"
date: 2025-06-05 13:11 +0900
description: 그래프와 그래프 탐색 알고리즘인, DFS와 BFS 알고리즘에 대해 다룹니다.
image:
  path: /assets/img/contents/Algorithm/graph_intro.png
  alt: graph_intro
category: [Computer Science, Algorithm]
tags: [DFS, BFS, Graph Theory]
pin: true
math: true
mermaid: true
toc: true
---

## Introduction to Graphs  

### Definition & Applications  
> 그래프란 entity와 그 entity 간의 relation를 표현하는 일반적인 언어이다.  
{: .prompt-info }  
적용 예시: Social Network Analysis, Digital Healthcare, RecSys, Social Welfare, RAG 등  

### Terminologies  
G(V, E)로 정의하며, V는 Vertex (정점, 노드)이고, E는 Edge (간선)이다.  
즉, V는 Entity 집합, E는 Relation의 집합을 의미한다.  

**Directed Graph vs. Undirected Graph**  
- Directed Graph: Edge에 방향성이 존재한다. 만약, 어떤 edge를 (u, v)로 나타내면, u는 v에 `adjacent`하다고 표현할 수 있다. (단, v가 u에 adjacent하다고 표현하진 못한다. 이는 `Asymmetric`한 특징을 나타낸다.)  
- Undirected Graph: Edge에 방향성이 없다. 만약, 어떤 edge를 (u, v)로 나타내면, u는 v에 `adjacent`하다고 표현할 수 있다. 반대로 v도 u에 `adjacent`하다고 표현할 수 있다. (`Symmetric`한 특징이 드러난다.)  

**Degree of a Node(노드 또는 정점의 차수)**  
쉽게 설명하면, 꼭지점(정점, 노드)에 입사하는 모서리(간선)의 개수이다.  
이는 Directed인지, Undirected 인지에 따라 다르게 계산될 수 있다.  
1. Directed Graph  
  - In-degree of a node: 해당 노드에서 incoming edges의 개수이다.  
  - Out-degree of a node: 해당 노드에서 outcoming edges의 개수이다.(바깥 방향을 향하는 간선의 개수)  
2. Undirected Graph  
  해당 노드(정점)에 연결된 간선의 개수이다.  

**Path(경로)**  
vertex u에서 vertex v로 가는 path(경로)는 $<v_0, v_1, \dots, v_k>$로 나타낸다. 이때, $v_0$는 u, $v_k$는 v로 볼 수 있다.  
vertices에 대한 sequence의 길이(length)는 path(경로)에서 지나가는 edge의 개수로 나타낸다.  
만약 vertex u에서 v까지 path가 있다면, `reachable`하다고 표현한다.  
`simple path`란, path상의 모든 정점이 `distinct`한 path로, cycle 없이(=중복되는 vertex)없이 path가 만들어진 경우를 말한다.  
해당 그래프를 통해 생성되는 모든 path가 simple한 경우, 즉 cycle이 존재하지 않는 graph를 `Acyclic Graph`라고 표현한다.  

### Representation  
Graph를 표현하는 방법엔 두 가지가 있다.  
1. Matrix  
2. List  

딱 봐도, 뭐가 더 효율적일지 보인다.  
결국 List를 활용해서 DFS나 BFS를 설명하겠지만, Matrix로 표현하는 방법도 있다는 것을 알아두고, 왜 Matrix가 더 비효율적인지 살펴볼 필요도 있다.  

**Adjacency-Matrix Representation**  
$|V| \times |V|$인 matrix A가 있을 때,  
vertex i에서 vertex j로 연결된 edge가 존재하면 A[i][j]의 값은 1로 표시하는 방법이다.  
특이한 점은, Undirected Graph의 경우 A의 대각선(diagonal)에 대하여 symmetric하다.  

![matrix_representation_example](assets/img/contents/Algorithm/matrix_rep_sample.png)  

**공간복잡도**  
$O(|V|^2)$  
Vertex 개수의 제곱만큼의 공간을 가진다.  
Matrix이고 존재하지 않는 edge에는 0으로 채우기 때문이다.  

**시간복잡도**  
기본적으로 $O(|V|^2)$를 가진다.  
연산 종류에 따라 다르지만, Edge가 존재하는지를 따지려면, $O(1)$이 필요.  
해당 Vertex의 Neighbor edge 판단하려면, $O(V)$이 필요.  
모든 edge를 탐색하려면, $O(|V|^2)$가 필요하다.  

**Adjacency-List Representation**  

$|V|$개의 List를 가지고, 각각의 리스트는 하나의 vertex에 대응한다.  
vertex u에 대해서, u의 adjacency list에는 adjacent vertices를 포함한다.  

![list_representation_example](assets/img/contents/Algorithm/list_rep_sample.png)  

**공간복잡도**  
$O(|V|+|E|)$  
존재하는 edge만 보관함  

**시간복잡도**  
$O(|E|)$  
Edge가 존재하는지 A[i][j]를 확인, O(vertex i의 차수)  
이웃 리스트 -> O(vertex의 차수)  
모든 엣지를 탐색 $O(|E|)$  


**모든 트리는 그래프지만, 모든 그래프는 트리는 아니다.**  
그래프는 만약 cycle 없고, 모든 vertice가 연결되어있다면 트리가 될 수 있다.  

## Searching on Graphs  

왜 우리는 Graph Searching 알고리즘이 필요할까?  
그래프에서 특정 vertex를 찾고, 특정 vertex까지 reachable 한지를 파악하고, shortest path를 찾는 다양한 문제를 풀기 위함이다.  

### BFS(Breath-First Search)  
> $G=(V, E)$를 가지는 그래프와 source vertex(시작 정점) s가 주어지면,  
> s로부터 모든 reachable(도달가능)한 vertex를 `discover`한다.  
{: .prompt-warning}  

`Discover`의 의미는 source vertex에서 `distance(거리)`를 점점 증가시키면서 탐색하는 것을 의미한다. Breath-First라는 이름에서 알 수 있듯이 가까운 vertex 먼저 탐색하는 알고리즘이다.  
(cf. 이때, distance의 의미는 임의의 정점 u에서 v까지의 최단 경로를 말한다.)  

BFS의 특징은 항상 해당 vertex에서 시작 정점으로부터의 거리 $d$와 해당 vertex가 이전에 지나온 vertex (즉, predecessor)인 $\pi$를 항상 연산해야 한다.  

![graph_bfs](assets/img/contents/Algorithm/graph_bfs.png)  

```
BFS(G, s)
  // source vertex를 제외한 vertex에 초기화
  for each vertex u ∈ G.V-{s}
    u.color = WHITE
    u.d = ∞
    u.π = NIL
  // WHITE는 아직 discover하지 않은 것 (= enqueue 대상)
  // GRAY는 Discover했지만, 끝나지 않은 것 (= 아직 Q에 있는 상태)
  // BLACK은 완전히 Finished된 것 (= dequeue 된 것)
  s.color = GRAY
  s.d = 0
  s.π = NIL
  Q = ∅   //Queue 자료구조 활용
  ENQUEUE(Q, s)
  while Q != ∅              //Explorer a Graph
    u = DEQUEUE(Q)
    for each v ∈ G.Adj[u]   //Adj linked-list 참고. u에 대해서!
      if v.color == WHITE
        v.color = GRAY
        v.d = u.d + 1
        v.π = u
        ENQUEUE(Q, v)
    u.color = BLACK
```  

**BFS의 시간복잡도**  
Initialization: $O(|V|)$  
Exploring a graph: $O(|V| + |E|)$  
모든 vertex는 최대 1번 enqueue됨  
모든 Adjacency list는 최대 1번 scan됨  

**BFS Tree**  
![bfs_tree](assets/img/contents/Algorithm/bfs_tree.png)  
G에 대한 Predecessor Subgraph인 $G_{\pi} = (V_{\pi}, E_{\pi})$  
$V_{\pi} = {v \in V: v.\pi \neq NIL} \cup \\{s\\}$  
$E_{\pi} = {(v.\pi, v): v \in V_{\pi} = \\{s\\}}$  

위 그림 및 집합으로 정의될 수 있다.  
또한, tree의 Edge 개수인 $|E_{\pi}|$는 $|V_{\pi} - 1|$인 특징을 보인다. (당연히 트리니까..)  

만약, Adajacency list가 아닌 Matrix 방식으로 표현한다면,  
시간복잡도는 Initialization에서 $O(|V|^2)$로 바뀌고,  
Exploring a graph에서 $O(|V|+|V|^2)$로 바뀐다.  
필요없는 `0`까지 martix에서 scanning 해야 하는 시간낭비가 일어난다.  
특히, 수도코드 상에서 `for each v in G.Adj[u]`부분이  
```
for v = 1 to |G.V|       // 모든 정점 v에 대해
  if G[u][v] == 1        // u와 v가 연결되어 있으면 (간선이 존재하면)
```  
위처럼 바뀐다.  

### DFS  
> $G=(V, E)$를 가지는 그래프가 주어지면,  
> 언제든 가능한만큼 그래프에서 `deeper`하게 탐색하는 알고리즘이다.  
{: .prompt-warning}  
`deeper`의 의미에서 알 수 있듯이, 정점을 하나 선택해 가능한 가장 깊은 정점까지 탐색한 후 인접한 정점으로 이동해 다시 깊게 탐색하는 알고리즘으로, BFS보다 조금 생소하고 어렵게 느껴지는 알고리즘이다.  

각 vertex는 다음 두 개의 timestamps를 가진다.  
`v.d`: discovery time  
`v.f`: finish time  

![dfs_example](assets/img/contents/Algorithm/dfs_example.png)

<DFS 메인 함수>  
```
DFS(G)
  // 모든 vertex 초기화
  for each vertex u ∈ G.V
    u.color = WHITE
    u.π = NIL
  time = 0
  // 모든 vertex (WHITE인) 대상으로 DFS-VISIT 수행
  for each vertex u ∈ G.V
    if u.color == WHITE
      DFS-VISIT(G, u)
```  

<DFS 탐색 함수 - DFS-VISIT>  
```
DFS-VISIT(G, u)
  // Discovered  
  time = time + 1
  u.d = time
  u.color = GRAY
  // 재귀적으로 deeper한 이웃 정점을 방문
  for each v ∈ G.Adj[u]
    if v.color == WHITE
      v.π = u
      DFS-VISIT(G, v)
  // 재귀 호출 전부 완료되면 하나씩 Finish time 정의
  u.color = BLACK
  time = time + 1
  u.f = time
```  

**DFS의 시간복잡도**  
Initialization: $\Theta(|V|)$  
Exploring a graph: $\Theta(|V|+|E|)$  
Aggregate Analysis에 의해서 $O(|V|*|E|)$가 아님을 알 수 있음.  

**DFS의 특징**  
1. Depth-First Forest  
  predecessor의 subgraph는 여러 개의 Tree들로 구성된 forest를 만든다.  
2. Descendant  
  v가 u의 descendant인 것은 v가 u가 GREY인 시간 동안 discover 됨을 의미한다.  
3. Parenthesis Structure  
  어떠한 DFS에서도, 모든 두 개의 vertex에 대해서, 아래 세 가지 조건 중 하나는 성립한다.  
  1) 임의의 두 vertex u, v에 대해서 [u.d, u.f]와 [v.d, v.f]의 시간 간격이 완전히 분리된 구간에 있으면, depth-first forest에서 서로 다른 트리에 속해 있음을 의미한다. (u, v가 둘 중 어느 것도 다른 것의 descendant가 될 수 없음)  
  2) [u.d, u.f]에서의 시간 간격이 [v.d, v.f]의 시간 간격 안에 포함된다면, u는 v의 descendant이다.  
  3) [v.d, v.f]에서의 시간 간격이 [u.d, u.f]의 시간 간격 안에 포함된다면, v는 u의 descendant이다.  
  ![parenthesis_structure_dfs](assets/img/contents/Algorithm/parenthesis_structure_dfs.png)  

**Edge의 분류**  
1. Tree Edge
  depth-first forest에 속하는 edge  
  즉, DFS 수행 중에 실제로 방문을 유도한 edge  
  새 정점을 발견할 때 사용된 edge  
2. Back Edge
  Nontree edge이면서, 한 정점에서 자신의 ancestor로 가는 edge  
  Cycle 탐지 시 이용  

3. Forward Edge
  Nontree edge이면서, 한 정점에서 이미 방문한 descendant로 가는 edge  
4. Cross Edge
  서로 조상-자손 관계가 없는 정점 사이를 잇는 간선  


## Applications  

### Connected components  


### Topological sort  
Acyclic 증명 = > DFS 이용 => DFS에서 Back Edge 있으면 Acyclic 아님 (=cycle 있음)