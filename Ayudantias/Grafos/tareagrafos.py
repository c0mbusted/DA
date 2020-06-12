def bfs(L, nodoInicial):
    
    visitados = []
    
    queue = [nodoInicial]
 
    while queue:
        
        nodo = queue.pop(0)
        if nodo not in visitados:
            
            visitados.append(nodo)
            adyacentes = L[nodo]
 
            
            for vecino in adyacentes:
                queue.append(vecino)
    return visitados
############################################################
def dijkstra(grafo,nodoInicio):

    #initial = 'A'
    camino = {}
    nodoAdyacente = {}
    queue = []
    #graph = initial_graph()
    for nodo in grafo:
        camino[nodo] = float("inf")
        nodoAdyacente[nodo] = None
        queue.append(nodo)
        
    camino[nodoInicio] = 0
    while queue:
        valor = queue[0]
        minimo = camino[valor]
        for n in range(1, len(queue)):
            if camino[queue[n]] < minimo:
                valor = queue[n]  
                minimo = camino[valor]
        act = valor
        queue.remove(act)
        #print(act)
        
        for i in grafo[act]:
            alt = grafo[act][i] + camino[act]
            if camino[i] > alt:
                camino[i] = alt
                nodoAdyacente[i] = act
    
    
    final = 'I'
    print('El camino mas corto del nodo inicial hasta el nodo final es : \n')
    print(final, end = '<-')
    while True:
        final = nodoAdyacente[final]
        if final is None:
            print("")
            break
        print(final, end='<-')


#############        MAIN          ###############
if __name__ == "__main__":
    noponderado = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['F'],
         'E': ['A', 'B','D'],
         'F': ['B'],
         'G': ['C']}

            
    ponderado= {'A': {'B':5, 'C':4, 'D':2},
        'B': {'A':9, 'E':5},
        'C': {'A':7, 'F':15},
        'D': {'A':10, 'F':7},
        'E': {'B':3, 'J':7},
        'F': {'C':11, 'D':14, 'K':3, 'G':9},
        'G': {'F':15, 'I':4},
        'H': {'J':13},
        'I': {'G':6, 'J':7},
        'J': {'H':7, 'I':4},
        'K': {'F':6}            
    }
    
    opc=int(input("1. Grafo Ponderado \n 2. Grafo NO ponderado: "))
    
    if(opc==1) :
        print("\n Grafo ponderado: \n",ponderado)
        print("\nSe aplica el algoritmo Dijkstra: \n")
        print(dijkstra(ponderado,'C'))
    
    if(opc==2) :
        print("\n Lista de adyacencia no ponderada: \n",noponderado)
        print("\nSe aplica el algoritmo BFS: \n")
        print(bfs(noponderado,'C'))
