#ejercicio # 10 

num_engranes = int(input("ingrese el numero de engranes vendidos"))
num_cilindros = int(input("ingresa el numero de cilindros vendidos"))

peso_engranes= num_engranes *112
peso_cilindros = num_cilindros * 75 
peso_total = peso_engranes + peso_cilindros

print ( "el peso total del paquete es: " + str(peso_total)+"gramos")
