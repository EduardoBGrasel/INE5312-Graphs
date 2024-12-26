from math import inf

class Grafo:
    def __init__(self, V=[], direcionado=False):
        self.Vertices = V
        self.NumArestas = 0
        self.MatrizAdj = self.iniciaMatriz()
        self.direcionado = direcionado
    
    def qtdVertices(self):
        return len(self.Vertices)
    
    def qtdArestas(self):
        return self.NumArestas
    
    def grau(self, v):
        vertice = self.Vertices[v-1]
        return vertice.getGrau()
    
    def getRotulo(self, v):
        vertice = self.Vertices[v-1]
        return vertice.getRotulo()

    def iniciaMatriz(self):
        self.MatrizAdj = []
        for i in range(self.qtdVertices()):
            linha = []
            for j in range(self.qtdVertices()):
                linha.append(inf)
            self.MatrizAdj.append(linha)
        return self.MatrizAdj

        
    def haArresta(self, u,v):
        ha_aresta = self.MatrizAdj[u-1][v-1] != inf and self.MatrizAdj[u-1][v-1] != None
        return ha_aresta
    
    def peso(self, u, v):
        peso = self.MatrizAdj[u-1][v-1]
        return peso
    
    def add_vertex(self, n, rotulo):
        self.Vertices.append(Vertice(n, rotulo))
    
    def add_aresta(self, u, v, peso):
        # Como nesse exercício lidamos tanto com grafos direcionados quanto não direcionados, precisamos tratar os dois casos
        if self.direcionado == False:
            self.MatrizAdj[u-1][v-1] = peso
            self.MatrizAdj[v-1][u-1] = peso
            self.Vertices[u-1].addVizinho(v)
            self.Vertices[v-1].addVizinho(u)
            self.NumArestas += 1
        else:
            self.MatrizAdj[u-1][v-1] = peso
            self.Vertices[u-1].addVizinho(v)
            self.NumArestas += 1

    def print_arestas(self):
        print("Arestas:")
        print(self.qtdVertices())
        for i in range(self.qtdVertices()):
            for j in range(self.qtdVertices()):
                if self.MatrizAdj[i][j] != inf:
                    print(f"({i+1}, {j+1})")
        



    def read_lines(self, data):
        # Lendo o arquivo com codificação UTF-8
        with open(data, encoding='utf-8') as f:
            data = f.read()

        # Dividindo as linhas e removendo espaços extras em cada linha
        lines = [line.strip() for line in data.split('\n') if line.strip()]

        # Pegando o número de vértices e removendo a linha
        qt_vertices = int(lines[0].split(' ')[1])
        lines.pop(0)

        # Iterando cada vértice e adicionando ao grafo
        for i in range(qt_vertices):
            if lines:  # Verificando se ainda há linhas disponíveis
                line = lines.pop(0).split(' ')
                if len(line) > 1:  # Verificando se há dados suficientes
                    data = ' '.join(line[1:])
                    self.add_vertex(line[0], data)

        # Inicializando o grafo
        self.iniciaMatriz()

        # Removendo a informação de início das arestas
        if lines:  # Verifica se ainda há linhas
            lines.pop(0)

        # Lendo as arestas, adicionando ao grafo e removendo a linha, enquanto houverem linhas
        for line in lines:
            try:
                parts = line.split()  # Dividir por qualquer quantidade de espaços
                if len(parts) == 3:  # Garantir que há exatamente 3 elementos
                    vertexa, vertexb, weight = parts
                    self.add_aresta(int(vertexa), int(vertexb), float(weight))
                else:
                    print(f"Linha inválida ignorada: {line}")
            except ValueError as e:
                print(f"Erro ao processar a linha '{line}': {e}")
        
    

class Vertice:
    def __init__(self, n, rotulo):
        self.Numero = n
        self.Rotulo = rotulo
        self.grau = 0
        self.vizinhos =[]
    
    def addGrau(self):
        self.grau += 1
    
    def getGrau(self):
        return self.grau
    
    def addVizinho(self, v):
        self.vizinhos.append(v)
        self.addGrau()
    
    def getVizinhos(self):
        return self.vizinhos
    
    def getRotulo(self):
        return self.Rotulo



    