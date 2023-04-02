cidades = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurglu': 77,
    'Hirsova': 151,
    'Lasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

import heapq

class priorityQueue:
    def __init__(self):
        self.cidades = []
    def push(self, cidade, custo):
        heapq.heappush(self.cidades, (custo, cidade))
    def pop(self):
        return heapq.heappop(self.cidades)[1]
    def isEmpty(self):
        if (self.cidades == []):
            return True
        else:
            return False
    def check(self):
        print(self.cidades)

class Graph:
    def __init__(self, Cidades):
        self.cidades = Cidades
        self.dic_adjacencia = {}

        for cidade in self.cidades:
            self.dic_adjacencia[cidade] = []


    def add_vertice(self):
        file = open("romania.txt", 'r')
    
        for string in file:
            line = string.split(',')
            ct1 = line[0]
            ct2 = line[1]
            dist = int(line[2])
            self.dic_adjacencia.setdefault(ct1, []).append({"cidade":ct2,"distancia":dist})
            self.dic_adjacencia.setdefault(ct2, []).append({"cidade":ct1,"distancia":dist})


        
    
    def print_dic_adjacencia(self):
        vizinhos_aux = []
        for cidade, vizinhos in self.dic_adjacencia.items():
            for adjacencia in vizinhos:
                vizinhos_aux.append(adjacencia['cidade'])
            print(cidade + '->'+ str(vizinhos_aux))
            vizinhos_aux.clear()

    def A_estrela(self,comeco,final):
        caminho = {}
        visitados = {}
        q = priorityQueue()
        h = self.cidades
        q.push(comeco,0)
        visitados[comeco] = 0
        caminho[comeco] = None
        listaExpandida = []

        while(q.isEmpty()==False):
            #usa o heap para que quando tirar algo da fila sempre seja o de maior prioridade
            # ou seja o que tiver o menor f_cost(distancia do nosso objetivo + distancia pra chegar no viznho)
            atual = q.pop()
            listaExpandida.append(atual)
            if(atual== final):
                break
            #verifica todos os vizinhos da nossa cidade inicial
            for new in self.dic_adjacencia[atual]:
                #g_cost = distancia de onde estamos em relacao ao nosso objetivo + caminho para nosso para chegar no vizinho
                g_cost = visitados[atual] + int(new["distancia"])
                # verifica se cidade vizinha ja foi visitada ou g_cost é menor que
                if(new["cidade"] not in visitados or g_cost < visitados[new["cidade"]]):
                    teste = new["cidade"]
                    visitados[new["cidade"]] = g_cost
                    #desiste de tentar explicar esse F ai muito confuso pra minha cabecinha
                    f_cost = g_cost + heuristic(new["cidade"], h)
                    #Adiciona o vizinho e o custo dele para minha que de prioridade
                    q.push(new["cidade"], f_cost)
                    #fala o caminho que fizemos
                    caminho[new["cidade"]] = atual
        printoutput(comeco, final, caminho,visitados,listaExpandida)

def heuristic(node, values):
    return values[node]

def printoutput(start, end, path, visitados, expandedlist):
    finalpath = []
    i = end
    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    print("A-star Agorithm para o mapa da Romenia")
    print("\t",start, "=>", end)
    print("=======================================================")
    print("Lista de cidades possiveis : " + str(expandedlist))
    print("Numero Total de ciades possiveis : " + str(len(expandedlist)))
    print("=======================================================")
    print("caminho final : ", end ='')
    for cidade in finalpath:
        if cidade != finalpath[-1]:
            print(cidade,"=>",end='')
        else:
            print(cidade)
    print("Numero total de cidades no nosso caminho final : " + str(len(finalpath)))
    print("Custo total : " + str(visitados[end]))


grafo = Graph(cidades)
grafo.add_vertice()
grafo.A_estrela("Arad","Bucharest")



