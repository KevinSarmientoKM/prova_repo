nome = "Mario"
cognome = "Rossi" 
anno_di_nascita = 2013 
citta= "Roma"
eta = 2025 - anno_di_nascita # calcolo eta
#-----------------------------
#1modo
Documento = ("Nominativo: " + nome + " " +  cognome  + "\ncitta: " + citta + "\nAnno di nascita : " + str(anno_di_nascita) + "\nEta: " + str(eta))
print(Documento)

#-----------------------------
#2 modo
print("Nominativo", nome, cognome, "\nAnno di nascita:", str(anno_di_nascita), "\nCitta:", citta, "\nEta:", str(eta))


#------------------------------------
#3 modo
print("Nominativo:  {}\nAnno di nascita: {}\nCitta: {}\nEta".format(nome +" "+ cognome, anno_di_nascita, citta, eta))



#-----------------------------
#4 modo con multiriga
Documento = (f"""Nominativo: {nome}  {cognome}
Anno di nascita: {anno_di_nascita}
Citta: {citta}
Eta: {eta}""")
print(Documento)
