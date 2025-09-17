'''
Calcolare il valore della rata di una casa sapendo che
la casa ha 3 stanze:
    salotto: quadrato
    camera da letto: rettangolare
    bagno: quadrato
Il valore totale del mutuo è dato dal valore al metro quadro per il numero di metri quadrati.
Una volta trovato il mutuo totale, dividerlo per il numero delle rate in cui si vuole 
suddividere il costo.
Il programma richiede all'utente nome, cognome, anno di nascita e in quante rate vuole dividere
il mutuo, dimensioni stanze
Stampare una scheda che riporti
Nomitativo: [nome] [cognome] - [eta]
Metri casa: [metriquadrati] m - Costo metro quadro: [costometroquadro] €
Valore Mutuo: [valore mutuo] € - Numero rate: [numerorate] - Importo singola rata: [rata] €
'''
#--------------inserimento dati personali --------
nome = input("inserisci il tuo nome: ")
cognome = input("inserisci il tuo cognome: ")
anno_nascita = int(input("inserisci l'anno di nascita: "))
eta = 2025 - anno_nascita


print(f"""Nominativo : {nome} 
Cognome : {cognome} 
Eta :{eta} anni""")
#--------------inserimento dati casa -----------
salotto_lato = float(input("inserisci il lato del salotto: "))
salotto_metro = salotto_lato **2

camera_base = float(input("inserisci il lato della camera: "))
camera_altezza = float(input("inserisci l'altezza della camera: "))
camera_metro = camera_base * camera_altezza

bagno_lato = float(input("inserisci il lato del bagno: "))
bagno_metro = bagno_lato **2

metro_quadrototale = salotto_metro + camera_metro + bagno_metro

print(f"""Salone : {salotto_metro}
Camera : {camera_metro}
Bagno : {bagno_metro}
metro quadrati totali : {metro_quadrototale} m²
""")
#--------------inserimento dati mutuo -----------

mutuo = float(input("inserisci il valore del mutuo: "))
costo_metro_quadro = float(input("inserisci il costo al metro quadro: "))   

numero_rate = int(input("inserisci il numero di rate: "))
rata = round(mutuo  / numero_rate,2)

print(f"""Metri casa : {metro_quadrototale} m²  
Costo metro quadro: {costo_metro_quadro} € 
""")

print(f"""Valore Mutuo: {mutuo} €
Numero rate: {numero_rate}
Importo singola rata: {rata} €""")



