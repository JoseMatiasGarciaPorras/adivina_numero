import random


def run():
    print('Tu Pc ha pensado un número entre el 0 y el 100. Intenta adivinarlo')
    number = int(input('Introduce un número: '))
    random_number = random.randint(0, 100)
    while number != random_number:
        if number > random_number:
            print('El número introducido es mayor')
            number = int(input('Prueba otra vez: '))
        elif number < random_number:
            print('El número introducido es menor')
            number = int(input('Prueba otra vez: '))
    
    print('Has acertado!')


if __name__ == "__main__":
    run()   