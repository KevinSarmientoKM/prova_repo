'''
creare un file e inserire 15 animali
animale1
animale2
.
.
.

stampare gli animali incolonnati nell'ordine in cui sono scritti
output:
    animale1
    animale2
stampare gli animali incolonnati nell'ordine dall'ultimo al primo
output: 
    animale2
    animale1
stampare gli animali sulla stessa riga separati da virgole
output:
    animale1, animale2, ecc
'''
# #stampare gli animali incolonnati nell'ordine in cui sono scritti
# output:
#     animale1
#     animale2

with open("./file/es12_file_animali.txt" , "r") as file:
    animali = file.readlines()
    diz_animali ={}
    for lista in range(len(animali)):
        diz_animali[lista] = {"animale": animali[lista].strip()}
        print(diz_animali[lista]["animale"])

    """ metodo alternativo !!!
    with open("./file/file_animali.txt" , "r") as file:
        for animale in animali :
            if animale == animali[0]
                file.write(animale)
            else:
                file.write("\n" + animale)
                """

print("-" * 50)
# stampare gli animali incolonnati nell'ordine dall'ultimo al primo
# output: 
#     animale2
#     animale1

with open("./file/es12_file_animali.txt", "r") as file:
    animali = file.readlines()
    diz_animali_rovescio = {}
    animali = [a.strip() for a in animali]  #rimuovo le \n
    for i, nome in enumerate(reversed(animali)):
        diz_animali_rovescio[i] = {"animale": nome}
        print(nome)

# with open("./file/file_animali.txt") as file:
#     animali = file.readlines()
#     lista_contrario = "".join(animali[::-1])
#     print(lista_contrario)
"""
metodo alternativo 
with open("./file/es12_file_animali.txt", "r") as file:
lista = file.read().splitlines()
for el in lista:
print(el)

oppure con reverse()
for i in reversed(lista):
    print(i)
"""
print("-" * 50)

# stampare gli animali sulla stessa riga separati da virgole
# output:
#     animale1, animale2, ecc
with open("./file/es12_file_animali.txt", "r") as file:
    animali = file.readlines()
    diz_animali_conc = {}
    for lista in range(len(animali)):
        diz_animali_conc[lista] = {"animali": animali[lista].strip()}
        print(diz_animali_conc[lista]["animali"], end="|")


# with open("./file/es12_file_animali.txt", "r") as file:
#     animali = [riga.strip() for riga in file]
#     stringa = ""
#     for animale in animali:
#         stringa += animale + " "

#     print(stringa.strip()) 

""" 
metodo alternativo 
print(*lista , sep="")
nb= lo rende piu pulito !!"""


