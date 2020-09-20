"""
Clase Grafo
Yael Chavoya
"""
from typing import List, Dict


class Grafo:

    def __init__(self, *nodos: str):
        """
        Constructor

        :param nodos: Identificadores de nodos del grafo (Opcional)
        """

        self.nodos: List[str] = []

        # Crear una matriz de adyacencia vacía
        self.matriz_ady: List[List[float]] = [[float('inf')]*0 for _ in range(0)]

        for nodo in nodos:
            self.add(nodo)

    def __str__(self) -> str:
        """
        Devuelve una representación string del grafo

        :return: Un string con nodos y matriz de adyacencia
        """
        ret = f'{self.nodos} -> [\n'
        for row in self.matriz_ady:
            ret += f'\t{row}\n'
        ret += ']'
        return ret

    def add(self, *nodos: str) -> bool:
        """
        Agrega uno o varios nodos nuevos al grafo

        :param nodos: Los identificadores de los nodos
        :return: True si todos los nodos se agregaron
        """

        for nodo in nodos:
            # Verificar si el nodo ya está en la lista
            if nodo in self.nodos:
                return False

            self.nodos.append(nodo)

            # Cambiar el tamaño de la matriz de adyacencia
            new_size = len(self.nodos)
            new_matriz: List[List[float]] = [[float('inf')] * new_size for _ in range(new_size)]
            for row in range(new_size - 1):
                for col in range(new_size - 1):
                    new_matriz[row][col] = self.matriz_ady[row][col]
            self.matriz_ady = new_matriz

            # La distancia de un nodo a sí mismo es 0
            self.matriz_ady[new_size - 1][new_size - 1] = 0

        return True

    def remove(self, nodo: str) -> bool:
        """
        Eliminar un nodo del grafo

        :param nodo: El nodo a eliminar
        :return:True si el nodo se eliminó
        """

        if nodo not in self.nodos:
            return False

        idx = self.nodos.index(nodo)

        # Eliminar de la lista de nodos
        self.nodos.pop(idx)

        # Eliminar de la matriz de adyacencia
        self.matriz_ady.pop(idx)
        for row in self.matriz_ady:
            row.pop(idx)

        return True

    def connect(self, v1: str, v2: str, distancia: float) -> bool:
        """
        Conecta dos vértices con un arista

        :param v1: Nodo origen
        :param v2: Nodo destino
        :param distancia: El peso del arista
        :return: True si los vértices fueron conectados
        """

        # No conectar si los nodos no están en el grafo
        if v1 not in self.nodos and v2 not in self.nodos:
            return False

        # No conectar si es el mismo nodo
        if v1 == v2:
            return False

        idx1 = self.nodos.index(v1)
        idx2 = self.nodos.index(v2)

        # Conectar v1 a v2 y v2 a v1, porque es un grafo no dirigido
        self.matriz_ady[idx1][idx2] = distancia
        self.matriz_ady[idx2][idx1] = distancia

        return True

    def get_conectados(self, nodo: str) -> Dict[str, float]:
        """
        Devuelve los nodos conectados a un nodo y su peso

        :param nodo: El nodo a evaluar
        :return: Un diccionario con los nodos conectados al nodo y su peso
        """

        if nodo not in self.nodos:
            raise KeyError('El nodo no se encuentra en el grafo')

        nodo_idx = self.nodos.index(nodo)

        conectados: Dict[str, float] = dict()

        for idx, n in enumerate(self.nodos):
            distancia = self.matriz_ady[nodo_idx][idx]

            # Si la distancia es infinita, no están conectados
            # Además, excluir el mismo nodo
            if distancia != float('inf') and idx != nodo_idx:
                conectados[n] = distancia

        return conectados
