#El programa realiza la operacion para conocer cuales son los numeros primos entre 1 y 250
import os 

#Definimos una funcion para evaluar el número
def es_primo(num):
    """
    Funcion que evalua si un número es primo o no
    """
    #Evaluamos si el numero que viene como parametro es menor o igual a 1 y de ser así devuelve false
    if num <= 1:
        return False
    
    #
    for i in range(2, num):
        if num % i ==0:
            return False

    return True


def calcular_y_almacenar_numeros():
    """
    Funcion que manda los numeros  a evaluar llamando a la funcion es_primo
     y los almacena en un archivo si son primos.
    
    """
    #Abrimos el archivo en modo de escritura
    with open('results.txt', 'w') as archivo:
        x=1
        #Calcula los números primos que el usuario haya ingresado y los almacena en un archivo
        while x < numero_ingresado:
            if es_primo(x):
                print(f'{x} es número primo')
                archivo.write(f'{x} es un número primo\n')
            x+=1

def main():
    calcular_y_almacenar_numeros()

while True:
    try:
        numero_ingresado = int(input('Ingrese hasta que número desea conocer si es primo o no: '))
        break
    except:
        print('Debe de ingresar un número entero')  


#Guardamos la ruta de nuestro archivo en una variable
ruta_absoluta = os.path.abspath('results.txt')
print(ruta_absoluta)

if __name__ == '__main__':
    main()

input('Presione "enter" para salir:')