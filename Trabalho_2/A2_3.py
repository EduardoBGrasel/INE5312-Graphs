from Grafo import Grafo
import sys

def kruskal(grafo):
    A = []  # Conjunto de arestas da MST
    S = {v: {v} for v in range(1, grafo.qtdVertices() + 1)}  # Conjuntos disjuntos
    soma_pesos = 0  # Soma dos pesos das arestas na MST

    # Ordena as arestas por peso
    arestas_ordenadas = []
    for u in range(1, grafo.qtdVertices() + 1):
        for v in grafo.Vertices[u-1].getVizinhos():
            if u < v:  # Evitando duplicidade
                peso = grafo.peso(u, v)
                arestas_ordenadas.append((peso, u, v))
    arestas_ordenadas.sort()  # Ordena as arestas pelo peso

    # Processa as arestas ordenadas
    for peso, u, v in arestas_ordenadas:
        if S[u] != S[v]:  # Se u e v estão em componentes diferentes
            A.append((u, v))  # Adiciona a aresta ao conjunto A
            soma_pesos += peso  # Adiciona o peso da aresta à soma total
            x = S[u].union(S[v])  # União dos conjuntos Su e Sv
            for vertice in x:
                S[vertice] = x  # Atualiza todos os vértices para o conjunto unificado

    return A, soma_pesos  # Retorna o conjunto de arestas e o somatório dos pesos

def exibir_mst(grafo):
    mst, soma_pesos = kruskal(grafo)
    
    # Exibe o somatório dos pesos das arestas
    print(f"{soma_pesos:.1f}")

    # Formata e exibe as arestas da MST na ordem desejada
    arestas_formatadas = [f"{u}-{v}" for u, v in mst]
    print(", ".join(arestas_formatadas))

def main():
    if len(sys.argv) != 2:
        print("Uso correto: python3 programa.py <arquivo_de_entrada>")
        sys.exit(1)

    input_file = sys.argv[1]
    grafo = Grafo(direcionado=False)

    try:
        grafo.read_lines(input_file)
        exibir_mst(grafo)

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)

main()
