"""
Interfaz de comandos
Yael Chavoya
"""
from grafo import Grafo
from caminos import imprimir_camino
import ejemplos
import gui


def _clear_screen():
    """
    Colocar espaciado entre menú y menú
    """
    print('\n'*3)


def _wait_enter():
    """
    Esperar a que el usuario presione ENTER
    """
    input('Presione ENTER para continuar...')
    _clear_screen()


def _agregar_nodo(grafo: Grafo):
    """
    Agregar un nodo al grafo
    :param grafo: El grafo donde se agregará el nodo
    """
    while True:
        nombre = input('Ingrese un nombre para el nuevo nodo (ENTER para cancelar): ')
        if len(nombre) == 0:
            _clear_screen()
            break
        if grafo.add(nombre):
            print(f'Nodo "{nombre}" agregado correctamente\n')
            _wait_enter()
            break
        else:
            print(f'El nodo "{nombre}" ya existe\n')


def _eliminar_nodo(grafo: Grafo):
    """
    Eliminar un nodo del grafo
    :param grafo: El grafo donde se eliminará el nodo
    """
    if len(grafo.nodos) == 0:
        print('No hay nodos en el grafo')
        _wait_enter()
        return
    while True:
        print(f'Nodos disponibles: {grafo.nodos}')
        nombre = input('Ingrese el nombre del nodo a ELIMINAR (ENTER para cancelar): ')
        if len(nombre) == 0:
            _clear_screen()
            break
        if grafo.remove(nombre):
            print(f'Nodo "{nombre}" eliminado correctamente\n')
            _wait_enter()
            break
        else:
            print(f'El nodo "{nombre}" no está en el grafo\n')


def _conectar_nodos(grafo: Grafo):
    """
    Conectar dos nodos del grafo
    :param grafo: El grafo donde se conectarán los nodos
    """
    if len(grafo.nodos) < 2:
        print('No hay nodos suficientes en el grafo')
        _wait_enter()
        return
    while True:
        print(f'Nodos disponibles: {grafo.nodos}')
        nombre1 = input('Ingrese el nombre del nodo ORIGEN (ENTER para cancelar): ')
        if len(nombre1) == 0:
            _clear_screen()
            break

        if nombre1 not in grafo.nodos:
            print(f'El nodo "{nombre1}" no está en el grafo\n')
            continue

        while True:
            nombre2 = input('Ingrese el nombre del nodo DESTINO (ENTER para volver): ')
            if len(nombre2) == 0:
                break

            if nombre2 not in grafo.nodos:
                print(f'El nodo "{nombre2}" no está en el grafo\n')
                continue

            if nombre1 == nombre2:
                print(f'No se puede conectar un nodo a sí mismo\n')
                continue

            while True:
                dist = input(f'Ingrese la distancia entre "{nombre1}" y "{nombre2}" (ENTER para volver): ')
                if len(dist) == 0:
                    break
                try:
                    dist_n = float(dist)
                    if grafo.connect(nombre1, nombre2, dist_n):
                        print(f'Conectado "{nombre1}" a "{nombre2}" con distancia de {dist_n}')
                    else:
                        print(f'Ha ocurrido un error conectando "{nombre1}" a "{nombre2}" con distancia de {dist_n}')
                    _wait_enter()
                    return

                except ValueError:
                    print('Por favor ingrese un número')

def _ver_matriz_ady(grafo: Grafo):
    """
    Visualizar un grafo

    :param grafo: El grafo a visualizar
    """
    if len(grafo.nodos) == 0:
        print('El grafo está vacío')
    else:
        print(grafo)
    _wait_enter()


def _mostrar_grafo(grafo: Grafo):
    print('Mostrando en pyplot...')
    gui.visualizar_grafo(grafo)
    _wait_enter()


def _buscar_camino(grafo: Grafo):
    """
    Ver el camino más corto entre dos nodos
    :param grafo: El grafo donde se hará la búsqueda
    """
    if len(grafo.nodos) < 2:
        print('No hay nodos suficientes en el grafo')
        _wait_enter()
        return
    while True:
        print(f'Nodos disponibles: {grafo.nodos}')
        origen = input('Ingrese el nombre del nodo ORIGEN (ENTER para cancelar): ')
        if len(origen) == 0:
            _clear_screen()
            break

        if origen not in grafo.nodos:
            print(f'El nodo "{origen}" no está en el grafo\n')
            continue

        while True:
            destino = input('Ingrese el nombre del nodo DESTINO (ENTER para volver): ')
            if len(destino) == 0:
                break

            if destino not in grafo.nodos:
                print(f'El nodo "{destino}" no está en el grafo\n')
                continue

            imprimir_camino(grafo, origen, destino)
            _wait_enter()
            return


def main_menu():
    """
    Menú principal
    """

    grafo = Grafo()
    entrada: str = ''

    while entrada != '0':
        print('====== Grafos ======\nAutor: Yael Chavoya\n')
        print('Seleccione una opción:')
        print('1: Agregar nodo')
        print('2: Eliminar nodo')
        print('3: Conectar nodos')
        print('4: Ver matriz de adyacencia')
        print('5: Ver grafo')
        print('6: Buscar camino')
        print('7: Ver ejemplo')
        print('0: Salir')

        entrada = input('> ')
        print()

        if entrada == '0':
            break
        elif entrada == '1':
            _agregar_nodo(grafo)
        elif entrada == '2':
            _eliminar_nodo(grafo)
        elif entrada == '3':
            _conectar_nodos(grafo)
        elif entrada == '4':
            _ver_matriz_ady(grafo)
        elif entrada == '5':
            _mostrar_grafo(grafo)
        elif entrada == '6':
            _buscar_camino(grafo)
        elif entrada == '7':
            g_ej = ejemplos.ciudades()
            _wait_enter()
            _mostrar_grafo(g_ej)
        else:
            print('Opción no reconocida.')
            _wait_enter()
