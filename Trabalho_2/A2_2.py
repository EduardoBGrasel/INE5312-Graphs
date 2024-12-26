import sys
from Grafo import Grafo
import math

def dfs_visit_ot(v, grafo, C, T, F, O, tempo):
    C[v] = True
    tempo[0] += 1
    T[v] = tempo[0]

    for u in grafo.Vertices[v-1].getVizinhos():
        if not C[u]:
            dfs_visit_ot(u, grafo, C, T, F, O, tempo)

    tempo[0] += 1
    F[v] = tempo[0]
    O.insert(0, v)  # Adiciona o vértice no início da lista O para manter a ordenação topológica

def dfs_ordenacao_topologica(grafo):
    # Inicializando variáveis de controle
    C = {v: False for v in range(1, grafo.qtdVertices() + 1)}  # Visitado
    T = {v: float('inf') for v in range(1, grafo.qtdVertices() + 1)}  # Tempo de início
    F = {v: float('inf') for v in range(1, grafo.qtdVertices() + 1)}  # Tempo de finalização
    O = []  # Lista para a ordenação topológica
    tempo = [0]  # Usando uma lista para que `tempo` seja mutável e compartilhado entre chamadas

    # Percorrendo todos os vértices do grafo
    for v in range(1, grafo.qtdVertices() + 1):
        if not C[v]:
            dfs_visit_ot(v, grafo, C, T, F, O, tempo)

    return O  # Retorna a lista com os vértices ordenados topologicamente

def exibir_ordenacao_topologica(grafo):
    # Realiza a ordenação topológica e obtém a lista de vértices ordenados
    ordem_vertices = dfs_ordenacao_topologica(grafo)

    # Constrói uma lista com os rótulos dos vértices na ordem topológica
    ordem_rotulos = [grafo.getRotulo(v) for v in ordem_vertices]

    # Exibe a ordem topológica em formato de sequência
    print(" → ".join(ordem_rotulos))

def main():
    if len(sys.argv) != 2:
        print("Uso correto: python3 A2_1.py <arquivo_de_entrada>")
        sys.exit(1)

    input_file = sys.argv[1]
    grafo = Grafo(direcionado=True)

    try:
        grafo.read_lines(input_file)
        exibir_ordenacao_topologica(grafo)

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)

main()
