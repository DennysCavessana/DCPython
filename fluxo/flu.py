import random



print("\n\n",90*"=")
print("Programa para gerar 5 números aleatorios e mostrar o maior e o menor ")
print(90*"=","\n\n")

numeros=[]

for c in range(5):   #Pede 5 números aleatórios de 1 a 100
    numeros.append(random.randint(1,100))

lista=numeros
b=numeros[0]
a=numeros[0]


print("\n Os números gerados foram \n")

for v in lista: # remover os colchetes e as vírgulas da lista 
    print(f"{v}  ", end='')




for n in lista:  #loop para colocar o Maior na variável B e o Menor na variável A
    if n> b:
        b = n

    if n < a:
        a = n


print("\n", 90*"=","\n")

print (f"O maior número da lista é -> {b}")
print(f"O menor número da lista é -> {a}")

print("\n", 90*"=","\n")