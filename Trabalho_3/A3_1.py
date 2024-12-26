from collections import deque
import sys
from Grafo import Grafo

def edmonds_karp(grafo, s, t):
    """Implementação do algoritmo de Edmonds-Karp com validações para evitar valores infinitos."""
    n = grafo.qtdVertices()
    capacidade = grafo.MatrizAdj  # Matriz de capacidades
    fluxo = [[0] * n for _ in range(n)]  # Matriz de fluxo inicial
    
    # Verificação: substituir valores "inf" na matriz de capacidades por 0
    for i in range(n):
        for j in range(n):
            if capacidade[i][j] == float('inf') or capacidade[i][j] < 0:  # Capacidade inválida
                capacidade[i][j] = 0

    # Caso especial: origem e destino iguais
    if s == t:
        return 0

    def bfs():
        """Busca em largura para encontrar um caminho aumentante."""
        pai = [-1] * n  # Vetor para armazenar o caminho
        pai[s - 1] = s - 1  # Fonte é sua própria origem
        fila = deque([s - 1])  # Fila para o BFS
        while fila:
            u = fila.popleft()
            for v in range(n):
                # Capacidade residual > 0 e vértice ainda não visitado
                if pai[v] == -1 and capacidade[u][v] - fluxo[u][v] > 0:
                    pai[v] = u
                    if v == t - 1:  # Chegamos no destino
                        return pai
                    fila.append(v)
        return None

    max_fluxo = 0
    iteracao = 0  # Contador de iterações

    while True:
        # Encontra um caminho aumentante
        caminho = bfs()
        if not caminho:  # Se não houver caminho aumentante, pare
            break

        # Determinar a capacidade residual mínima no caminho aumentante
        v = t - 1
        capacidade_residual = float('inf')
        while v != s - 1:
            u = caminho[v]
            capacidade_residual = min(capacidade_residual, capacidade[u][v] - fluxo[u][v])
            v = u

        # Atualizar o fluxo no grafo residual
        v = t - 1
        while v != s - 1:
            u = caminho[v]
            fluxo[u][v] += capacidade_residual
            fluxo[v][u] -= capacidade_residual
            v = u

        max_fluxo += capacidade_residual

        # Mostrar o grafo residual a cada iteração
        iteracao += 1

    return max_fluxo

def main():
    if len(sys.argv) != 4:
        print("Uso correto: python3 A2_1.py <arquivo_de_entrada>")
        sys.exit(1)

    input_file = sys.argv[1]
    s = int(sys.argv[2])
    t = int(sys.argv[3])
    grafo = Grafo(direcionado=True)

    try:
        grafo.read_lines(input_file)
        print(edmonds_karp(grafo, s, t))

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()