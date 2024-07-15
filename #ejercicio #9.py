#ejercicio #9
peso = float(input("ingresa tu peso en kg: "))
estatura = float(input("ingresa tu estatura en metros: "))

imc=round(peso/(estatura ** 2), 2)

print("tu indice en masa corporal es:" + repr(imc))
