lista_numeri = [5, 9, 25, 33, 114]
# calcolare e stampare la somma dei numeri contenuti nella lista

# creare una nuova lista che contiene i quadrati dei numeri della lista di partenza

# creare una nuova lista che contiene solo i nomi che iniziano con la lettera g

# creare una nuova lista che contiene solo i nomi che come seconda lettera hanno una vocale

#esercizio 1
for somma in lista_numeri:
    somma = sum(lista_numeri)
    print(somma)
""""
usando la funzione .sum() per calcolare la somma dei numeri
facendo semplicemente cosi 
print(sum(lista_numeri))
"""

#esercizio 2 
lista_num_2= []
for numero in lista_numeri:
    lista_num_2.append(numero ** 2)
    
print(lista_num_2)

#esercizio 3

lista_nomi = ["Giorgio", "Federico", "Jhon", "Giovanni", "Anna"]
lista_nomi_g = []
for nome in lista_nomi:
        if nome[0].casefold() == "g":
            lista_nomi_g.append(nome)
            print(lista_nomi_g)
"""
for nome in lista_nomi:
    if nome.startswith("G"):
        lista_nomi.append(nome)
        print(lista_nomi)
"""


#esercizio 4
lista_nomi = ["Giorgio", "Federico", "Jhon", "Giovanni", "Anna"]
vocali = ["a", "e", "i", "o", "u"]
lista_v = [] #creiamo la listaq vuota per l inserimento con apppend()
for nome in lista_nomi:
    if nome[1].casefold() in vocali:
        lista_v.append(nome)
        print(lista_v)

#------------------------------------------
#esercizio 5

lista_numeri = [5,9,25,33,114,345,546,789,1089,6543,123,987,600]
numero_p = []
for numero in lista_numeri:
    if numero % 2 == 0:
        numero_p.append(numero)
        #print(numero_p) se lo scrivo qua ripete il ciclo stampandolo numero per numero

print(numero_p) #miglior soluzione con una sola stampa finale

#--------------------------------------------
#stampa le parole solo se hanno 5 lettere usando il for 
lista_parole = ["cane" ,"gatto", "gnu","tigre","orso","elefante","giraffe","ratto","elephant"]

parola_5 = []

for parola in lista_parole:
    if len(parola) == 5:
        parola_5.append(parola)       
print(parola_5)


"""
oppure scritto cosi 
for parola in lista_parole:
    if parola (parola) == 5:
        print(parola)
"""