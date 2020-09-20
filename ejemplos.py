"""
Ejemplos de Búsquedas de caminos
Yael Chavoya
"""
from grafo import Grafo
from caminos import imprimir_camino


def letras():
    """
    Ejemplo 1: Letras
    """

    # Crear grafo y agregar nodos
    grafo = Grafo()
    grafo.add('A', 'B', 'C', 'D')

    # Conectar nodos con sus respectivas distancias
    grafo.connect('B', 'C', 200)
    grafo.connect('B', 'A', 100)
    grafo.connect('A', 'D', 50)
    grafo.connect('D', 'C', 10)

    imprimir_camino(grafo, 'A', 'C')


def ciudades():
    """
    Ejemplo 2: Ciudades
    """

    albacete = 'Albacete'
    alicante = 'Alicante'
    cordoba = 'Córdoba'
    madrid = 'Madrid'
    valencia = 'Valencia'

    # Crear grafo y agregar nodos, esta vez mediante el constructor
    grafo = Grafo(albacete, alicante, cordoba, madrid, valencia)

    # Conectar nodos con sus respectivas distancias
    grafo.connect(albacete, alicante, 96)
    grafo.connect(albacete, cordoba, 254)
    grafo.connect(albacete, madrid, 100)
    grafo.connect(albacete, valencia, 105)
    grafo.connect(alicante, valencia, 110)
    grafo.connect(cordoba, madrid, 102)
    grafo.connect(madrid, valencia, 98)

    imprimir_camino(grafo, cordoba, alicante)
