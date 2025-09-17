
#1 esercizio
# 1 - Write a Python script to concatenate the following list of dictionaries 
# to create a new dictionary.
lista_diz =[{1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60},
            {7:10, 8:20}, {9:30, 10:40}, {11:50, 12:60},
            {13:10, 14:20}]

dict_concatenazione = {}

for diz in lista_diz:
    dict_concatenazione.update(diz)
    
print(dict_concatenazione)
#-------------------------------------------------
#2 esercizio
# 2 - Write a Python script to generate and print a dictionary that contains 
# a number (between 1 and n) in the form (x, x*x).
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dict_elevato = {}

for i in range(1, 11):
    dict_elevato[i] = i ** 2

print(dict_elevato)

#3 esercizio
# 3 - In una lista trovare 2 numeri che sommati danno un numero target
nums = [3, 2, 4, 3]
target = 6

lista_risultati = [] 

for a in range(len(nums)):
    for b in range(len(nums)):
        if nums[a] + nums[b] == target:
            print( "Numeri: " ,nums[a], nums[b])
            lista_risultati.append((nums[a], nums[b]))
            

print("Risultati: ", lista_risultati)
#metodo while 

"""
i = 0 
while i < len(nums):
    j = i + 1
    while j < len(nums):
        if nums[i] + nums[j] == target:
            print( "Numeri: " ,nums[i], nums[j])
            j += 1
            break
    i += 1

"""