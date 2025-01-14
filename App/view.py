"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print('2- Hallar los n videos con más LIKES para una categoría específica')

def printVideosPorCategoria(videos):
    if (videos):
        print('Se encontraron: ' + str(lt.size(videos)) + ' Videos.')
        for video in lt.iterator(videos):
            print(video['title'])
        print("\n")
    else:
        print("NF")
catalog = None

def initCatalog(tipo):
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(tipo)


def loadData(catalog):
    
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

    elif int(inputs[0]) == 2:
        label = input("Categoria a buscar: ")
        n = int(input("Ingrese el n: "))
        videos = controller.getVideosByCategory(cont, label, n)
    elif int(inputs[0]) == 0:
        menu = Fals    
    else:
        sys.exit(0)
sys.exit(0)
