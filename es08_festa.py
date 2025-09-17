'''
Scrivi un programma per organizzare una festa di compleanno che permetta di gestire 
la raccolta fondi per un regalo. Il programma deve:

Chiedere all'utente quanti saranno gli invitati alla festa.

Per ogni invitato: 
- Chiedere il nome.
- Chiedere quanto vuole contribuire al regalo.

Calcolare il totale del budget raccolto.

Mostrare un riepilogo con: 
- La lista degli invitati.
- I contributi individuali.
- Il budget totale disponibile per il regalo.
'''

#creiamo una lista vuota per i nomi degli invitati

n_invitati = int(input("Inserisci il numero di invitati :  ").strip())

lista_nomi = [] #creiamo iuna lista vuota per i nomi degli invitati
lista_contributi = [] #creiamo una lista vuota per i contributi degli invitati
budget_totale = 0 #creiamo una variabile per il budget totale
#creiamo un for range per gli invitati 

for n in range(n_invitati):
#potevamo anche introdure una specie di contatore scrvendo print("Invitato n°", n+1) partendo da 1 e non da 0
#chiediamo il nome dell'invitato
    nome = input("Nome dell'invitato: ").strip().capitalize()
    contributo = float(input("Quanto vuoi contribuire al regalo: ").strip()) #mettiamo float() per la gestione dei decimali
    lista_nomi.append(nome) #aggiungiamo il nome all'interno della lista
    lista_contributi.append(contributo) #aggiungiamo il contributo all'interno della lista
    budget_totale = budget_totale + contributo #aggiungiamo il contributo al budget totale 
    #budget_totale = contributo #aggiungiamo il contributo al budget totale  
    #oppure scrivo cosi budget_totale += contributo

#budget_totale = sum(lista_contributi) #calcoliamo il budget totale sommando gli elementi della lista 
#sum() funzione per calcolare la somma diretta della lista

#creiamo un metodo alternativo per il calcolo del budget totale inserendo nel for  (riga76) e stampare in riga(53)

#creiamo un ciclo for per stampare i contributi e nomi degli invitati08
for i in range(len(n_invitati)):
    #creiamo un cassetto dove inserimo i valore i-esimo delle liste indicate  | _o sta per output
    nome_o = lista_nomi[i]
    contributo_o = lista_contributi[i]
    print("Invitato:", nome_o,  "| contribuisce:", contributo_o, "euro")

print("Budget totale:", budget_totale, "euro") 
#creiamo un print per mostrare il budget totale alla fine

