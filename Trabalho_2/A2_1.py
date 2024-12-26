import sys
from Grafo import Grafo, Vertice

def exibir_cfc(grafo: Grafo):
    # Faz a busca em profundidade no grafo original
    C, T, F, A = dfs_cormen(grafo)

    # Cria o grafo transposto
    grafo_transposto = criar_grafo_transposto(grafo)

    # Faz a busca em profundidade no grafo transposto
    Ctransposto, Ttransposto, Atransposto, Ftransposto = dfs_adaptado(grafo_transposto, F)



    # Exibe as componentes fortemente conexas
    exibir_componentes(Atransposto, grafo_transposto)

def exibir_componentes(antecessores, grafo: Grafo):
    # Inicializa a lista de componentes fortemente conexas
    componentes = []

    # Identifica as raízes das árvores de busca em profundidade
    vertices = set(antecessores.keys())
    filhos = set(valor for valor in antecessores.values() if valor is not None)

    # Adiciona as raízes das árvores de busca em profundidade à lista de componentes/
    raizes = vertices - filhos

    for raiz in raizes:
        sub_arvore = []
        atual = raiz
        while atual is not None:
            sub_arvore.append(atual)
            atual = antecessores[atual]
        componentes.append(sub_arvore)

    # Exibe as componentes fortemente conexas
    for componente in componentes:
        print(", ".join(str(v) for v in componente))

def criar_grafo_transposto(grafo: Grafo):
    # Guarda os vertices do grafo original, mas sem arestas
    vertices = []
    for v in grafo.Vertices:
        vertice = Vertice(v.Numero, v.Rotulo)
        vertices.append(vertice)

    # Cria um novo grafo com os vértices do grafo original
    grafo_transposto = Grafo(direcionado=True, V=vertices)
    
    # Adiciona as arestas invertidas do grafo original no grafo transposto
    for i in range(grafo.qtdVertices()):
        u = grafo.Vertices[i]
        for v in u.vizinhos:
            grafo_transposto.add_aresta(v, int(u.Numero), grafo.peso(int(u.Numero), v))

    return grafo_transposto

def dfs_cormen(grafo: Grafo):
    # Inicializando variáveis de controle
    C = {v: False for v in range(1, grafo.qtdVertices() + 1)}  # Visitado
    T = {v: float('inf') for v in range(1, grafo.qtdVertices() + 1)}  # Tempo de início
    F = {v: float('inf') for v in range(1, grafo.qtdVertices() + 1)}  # Tempo de finalização
    A = {v: None for v in range(1, grafo.qtdVertices() + 1)}  # Antecessor

    tempo = [0]  # Usando uma lista para que 'tempo' seja mutável e compartilhado entre chamadas

    for v in range(1, grafo.qtdVertices()):
        if not C[v]:
            dfs_visit_cormen(v, grafo, C, T, F, A, tempo)
    
    return C, T, F, A

def dfs_visit_cormen(v: int, grafo: Grafo, C: list, T: list, F: list, A: list, tempo: list):
    C[v] = True
    tempo[0] += 1
    T[v] = tempo[0]

    for u in grafo.Vertices[v-1].getVizinhos():
        if not C[u]:
            A[u] = v
            dfs_visit_cormen(u, grafo, C, T, F, A, tempo)

    tempo[0] += 1
    F[v] = tempo[0]

def dfs_adaptado(grafo: Grafo, F_original: dict):
    # Inicializando variáveis de controle
    C = {v: False for v in range(1, grafo.qtdVertices() + 1)}  # Visitado
    T = {v: float('inf') for v in range(1, grafo.qtdVertices() + 1)}  # Tempo de início
    F = {v: F_original[v] for v in range(1, grafo.qtdVertices() + 1)}  # Tempo de finalização
    A = {v: None for v in range(1, grafo.qtdVertices() + 1)}  # Antecessor

    tempo = [0] 

    # Ordena os vértices de acordo com o tempo de finalização no grafo original
    vertices = sorted(F, key=F.get, reverse=True)
    for v in vertices:
        if not C[v]:
            dfs_visit_cormen(v, grafo, C, T, F, A, tempo)
    return C, T, A, F



    
def main():
    if len(sys.argv) != 2:
        print("Uso correto: python3 A2_1.py <arquivo_de_entrada>")
        sys.exit(1)

    input_file = sys.argv[1]
    grafo = Grafo(direcionado=True)

    try:
        grafo.read_lines(input_file)
        exibir_cfc(grafo)

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()