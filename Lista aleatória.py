import random

lista =[]

for element in range(30):
   indice = random.randrange(1,501)
   lista.append(indice)
   
print(lista)

maior = 0
pares = []
for item in lista:
   if item>maior:
      maior = item
   if item%2 == 0:
     pares.append(item)

print("O maior item da lista é", maior)
print("A lista possui ", len(pares), " números pares.")



