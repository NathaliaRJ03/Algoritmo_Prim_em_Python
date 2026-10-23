🌳 Algoritmo de Prim em Python

Este projeto implementa o Algoritmo de Prim em Python para encontrar a Árvore Geradora Mínima (AGM) de um grafo não orientado e ponderado.

O programa permite cadastrar vértices e arestas, definir os pesos das conexões e calcular a árvore geradora mínima, apresentando as arestas selecionadas e o custo total. Caso o grafo não seja conexo, o programa informa que não existe uma árvore geradora mínima para todos os vértices.

🎯 Objetivo

Aplicar conceitos de teoria dos grafos e algoritmos de otimização, utilizando o Algoritmo de Prim para encontrar uma árvore que conecte todos os vértices de um grafo com o menor custo total possível.

⚙️ Funcionalidades
Cadastro da quantidade de vértices e arestas.
Construção de um grafo não orientado e ponderado.
Definição de pesos não negativos e finitos para as arestas.
Validação de entradas numéricas.
Impedimento de laços e arestas duplicadas.
Utilização de uma fila de prioridade com o módulo heapq.
Cálculo da Árvore Geradora Mínima (AGM).
Exibição das arestas selecionadas e do peso total da árvore.
Verificação de conectividade do grafo.
🧠 Como funciona o Algoritmo de Prim?

O Algoritmo de Prim encontra uma Árvore Geradora Mínima expandindo gradualmente uma árvore a partir de um vértice inicial.

O funcionamento segue estas etapas:

Escolhe um vértice inicial.
Adiciona à fila de prioridade as arestas que conectam os vértices visitados aos não visitados.
Seleciona a aresta de menor peso que leva a um vértice ainda não visitado.
Adiciona esse vértice à árvore e atualiza as possibilidades de conexão.
Repete o processo até visitar todos os vértices ou esgotar as arestas disponíveis.

Se todos os vértices forem visitados, o programa apresenta a árvore geradora mínima. Caso contrário, informa que o grafo não é conexo.


💻 Exemplo de utilização

Considere um grafo com 4 vértices e as seguintes arestas:

Origem	Destino	Peso
0	1	1
0	2	4
1	2	2
1	3	5
2	3	3

Uma possível saída do programa será:

=== ARVORE GERADORA MINIMA ===
0 -- 1 | Peso: 1
1 -- 2 | Peso: 2
2 -- 3 | Peso: 3

Peso total da AGM: 6
Quantidade de arestas da AGM: 3


A árvore geradora mínima conecta os quatro vértices utilizando três arestas, com custo total igual a 6.

⏱️ Complexidade

Utilizando uma fila de prioridade baseada em heap, a implementação apresenta complexidade de tempo de até O((V + E) log E), considerando uma implementação com inserção de arestas candidatas na fila, em que:

V representa a quantidade de vértices.
E representa a quantidade de arestas.

A complexidade espacial é O(V + E) para armazenar o grafo e as estruturas auxiliares, considerando também a fila de prioridade.

📌 Conceitos aplicados
Grafos não orientados e ponderados.
Árvore Geradora Mínima (AGM).
Algoritmo de Prim.
Filas de prioridade e heaps.
Validação de dados e tratamento de exceções.
Análise de complexidade de algoritmos.
