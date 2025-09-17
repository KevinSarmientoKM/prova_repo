# Scriviamo un programma che calcoli il prezzo di un biglietto per il cinema
# Chiediamo all'utente la sua età, il comune di residenza e il lavoro svolto
# Se l'utente è residente a Como, il prezzo del biglietto è 0
# Se l'utente è minorenne il prezzo del biglietto viene scontato di 3€
# Se l'utente ha più di 70 anni, il prezzo del biglietto viene scontato di 5€
# Se l'utente è uno studente o un docente, il biglietto viene scontato di altri 2€
# Di base, il biglietto costa 10€






#print("Benvenuto nel portale di acquisto biglietto di COMO_Cinema!")
#eta = int(input("Inserisci la tua età: "))
#comune = input("Inserisci il tuo comune di residenza: ").casefold()
#lavoro = input("Inserisci il tuo lavoro: ").casefold()
#correzione dell esercizio 
# if eta < 18:
    #prezzo -= 3
# if eta > 70:    
#prezzo -= 5
# if lavoro == "studente" or lavoro == "docente":
#    prezzo -= 2
# if comune == "como":
#    prezzo = 0 (lo azzeriamo) oppure | prezzo -= prezzo  10

#print(f"Il prezzo del biglietto è: {prezzo}€")




prezzo = 10
comune = input("In quale comiune abiti? ").casefold()

if comune == "como":
    prezzo -= prezzo
else:
    eta = int(input("Inserisci la tua età: "))
    if eta < 18:
        prezzo -= 3
    elif eta > 70:
        prezzo -= 5
    #poniamo il lavoro come controllo per un ulteriose sconto nel caso esce studente o docente 
    lavoro = input("Inserisci il tuo lavoro: ").casefold()
    if lavoro == "studente" or lavoro == "docente":
        prezzo -= 2

    else:
        print("eta non conforme ")
        prezzo = "NON VALIDO!"
#-------------------------------------

print(f"Il prezzo del biglietto è: {prezzo}€")