import sys
from Grafo import Grafo, Vertice

# Função BFS para Hopcroft-Karp
def bfs(U, M, dist):
    # Cria uma pilha para executar a BFS
    queue = []
    for u in U:
        if u not in M:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')
    
    # Sentinela para emparelhamento final
    dist[None] = float('inf')  
    
    for u in queue:
        if dist[u] < dist[None]:
            for v in u.getVizinhos():
                match = M.get(v, None)
                if dist.get(match, float('inf')) == float('inf'):
                    dist[match] = dist[u] + 1
                    queue.append(match)
    
    return dist[None] != float('inf')

# Função DFS para Hopcroft-Karp
def dfs(u, M, dist):
    if u is not None:
        for v in u.getVizinhos(): 
            match = M.get(v, None)
            if dist[match] == dist[u] + 1 and dfs(match, M, dist):
                M[v] = u
                M[u] = v
                return True
        dist[u] = float('inf')
        return False
    return True

# Função Hopcroft-Karp para emparelhamento máximo
def hopcroft_karp(grafo: Grafo):
    # Separa os vértices do grafo em 2 grupos
    qtd_vertices = grafo.qtdVertices()
    vertices = grafo.Vertices  
    U = vertices[:qtd_vertices // 2]  
    V = vertices[qtd_vertices // 2:] 
    
    
    # Distancia e emparelhamento inicial definidos
    M = {}
    dist = {}

    # Executa a BFS para encontrar os vértices emparelhados
    while bfs(U, M, dist):
        for u in U:
            if u not in M:
                dfs(u, M, dist)

    return [(int(u.Numero), M[u]) for u in M if isinstance(u, Vertice)]

# Lendo arquivo
def carregar_grafo(input_file):
    grafo = Grafo(direcionado=True)
    grafo.read_lines(input_file)
    return grafo

# Execução do emparelhamento
def executar_emparelhamento(input_file):
    try:
        grafo = carregar_grafo(input_file)
        emparelhamento = hopcroft_karp(grafo)
        
        print(len(emparelhamento))
        for u, v in emparelhamento:
            if (u, v) != emparelhamento[-1]:
                print(f"{u}-{v}", end=', ')
            else:
                print(f"{u}-{v}")

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)

# Execução do programa
def main():
    if len(sys.argv) != 2:
        print("Uso correto: python3 A2_1.py <arquivo_de_entrada>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    executar_emparelhamento(input_file)

if __name__ == "__main__":
    main()