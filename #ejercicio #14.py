#ejercicio #14

try:
    dividiendo = float(input("ingresa el dividendo:"))
    divisor = float(input("ingresa el divisor:"))

    resultado = dividiendo / divisor

    print("el resultado de la division es: ",resultado)
except ZeroDivisionError:
    print("Error:no se puede dividir entre cero ")
