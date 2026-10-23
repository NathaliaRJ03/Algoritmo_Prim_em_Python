import heapq

def ler_inteiro(mensagem, minimo, maximo=None):
    while True:
        try:
            valor = int (input(mensagem))
            if valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Digite um valor menor ou igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Erro! Digite um numero inteiro valido.")

def ler_peso():
    while True:
        try:
            peso = float(input("Peso da aresta: "))
            if not (0 <= peso < float("inf")):
                print("O peso deve ser finito e não negativo.")
                continue
            return peso
        except ValueError:
            print("Erro! Digite um peso numerico valido.")

def prim(grafo, inicio=0):
    visitados = set()
    fila = [(0, inicio, -1)]
    arvore = []
    custo_total = 0
    while fila:
        peso, atual, origem = heapq.heappop(fila)
        if atual in visitados:
            continue
        visitados.add(Atual)
        if origem != -1:
            arvore.append((origem, atual, peso))
            custo_total += peso
        for vizinho, peso_aresta in grafo[atual]:
            if vizinho not in visitados:
                heapq.heappush(
                    fila,
                    (peso_aresta, vizinho, atual)
                )

    if len(visitados) != len(grafo):
        return None, None
    return arvore, custo_total

print ("=== ALGORITMO DE PRIM ===")
print ("Grafo não orientado")
n = ler_inteiro("Quantidade de vertices: ", 1)
max_arestas = n* (n-1) // 2
m = ler_inteiro(
        f"Quantidade de arestas (0 a {max_arestas}): ",
        0,
        max_arestas
    )

grafo = [[] for _ in range (n)]
aresta_cadastradas = set()


for i in range(m):
    print(f"\n Aresta {i + 1}")
    while True:
        u = ler_inteiro(
            f"Vertice de origem (0 a {n - 1}):",
            0, n - 1

        )

        v = ler_inteiro(
            f"Vertice de destino (0 a  {n -1 }):",
            0, n - 1
        )

        if u == v:
            print ("Erro! Nao sao permitido laços.")
            continue

        aresta = tuple(sorted((u, v)))
        if aresta in aresta_cadastradas:
            print ("Erro! Esta aresta ja foi cadastrada. ")
            continue
        break

    peso = ler_peso()
    aresta_cadastradas.add(aresta)

    grafo[u].append((v, peso))
    grafo[v].append((u, peso))

print("\n === GRAFO CADASTRADO ===")
for vertice in range (n):
    print(f"Vertice {vertice}: {grafo[vertice]}")

arvore, custo = prim(grafo)
print ("\n === ARVORE GERADORA MINIMA === ")
if arvore is None:
    print("O grafo noa é conexo.")
    print ("Nao existe árvore geradora minima. ")

else:
    for u, v, peso in arvore:
        print(f"{u} -- {v} | Peso: {peso:g}")
    print(f"\n Peso total da AGM: {custo:g}")
    print (f"Quantidade de arestas da AGM: {len(arvore)}")