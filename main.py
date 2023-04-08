from problema1 import sumar_5_enteros, primeros_cuatro_meses
import alumnos

'''
Hasta ahora hemos
trabajado con variables
que permiten almacenar
un único valor
'''

edad = 12

altura = 1.79

nombre = "Juan"

'''
En python podemos
usar una variable
que almacena una
colección de datos
y luego accederla
usando un subíndice
'''

# lista de enteros
lista1 = [10, 5, 3, 9]
# lista de decimales
lista2 = [1.78, 2.66, 1.55, 89.4]
# lista de string
lista3 = ["Lunes","Martes","Miercolés"]
'''
lista de elementos
de distinto tipo
'''
lista4 = ["juan",45,1.92]


if __name__ == '__main__':

    '''
    Cantidad de elementos de cada lista:
    '''
    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print()

    sumar_5_enteros()

    print()

    primeros_cuatro_meses()

    print()

    alumnos.alumnos()
