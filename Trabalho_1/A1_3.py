from A1_1 import Grafo, Vertice
import sys

def Hierholzer(grafo):
    # Inicializa a matriz de arestas visitadas como False
    arestas_visitadas = [[None for _ in range(grafo.qtdVertices())] for _ in range(grafo.qtdVertices())]
    no_inicio = None

    # Encontra um vértice com arestas (inicializa no_inicio)
    for i in range(grafo.qtdVertices()):
        for j in range(grafo.qtdVertices()):
            if grafo.haArresta(i+1, j+1) == True and i != j:
                # Se existe uma aresta, define como nao visitada
                if no_inicio is None:
                    no_inicio = i+1  
                arestas_visitadas[i][j] = False  

    # Se não há arestas, retorna False
    if no_inicio is None:
        return False, None
    

    # Invocando a função auxiliar
    r, ciclo = buscarSubcicloEuleriano(grafo, no_inicio, arestas_visitadas)
    return r, ciclo
    

    
    

def buscarSubcicloEuleriano(grafo: Grafo, v: Vertice, arestas: list):
    # Adiciona o vértice ao subciclo e define o vértice atual como v
    ciclo = [v]
    t = v
    

    while True:
        # Pegando os vizinhos do vértice atual
        vizinhos = grafo.Vertices[v-1].getVizinhos()
        # Percorrendo somente se houver arestas não visitadas
        existe_nao_visitada = False
        for u in vizinhos:
            if arestas[v-1][u-1] == False:
                arestas[v-1][u-1] = True
                arestas[u-1][v-1] = True
                ciclo.append(u)
                v = u
                existe_nao_visitada = True
                break
        # Se não houver arestas não visitadas, retorna o ciclo
        if not existe_nao_visitada:
            return False, None
        if v == t:
            break
    
    # Percorrendo os vizinhos dos nós do ciclo que não foram visitados
    # Percorrendo os vizinhos dos nós do ciclo que não foram visitados
    for x in ciclo:
        vizinhos = grafo.Vertices[x - 1].getVizinhos()  # x - 1, porque 'ciclo' usa 'v + 1'
        for u in vizinhos:
            if arestas[x - 1][u-1] == False:  # Verificação de arestas não visitadas
                r, subciclo = buscarSubcicloEuleriano(grafo, x, arestas)
                if not r:
                    return False, None
                else:
                    ciclo = ciclo[:ciclo.index(x)] + subciclo + ciclo[ciclo.index(x)+1:]
    return True, ciclo


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso correto: python3 A1_2.py <arquivo_de_entrada>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Inicializando o grafo
    G = Grafo()

    try:
        G.read_lines(input_file)

        # Buscando o ciclo euleriano
        r, ciclo = Hierholzer(G)
        if r == False:
            print("0")
        else:
            print("1")
            print(','.join(map(str, ciclo)))

        
    except FileNotFoundError:
        print("Arquivo não encontrado")
        sys.exit(1)