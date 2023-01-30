import random


def adivina():
    num1 = int(input("Indicar un numero del 1-100: "))
    num2 = random.randrange(1, 100)
    if num1 == num2:
        return 'Molt bé! Has endevinat el número!'
    elif num1<num2:
        print('El número és més gran')
        return adivina()
    else:
        print('El número és més petit')
        return adivina()


