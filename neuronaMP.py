#Programa que calcula la neurona MP
#Entradas: Número de entradas, umbral de activación, valores de las entradas, pesos de las entradas, si las entradas son inhibidoras o no
#Salidas: Suma ponderada, si la neurona está activada o no


print("Programa que calcula la neurona MP")
num_entradas = int(input("Ingrese el número de entradas: "))
umbral = float(input("Ingrese el umbral de activación: "))

entradas = []
inhibidores = []

# Recoger las entradas e indicar si son inhibidores
for i in range(num_entradas):
    valor = int(input(f"Ingrese el valor de la entrada {i + 1}: "))
    inhibidor = input(f"La entrada {i + 1} es un inhibidor? (s/n): ").lower() == 's'
    if inhibidor and valor == 1:
        print("Se detectó una entrada inhibidora activa. Finalizando el programa.")
        exit()  # Finaliza el programa si una entrada inhibidora es activa
    entradas.append(valor)
    inhibidores.append(inhibidor)
    print(f"Estado actual de las entradas: {entradas}")  # Muestra el array de entradas actualizado

# Calculo de la suma ponderada
suma_ponderada = 0
for valor, inhibidor in zip(entradas, inhibidores):
    if not inhibidor:
        suma_ponderada += valor  # Suma el valor de las entradas no inhibidoras

# Determinación de la salida de la neurona
activacion = 1 if suma_ponderada >= umbral else 0

print(f"Suma ponderada: {suma_ponderada}")
print(f"Neurona activada: {'Sí' if activacion == 1 else 'No'}")

#Continuar con la parte de agregar peso a los valores de las entradas


    