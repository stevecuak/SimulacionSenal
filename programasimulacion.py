puntos = int(input("Cuantos saltos?")) #pregunta el numero de saltos
potensia = 55 #potencia de la señal transmitida
potenciaT = potensia
counter = 1
miku = True 
print("Distancia -- Potencia")
print("0m --------- 55")
while(miku) :
    potensia = potensia*0.90 #Reduce la potencia al 90% de la misma
    texto = f"{counter}m --------- {round(potensia,2)}"
    if (counter >=10): #Elimina un caractér para mantener las columnas alineadas
        texto = texto[:5] + texto[5+1:]
    print(texto) #Imprime los calculos
    if (counter == puntos): #Revisa si el contador llego a los saltos indicados
        miku = False
    if (counter < puntos): #Agrega al contador antes de repetir el ciclo
        counter +=1

salida = f"La potencia final con {puntos} saltos a 1m de distancia es: {round(potensia,2)}, inicio con {potenciaT} mW."
print(salida) #Imprime la potencia final.
