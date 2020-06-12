#encoding utf-8
from collections import deque
import math
import numpy as np

class Grafo:

  def __init__(self):
        self.vertices = []
        self.matriz = [[None]*0 for i in range(0)]

  def esta_en_vertices(self, v):
        if self.vertices.count(v) == 0:
            return False
        return True
  def agregar_vertices(self, v):
        if self.esta_en_vertices(v):
            return False
        # Si no esta contenido.
        self.vertices.append(v)

        # Redimensiono la matriz de adyacencia.
        filas = columnas = len(self.matriz)
        matriz_aux = [[None] * (filas+1) for i in range(columnas+1)]

        # Recorro la matriz y copio su contenido dentro de la matriz mas grande.
        for i in range(filas):
            for j in range(columnas):
                matriz_aux[i][j] = self.matriz[i][j]

        # Igualo la matriz a la matriz mas grande.
        self.matriz = matriz_aux
        return True

  def agregar_arista(self, fin, inicio, valor, dirijida):

        if not(self.esta_en_vertices(inicio)) or not(self.esta_en_vertices(fin)):
            return False
        # Si estan contenidos en la lista de vertices.
        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = valor

        # Si la arista entrante no es dirijida.
        # Instancio una Arista en sentido contrario de Fin a Inicio.
        #if not dirijida:
         #   self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = valor
        #return True

  def imprimir_matriz(self, m, texto):
        cadena = ""
        #Columnas 
        for i in range(len(m)):
            cadena += "\t" + str(self.vertices[i])

        cadena += "\n " + ("       -" * len(m))
        #Filas
        for j in range(len(m)):
            cadena += "\n" + str(self.vertices[j]) + " |"
            for i in range(len(m)):
                if texto:
                    cadena += "\t" + str(m[i][j])
                else:
                
                        if m[i][j] is None or math.isinf(m[i][j]):
                            cadena += "\t" + "0"
                        else:
                            cadena += "\t" + str(m[i][j])

        cadena += "\n"
        print(cadena)


if __name__ == "__main__":

    
    g = Grafo()

    g.agregar_vertices("A")
    g.agregar_vertices("B")
    g.agregar_vertices("C")
    g.agregar_vertices("D")
    g.agregar_vertices("E")
    g.agregar_vertices("F")
    g.agregar_vertices("G")

    g.agregar_arista("A","B",1,False)
    g.agregar_arista("A","C",1,False)
    g.agregar_arista("A","D",1,False)
    g.agregar_arista("B","A",1,False)
    g.agregar_arista("C","A",1,False)
    g.agregar_arista("C","D",1,False)
    g.agregar_arista("D","A",1,False)
    g.agregar_arista("D","C",1,False)
    g.agregar_arista("D","E",1,False)
    g.agregar_arista("E","D",1,False)
    g.agregar_arista("F","G",1,False)

    
    g.imprimir_matriz(g.matriz, False)