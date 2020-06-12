from collections import deque
import math

class Grafo:

    def __init__(self): #lo mismo que this es c
        self.vertices=[]
        self.matriz=[[None]*0 for i in range(0)]
#seinicia la var en none o vacia creo el array y que lo creo completo vacio
    
    #si noso a existe en el array y si no esta return true
    def esta_en_vertices(self,v):
        if self.vertices.count(v)==0:
            return False
        return True
    
    #aqui agrega
    def agregar_vertices(self,v):
        if self.esta_en_vertices(v):
            return False
        self.vertices.append(v)

#redimension de la matriz de ad
        filas=columnas=len(self.matriz)
        matriz_aux=[[None]*(filas+1)for i in range(columnas +1)]

        #recorre la matriz y copia su contenido dentro de la matriz mas grande
        for i in range(filas):
            for j in range(columnas):
                matriz_aux[i][j]=self.matriz[i][j]

        #iguala la matriz a la matriz mas grande
        self.matriz=matriz_aux
        return True

    def agregar_arista(self,fin,inicio,valor,dirijida):

        if not(self.esta_en_vertices(inicio)) or not(self.esta_en_vertices(fin)):
            return False
#si el vertice de inicio o de fin no estan en la lista da false
        #si estan contenidos en la lista de vertices
        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)]=valor  

    #pregunta si existen los nodos de inicio y fin y se existen entonces agrega valor que es el 1 en la matriz

    def imprimir_matriz(self,m,texto):
        cadena=""

        #columns
        for i in range(len(m)):
            cadena += "\t" + str(self.vertices[i])

        cadena+= "\n" + ("    -"*len(m))
        
        #filas
        for j in range(len(m)):
            cadena+="\n" + str(self.vertices[j]) + " |"
            for i in range(len(m)):
                if texto:
                    cadena +="\t"+str(m[i][j])
                else:
                    if m[i][j] is None or math.isinf(m[i][j]):
                        cadena+="\t"+ "0"
                    else:
                        cadena+="\t"+str(m[i][j])
        cadena+="\n"
        print(cadena)
    
    def imprimirLista(self,matriz,raiz):
        print(raiz,end="")
        for i in range(len(matriz)):
            if not matriz[i][self.vertices.index(raiz)]==None:
                print("-"+str(matriz[i][self.vertices.index(raiz)])+"->"+self.vertices[i],end="")

        print("")


if __name__=="__main__":
    g=Grafo()

    g.agregar_vertices("A")
    g.agregar_vertices("B")
    g.agregar_vertices("C")
    g.agregar_vertices("D")
    g.agregar_vertices("E")
    g.agregar_vertices("F")

#aqui solo se agregan los que estan conectados , que si tienenrelacion
    g.agregar_arista("A","B",1,False)
    g.agregar_arista("A","D",1,False)
    g.agregar_arista("A","F",1,False)
    g.agregar_arista("B","A",1,False)
    g.agregar_arista("B","C",1,False)
    g.agregar_arista("C","B",1,False)
    g.agregar_arista("D","A",1,False)
    g.agregar_arista("D","E",1,False)
    g.agregar_arista("E","D",1,False)
    g.agregar_arista("F","D",1,False)
    g.agregar_arista("F","A",1,False)
    g.imprimir_matriz(g.matriz,False)

    g.imprimirLista(g.matriz,"A")
    g.imprimirLista(g.matriz,"B")
    g.imprimirLista(g.matriz,"C")
    g.imprimirLista(g.matriz,"D")
    g.imprimirLista(g.matriz,"E")
    g.imprimirLista(g.matriz,"F")