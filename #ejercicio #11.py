#ejercicio #11
precio_normal= 3.49

num_barras_no_frescas = int(input("ingresa el numero de barras vendidas que no son del dia: "))

descuento = 0.6  # 60% de descuento

precio_final = precio_normal * (1 - descuento)
total_no_frescas = num_barras_no_frescas * precio_final

print ("precio normal de una barra de pan: $" + str(precio_normal) )
print("descuento por no ser fresca; " + str(int(descuento * 100)) + "%")
print("precio final de las barras no frescas: $" + str(round(precio_final,2)))
print("coste final total: $" + str(round(total_no_frescas, 2)))