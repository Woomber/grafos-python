"""
Algoritmo de Búsqueda de Caminos en Grafos (Dijkstra)
Yael Chavoya
"""
from grafo import Grafo
from typing import List, Dict, Tuple


def _obtener_no_recorridos(recorridos: List[bool]) -> List[int]:
    """
    Obtiene los índices de los nodos no recorridos por el algoritmo

    :param recorridos: Una lista de bool donde True significa que el nodo ya se ha recorrido
    :return: Una lista con los índices de la lista original que no han sido recorridos
    """

    return [idx for idx, estado in enumerate(recorridos) if not estado]


def _build_path(grafo: Grafo, padres: List[int or None]) -> Dict[str, List[str]]:
    """
    Reconstruye los caminos del grafo a partir de una lista de índices de nodos padre

    :param grafo: El grafo con las conexiones
    :param padres: Una lista tal que el índice de cada elemento es el índice del nodo hijo del
        valor de dicho elemento
    :return: Un diccionario donde la clave es el nodo y el valor es una lista que contiene el camino para llegar al nodo
    """
    paths: Dict[str, List[str]] = dict()

    for idx, nodo in enumerate(grafo.nodos):
        paths[nodo] = list()

        # Todos los caminos incluyen al nodo mismo
        paths[nodo].insert(0, nodo)
        curr_idx = padres[idx]

        # Si curr_idx es None quiere decir que el camino llegó al inicio (nodo "raíz")
        while curr_idx is not None:
            paths[nodo].insert(0, grafo.nodos[curr_idx])
            curr_idx = padres[curr_idx]

    return paths


def dijkstra(grafo: Grafo, origen: str) -> Tuple[Dict[str, float], Dict[str, List[str]]]:
    """
    Utiliza el algoritmo de Dijkstra para encontrar la distancia de un nodo a todos los demás

    :param grafo: El grafo que contiene la información
    :param origen: El nodo origen de la búsqueda
    :return: Una lista con la distancia del origen a cada nodo (infinito si no hay camino) y un diccionario donde
        cada clave es un nodo del grafo y el valor es una lista que contiene el camino para llegar a ese nodo
    """
    if origen not in grafo.nodos:
        raise KeyError('El nodo no se encuentra en el grafo')

    origen_idx = grafo.nodos.index(origen)

    # Distancias almacena la distancia mínima a cada nodo
    distancias: List[float] = [float('inf') for _ in grafo.nodos]

    # Recorridos almacena cuáles nodos ya fueron recorridos por el algoritmo
    recorridos: List[bool] = [False for _ in grafo.nodos]

    # Padres almacena a través de cuál nodo se llegó a la distancia más corta de cada nodo
    padres: List[int or None] = [None for _ in grafo.nodos]

    # Procesar todos los nodos directamente conectados al origen
    for nodo in grafo.get_conectados(origen).keys():
        padres[grafo.nodos.index(nodo)] = origen_idx

    # Obtener las distancias iniciales usando la matriz de adyacencia
    # Colocará infinito en aquellos no conectados
    for idx in range(len(grafo.nodos)):
        distancias[idx]: float = grafo.matriz_ady[origen_idx][idx]

    # El nodo origen es recorrido desde el inicio porque la distancia es 0
    recorridos[origen_idx] = True

    # Repetir el algoritmo mientras haya nodos que no han sido recorridos
    while len(_obtener_no_recorridos(recorridos)) > 0:
        no_recorridos = {idx: distancias[idx] for idx in _obtener_no_recorridos(recorridos)}

        # Encontrar el índice del nodo no recorrido con la distancia más corta al origen
        actual_idx: int = min(no_recorridos, key=no_recorridos.get)
        recorridos[actual_idx] = True

        # Para cada nodo conectado a ese nodo
        for nodo, distancia in grafo.get_conectados(grafo.nodos[actual_idx]).items():
            idx = grafo.nodos.index(nodo)

            # Si ya fue recorrido, no hacer nada
            if recorridos[idx]:
                continue

            # Si la nueva distancia es menor que la distancia que ya se tenía, reemplazarla
            # y almacenar el nodo que llevó a este nuevo camino
            if distancias[idx] > distancias[actual_idx] + distancia:
                distancias[idx] = distancias[actual_idx] + distancia
                padres[idx] = actual_idx

    # Dar formato a la lista de distancias como un diccionario donde el nodo es la clave y la distancia el valor
    distancias_dict = {grafo.nodos[idx]: distancias[idx] for idx in range(len(distancias))}

    # Reconstruir los caminos a partir de la lista de índices de nodos padre
    caminos = _build_path(grafo, padres)

    return distancias_dict, caminos


def imprimir_camino(grafo: Grafo, origen: str, destino: str):
    """
    Imprime el grafo, la distancia entre origen y destino, y el camino

    :param grafo: El grafo al que pertenecen los nodos
    :param origen: El nodo origen
    :param destino: El nodo destino
    """

    print(f'\nEl grafo es \n{grafo}')

    distancias, caminos = dijkstra(grafo, origen)

    if distancias[destino] == float('inf'):
        print(f'No hay camino de "{origen}" a "{destino}"')
    else:
        print(f'La distancia mínima de "{origen}" a "{destino}" es de {distancias[destino]}')
        print(f'El camino seguido es {" -> ".join(caminos[destino])}')
