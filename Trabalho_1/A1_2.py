from A1_1 import Grafo
import math
import sys

def BFS(grafo: Grafo, root): # Função que realiza a busca em largura
        # Inicializando as listas de nós visitados, distâncias e predecessores
        visited = [False] * grafo.qtdVertices()
        distance = [math.inf] * grafo.qtdVertices()
        predecessor = [None] * grafo.qtdVertices()

        # Marcando o nó raiz como visitado e com distância 0
        visited[root-1] = True
        distance[root-1] = 0

        # Inicializando a fila
        queue = []
        queue.append(root)

        # Enquanto a fila não estiver vazia
        while len(queue) > 0:
            # Pegando o primeiro elemento da fila e verificando seus vizinhos
            u = queue.pop(0) 
            neighbors = grafo.Vertices[u-1].getVizinhos()

            # Percorrendo os vizinhos e adicionando na fila caso ele não tenha sido visitado
            for neighbor in neighbors:
                if not visited[neighbor-1]:
                    visited[neighbor-1] = True
                    distance[neighbor-1] = distance[u-1] + 1
                    predecessor[neighbor-1] = u
                    queue.append(neighbor)
        return distance, predecessor

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso correto: python3 A1_2.py <arquivo_de_entrada> <vértice_de_origem>")
        sys.exit(1)

    input_file = sys.argv[1]
    root = int(sys.argv[2])

    # Inicializando o grafo
    G = Grafo()

    try:
        G.read_lines(input_file)

        # Verificando se o vértice de origem é válido
        if root < 1 or root > G.qtdVertices():
            print("Vértice inválido")
            sys.exit(1)

        # Chamando a função para pegar a profundidade
        distancias, predecessores = BFS(G, root)

        # Imprimindo as distâncias e os predecessores
        dic_resultados = {}
        for v in range(G.qtdVertices()):
            if distancias[v] != math.inf:
                if distancias[v] in dic_resultados:
                    dic_resultados[distancias[v]] += "," + str(v+1)
                else:
                    dic_resultados[distancias[v]] = str(v+1)
        
        # Imprimindo os resultados
        for key in sorted(dic_resultados.keys()):
            print(f"{key}: {dic_resultados[key]}")

    except FileNotFoundError:
        print("Arquivo não encontrado")
        sys.exit(1)