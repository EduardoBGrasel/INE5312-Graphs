from A1_1 import Grafo, Vertice
import math
import sys

def Dijkstra(grafo: Grafo, root: int):
    distance = [math.inf] * grafo.qtdVertices()  # Distâncias iniciais são infinitas
    predecessor = [None] * grafo.qtdVertices()  # Predecessores iniciam como None
    visited = [False] * grafo.qtdVertices()  # Nenhum vértice foi visitado ainda


    distance[root] = 0  # A distância da raiz para si mesma é 0

    for c in range(grafo.qtdVertices() - 1):
        u = distancia_minima(distance, visited)
        visited[u] = True

        for v in range(grafo.qtdVertices()):
            if not visited[v] and grafo.MatrizAdj[u][v] != 0 and distance[u] != math.inf \
                and distance[u] + grafo.MatrizAdj[u][v] < distance[v]:
                distance[v] = distance[u] + grafo.MatrizAdj[u][v]
                predecessor[v] = u
    print_caminhos(distance, predecessor, root)
    return distance, predecessor

def print_caminhos(distances, predecessors, root):

    for v in range(len(distances)):
        if distances[v] != math.inf:  # Se o vértice é acessível
            caminho = []
            atual = v
            
            # Reconstrói o caminho a partir do predecessor
            while atual is not None:
                caminho.append(atual + 1)  # +1 para ajustar a indexação
                atual = predecessors[atual]
            
            caminho.reverse()  # Inverte o caminho para começar de 's' até 'v'
            d = distances[v]
            print(f"{v + 1}: {','.join(map(str, caminho))}; d={int(d)}")  # Formata a saída

def distancia_minima(distancias, visitados):
    minimo = math.inf
    indice = -1
    for i in range(len(distancias)):
        if not visitados[i] and distancias[i] < minimo:
            minimo = distancias[i]
            indice = i
    return indice


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso correto: python3 A1_2.py <arquivo_de_entrada> <vértice_de_origem>")
        sys.exit(1)

    input_file = sys.argv[1]
    root = int(sys.argv[2]) - 1  # Convertendo para índice baseado em zero

    grafo = Grafo()

    try:
        grafo.read_lines(input_file)

        # Verificando se o vértice de origem é válido
        if root < 0 or root >= grafo.qtdVertices():
            print("Vértice inválido")
            sys.exit(1)
        
        # Calcula as distâncias e os predecessores a partir do vértice de origem

        distancias, predecessores = Dijkstra(grafo, root)
                
        
    except FileNotFoundError:
        print("Arquivo não encontrado")
        sys.exit(1)
