from math import inf

class Grafo:
    def __init__(self, V=[]):
        self.Vertices = V
        self.NumArestas = 0
        self.MatrizAdj = self.iniciaMatriz()
    
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
            
        
    def haArresta(self, u,v):
        ha_aresta = self.MatrizAdj[u-1][v-1] != inf and self.MatrizAdj[u-1][v-1] != None
        return ha_aresta
    
    def peso(self, u, v):
        peso = self.MatrizAdj[u-1][v-1]
        return peso
    
    def add_vertex(self, n, rotulo):
        self.Vertices.append(Vertice(n, rotulo))
    
    def add_aresta(self, u, v, peso):
        self.MatrizAdj[u-1][v-1] = peso
        self.MatrizAdj[v-1][u-1] = peso
        self.Vertices[u-1].addVizinho(v)
        self.Vertices[v-1].addVizinho(u)
        self.NumArestas += 1
    
    
    def read_lines(self, data):
        # Lendo o arquivo
        with open(data) as f:
            data = f.read()

        lines = data.split('\n')
        
        # Pegando o número de vértices e removendo a linha
        qt_vertices = int(lines[0].split(' ')[1])
        lines.pop(0)
        
        # Iterando cada vértice e adicionando ao grafo
        for i in range(0, qt_vertices):
            line = lines.pop(0).split(' ')
            # Dados do vértice, o que não é o número
            data = ' '.join(line[1:])
            self.add_vertex(line[0], data)

        # Inicializando o grafo
        self.iniciaMatriz()

        # Removendo a informação de inicio das arestas
        lines.pop(0)

        # Lendo as arestas, adicionando ao grafo e removendo a linha, enquanto houverem linhas (Arquivo não acabar)
        while len(lines) > 0:
            line = lines.pop(0)
            if line.strip() == '':
                break
            vertexa, vertexb, weight = line.split(' ') # Pegando peso e vértices para adicionar ao grafo
            self.add_aresta(int(vertexa), int(vertexb), float(weight) )
    
    

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



    
