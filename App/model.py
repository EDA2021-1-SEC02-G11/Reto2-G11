"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mrgs
assert cf
import time
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(tipo):

    catalog = {'videos': None,
                'videos-id': None,
                'categorias': None,
                'category-id': None}

    catalog["country"] = {}
    catalog['videos'] = lt.newList(datastructure='SINGLE_LINKED',
                                   cmpfunction=cmpVideosIds)
    catalog['videos-id'] = mp.newMap(10000,
                                maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapVideoIds)
    catalog['categorias'] = lt.newList(datastructure=tipo,
                                    cmpfunction=cmpcategory_id)
    catalog["categories"] = mp.newMap(100,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareCategories)
    catalog['category-id'] = mp.newMap(37,
                                     maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareCategoriesIds)                               
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    if not (video["video_id"]=="#NAME?"):
        lt.addLast(catalog["videos"], video)
        mp.put(catalog['videos-id'], video['video_id'], video)

def addCategoria(catalog, categoria):
    """
    Adiciona una categoría a su respectiva lista
    """
    tag = newCategoria(categoria["name"], categoria["id"])
    mp.put(catalog['categories'], category['name'], newcategory)
    mp.put(catalog['category-id'], category['id'], newcategory)

def newCategoria(name, id):
    """
    Esta estructura almacena las categorías de sus respectivos videos.
    """
    categoria = {"name": "", "id": "",'total_videos': 0,
           'videos': None}
    categoria["name"] = name
    categoria["category_id"] = id
    return categoria

def addVideoCategory(catalog, categoria):
    
    videoid = categoria['video_id']
    categoriaid = categoria['category_id']
    entry = mp.get(catalog['category-id'], categoriaid)

    if entry:
        categoriavideo = mp.get(catalog['categories'], me.getValue(entry)['name'])
        categoriavideo['value']['total_videos'] += 1
        video = mp.get(catalog['videos-id'], videoid)
        if video:
            lt.addLast(categoriavideo['value']['videos'], video['value'])
# Funciones de consulta

def nameToIdCategory(category_name,categories):
    for i in range(1,lt.size(categories)+1):
        category=lt.getElement(categories,i)
        if category_name==category["name"]:
            return category["id"]
    return None

def getVideosByCategory(catalog, categoryname,cantidad):
    category = mp.get(catalog['categories'], categoryname)
    videos = None
    if category:
        videos = me.getValue(category)['videos']
    sorted_list=mrgs.sort(videos,cmpVideosByLikes)
    i =0
    for video in lt.iterator(sorted_list):
        print(video['title'])
        i +=1
        if i==cantidad:
            break
# Funciones utilizadas para comparar elementos dentro de una lista
def compareCategories(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0
def compareMapVideoIds(id, entry):
    identry = me.getKey(entry)
    if (id == identry):
        return 0
    elif (id > identry):
        return 1
    else:
        return -1
def cmpVideosbyViews(video1,video2):
    return (int(video1["views"]) > (int(video2["views"])))

def cmpVideosbyName(video1,video2):
    return (str(video1["title"]).lower()>str(video2["title"]).lower())

def cmpTrending(video1, video2):
    return(int(video1["trending_date"])>int(video2["trending_date"]))

def cmpVideosByLikes(video1,video2):
    comparison=float(video2['likes'])<float(video1['likes'])
    return comparison

def cmpcategory_id(name, category_id):
    return (name == category_id['name'])
def cmpVideosIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1   
def compareCategoriesNames(keyname, category):
    catentry = me.getKey(category)
    if (keyname == catentry):
        return 0
    elif (keyname > catentry):
        return 1
    else:
        return -1
def compareCategoriesIds(id, category):
    categoryentry = me.getKey(category)
    if (int(id) == int(categoryentry)):
        return 0
    elif (int(id) > int(categoryentry)):
        return 1
    else:
        return 0
# Funciones de ordenamiento
def tamaño(catalog):
    return lt.size(catalog['videos'])
def sortVideos1(catalog, size, tipo):
    try:
        sub_list = lt.subList(catalog["videos"],1,size)
        sub_list = sub_list.copy()
        if tipo == "Insertion":
            start_time = time.process_time()
            sorted_list = ints.sort(sub_list, cmpVideosbyViews)
            stop_time = time.process_time()

        elif tipo == "Selection":
            start_time = time.process_time()
            sorted_list = sets.sort(sub_list, cmpVideosbyViews)
            stop_time = time.process_time()

        elif tipo == "Shell":
            start_time = time.process_time()
            sorted_list = shls.sort(sub_list, cmpVideosbyViews)
            stop_time = time.process_time()
    
        elif tipo == "Merge":
            start_time = time.process_time()
            sorted_list = mrgs.sort(sub_list, cmpVideosbyViews)
            stop_time = time.process_time()

        elif tipo == "Quick":
            start_time = time.process_time()
            sorted_list = qcks.sort(sub_list, cmpVideosbyViews)
            stop_time = time.process_time()

        Tiempo_total = (stop_time-start_time)*1000
        return Tiempo_total, sorted_list

    except IndexError:
        pass

def sortVideos(catalog):
           
    sorted_list=mrgs.sort(catalog,cmpVideosByLikes)

    return sorted_list
