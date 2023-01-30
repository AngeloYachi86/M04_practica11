#Esta funcion compara 2 numeros y devuelve el cual es mas grande, cual es el mas pequeñ y si son iguales
def comparar():
    num1 = input("Ingresar el primer valor: ")
    num2 = input("Ingresar el segundo valor: ")
    if num1 > num2:
        return 'El numero mas grande es: {max} y El numero mas pequeño es: {min}' .format(max=num1, min=num2)
    elif num2 > num1:
        return 'El numero mas grande es: {max} y El numero mas pequeño es: {min}' .format(max=num2, min=num1)
    else:
        return "Son iguales"

