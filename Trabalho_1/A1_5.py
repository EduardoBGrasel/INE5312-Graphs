from A1_1 import Grafo
import sys

def floyd_warshall(g: Grafo):
    total_vertices = g.qtdVertices()  # Número de vértices
    # Inicializa matrix(0) com a matriz de pesos do grafo G
    matrix = g.MatrizAdj
    
    # Iteração do algoritmo
    for k in range(total_vertices):
        # Cria uma nova matriz matrix(k) com base na iteração anterior
        for u in range(total_vertices):
            for v in range(total_vertices):
                matrix[u][v] = min(matrix[u][v], matrix[u][k] + matrix[k][v])
    
    for i, row in enumerate(matrix):
        print(f"{i + 1}: {', '.join(map(str, map(int, row)))}")
    # Retorna a matriz final
    return matrix

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso correto: python3 A1_5.py <arquivo_de_entrada>")
        sys.exit(1)

    input_file = sys.argv[1]

    grafo = Grafo()

    try:
        grafo.read_lines(input_file)
        floyd_warshall(grafo)
                
        
    except FileNotFoundError:
        print("Arquivo não encontrado")
        sys.exit(1)
