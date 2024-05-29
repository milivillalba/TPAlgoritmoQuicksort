# Defini una Función llamada "quicksort" que toma como argumento una lista.
def quicksort(array):
    # Se verifica si la lista tiene 0 o 1 elementos.
    if len(array) <= 1:
        return array
    
    # Se selecciona como pivote al primer elemento de la lista.
    pivote = array[0]

    # Reorganize los elementos de la sublista donde los menores se gurden en la variable izquierda y los mayores en la variable derecha.
    izquierda = [x for x in array[1:] if x < pivote]
    derecha = [x for x in array[1:] if x >= pivote]

    # Recursivamente ordenamos las sublistas izquierda y derecha, concatenándolas con el pivote en el medio al devolver el resultado.
    return quicksort(izquierda) + [pivote] + quicksort(derecha)

#PRUEBAS:
#Lista ordenada de manera ascendente:
print("Ordenar Lista Ascedente:", quicksort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#Lista ordenada de manera descendente:
print("Ordenar Lista Descendente:",quicksort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

#Lista con elementos repetidos:
print("Ordenar Lista Repetidos:",quicksort([2,2,1,3,4,4,5]))

# Lista desordenada
print("Ordenar Lista Desordenada:",quicksort([6,4,5,3,1,2]))

