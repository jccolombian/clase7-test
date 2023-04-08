def sumar_5_enteros():
    # definición de variables
    lista = []
    contadorWhile = 0
    tamano = 5
    suma = 0

    # Ingresamos los números:
    while contadorWhile < tamano:
        lista.append(int(input("Ingrese número "+str(contadorWhile) +": ")))
        contadorWhile +=1

    # Sumamos los números:
    contadorWhile = 0
    while contadorWhile < tamano:
        suma += lista[contadorWhile]
        contadorWhile +=1

    print("Los elementos de la lista son:")
    for numero in lista:
        print(numero,end=', ')

    print("\nLa suma de todos sus elementos es:")
    print(suma)

def primeros_cuatro_meses():

    '''
        Definir una lista por asignación que almacene los nombres de los
        primeros cuatro meses del año.
        Mostrar el primer y último elemento de la lista.
    '''

    meses = ["enero","febrero","marzo","abril",
             "mayo","junio","julio","agosto",
             "septiembre","octubre","noviembre","diciembre"]

    print(f'Primer mes del año {meses[0]}')
    print(f'Segundo mes del año {meses[1]}')
    print("Meses del año:")
    for mes in meses:
        print(mes)

