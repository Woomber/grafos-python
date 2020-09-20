"""
Visualización gráfica de Grafos usando pyplot y networkx
Yael Chavoya
"""
import networkx as nx
import matplotlib.pyplot as plt
from grafo import Grafo


def visualizar_grafo(grafo: Grafo):
    """
    Abre un plot de pyplot con una representación gráfica del grafo

    :param grafo: El grafo a dibujar
    """

    # Crear un grafo de networkx con los datos de nuestro grafo
    G = nx.Graph()

    # Nodos
    G.add_nodes_from(grafo.nodos)

    # Aristas
    for row_idx in range(len(grafo.matriz_ady)):
        for col_idx in range(len(grafo.matriz_ady)):
            if row_idx == col_idx:
                continue
            weight = grafo.matriz_ady[row_idx][col_idx]
            if weight == float('inf'):
                continue
            G.add_edge(grafo.nodos[row_idx], grafo.nodos[col_idx], weight=weight)

    # Crear un plot nuevo
    plt.plot()

    # Establecer el algoritmo para posicionar los nodos
    pos = nx.spring_layout(G)

    # Colocar el peso como etiqueta de los aristas
    labels = nx.get_edge_attributes(G, 'weight')

    # Dibujar y mostrar el grafo
    nx.draw(G, pos, with_labels=True, node_color="#aaa", node_size=800, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
