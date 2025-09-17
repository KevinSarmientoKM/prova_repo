# ESERCIZIO 2
# Calcolare perimetro e area di un rettangolo
# base e altezza saranno due variabili
# il valore delle variabili potete sceglierlo voi
# Stampare in output:

# Base: [base] cm 
# Altezza: [altezza] cm 
# Area: [area] cm2 
# Perimetro: [perimetro] cm

# ripetere per quadrato e cerchio

# EXTRA: usare modulo math per pi-greco 

import math

#rettangolo
base = 10
altezza = 5

#calcolo area  rettangolo  
area_ret = base * altezza

#stampa area
print("area rettangolo = ", area_ret) #esce 50 (il risultato della moltiplicazione)

#calcolo perimetro rettangolo
perimetro_ret = 2 * (base + altezza)

#stampa perimetro
print("perimetro rettangolo = ", perimetro_ret) #esce 30
print ("-" * 50 ) #stampa una linea di separazione nel terminal

Rettangolo = (f"""
Base: {base} cm
Altezza: {altezza} cm
area: {area_ret} cm
Perimetro: {perimetro_ret} cm""")
print(Rettangolo)
print("-" * 50 ) #stampa una linea di separazione nel terminal
#quadrato
lato = 5

#calcolo area
area_quad = lato ** 2

#stampa area
print("area quadrato = ", area_quad) #esce 25 (il risultato della potenza)

#calcolo perimetro
perimetro_quad = 4 * lato

#stampa perimetro
print("perimetro quadrato = ", perimetro_quad) #esce 20 (il risultato della moltiplicazione)

print ("-" * 50 ) #stampa una linea di separazione nel terminal

Quadrato = (f"""
Lato: {lato} cm
area: {area_quad} cm
Perimetro: {perimetro_quad} cm""")
print(Quadrato)
print ("-" * 50 ) #stampa una linea di separazione nel terminal
#cerchio 
raggio = 5

#calcolo area cerchio

raggio = 10
area_cer = math.pi * raggio**2
print("Area =", area_cer)
#stampa area
print("area cerchio = ", area_cer) #esce 78.5 (il risultato della moltiplicazione)

#diametro
diametro = 2 * raggio

#stampa diametro
print("diametro cerchio = ", diametro) #esce 10 (il risultato della moltiplicazione)
print("-" * 50)

Cerchio = (f"""
Raggio: {raggio} cm
Diametro: {diametro} cm
area: {round(area_cer , 2)} cm 
Diametro: {diametro} cm""")
print(Cerchio)
#area: {round(area)} cm per ottenere un valore intero 
print ("-" * 50 ) #stampa una linea di separazione nel terminal