#ejercicio # 17
numero =int ( input("ingresa un nunero entero positivo:"))

numeros_impares = []

for i in range ( 1,numero+1,2):
    numeros_impares.append(i)

resultado = " , ".join(str(x) for x in numeros_impares)

print ( resultado)
