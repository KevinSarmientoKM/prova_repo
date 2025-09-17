#domanda 11 (metti in ordine crescente gli elementi )
class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

# Creazione degli oggetti Persona
a = Persona("Walter", "White", 51)
b = Persona("Robin", "Nico", 30)
c = Persona("Tony", "Soprano", 48)
d = Persona("Sansa", "Stark", 18)

lista_persone = [a, b, c, d]

lista_ordinata = sorted(lista_persone, key=lambda persona: persona.eta)

for persona in lista_ordinata:
    print(f"{persona.nome} {persona.cognome}, {persona.eta} anni")





#domanda 28 concatenazione dei dizionari 

nomi = ["Luca", "Paolo", "Simone"]
indirizzi = ["Via Roma, 1", "Via Milano, 2", "Via Torino, 3"]

# Dictionary comprehension
rubrica = {nomi[i]: indirizzi[i] for i in range(len(nomi))}

print(rubrica)


#domanda 29 slicing
frase = "The Dark Knight Rises"


parte1 = frase[:15]  
print(parte1)  # Output: "The Dark Knight"

parte2 = frase[16:] 
print(parte2)  # Output: "Rises"


parte3 = frase[4:15]  
print(parte3)  # Output: "Dark Knight"


#domanda 30 creazione classe SerieTV
class SerieTV:
    def __init__(self, titolo, durata_media_episodio, numero_episodi_per_stagione, numero_di_stagioni, genere, anno_di_inizio_delle_riprese):
        self.titolo = titolo
        self.durata_media_episodio = durata_media_episodio  
        self.numero_episodi_per_stagione = numero_episodi_per_stagione
        self.numero_di_stagioni = numero_di_stagioni
        self.genere = genere
        self.anno_di_inizio_delle_riprese = anno_di_inizio_delle_riprese

    def __str__(self):
        return (f"Serie TV: {self.titolo}\n"
                f"Genere: {self.genere}\n"
                f"Anno di inizio riprese: {self.anno_di_inizio_delle_riprese}\n"
                f"Stagioni: {self.numero_di_stagioni}\n"
                f"Episodi per stagione: {self.numero_episodi_per_stagione}\n"
                f"Durata media episodio: {self.durata_media_episodio} minuti")

    def durata_della_serie(self):
        totale_minuti = (self.durata_media_episodio * 
                         self.numero_episodi_per_stagione * 
                         self.numero_di_stagioni)
        ore = totale_minuti // 60
        minuti = totale_minuti % 60
        return f"Durata totale della serie: {ore} ore e {minuti} minuti"


SwordArtOnline = SerieTV(
    titolo="Sword Art Online",
    durata_media_episodio=24,
    numero_episodi_per_stagione=15,
    numero_di_stagioni=5,
    genere="Anime",
    anno_di_inizio_delle_riprese=2012
)


print(SwordArtOnline)  
print(SwordArtOnline.durata_della_serie())




a = [3, 1, 5, 2, 4]
b = 0
while b < len(a):
    c = a[b]
    d = b + 1
    while d < len(a):
        c = c + a[d]  # Somma gli elementi successivi ad a[b]
        d = d + 1
    print(c)  # Stampa il risultato parziale
    b = b + 1  # Incrementa b per passare al prossimo elemento