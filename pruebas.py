lista = [1, 2, 3, 4]
listaMod=[]
contador = 0

print(lista)

fijos = lista.count(4)
contador += fijos
#lista = [x for x in lista if x != 4]  
for i in range(len(lista)):
    print (i)
    if lista[i]==4:
        lista.remove(lista[i])

print(lista)

