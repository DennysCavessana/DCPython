'''pessoa = [[ "joão", 10], ["Pedro" , 15],["José", 18]]
print(pessoa)
print(pessoa[0][0])
print(pessoa[1][1])
print(pessoa[2])

teste=list()
teste.append('Lindolfo')
teste.append(43)
galera=list()
galera.append(teste[:])
print(teste)
print(galera)


teste[0]='maria'
teste[1]= 22
galera=list()
galera.append(teste[:])
print(teste)
print(galera)

turma=[['Ana',15],['João',20],['Raul',44]]
for p in turma:
    print(f"{p[0]} Tem {p[1]} anos de idade!")'''

turma2=list()
dados=list()
totmaior=totmenor=0

for c in range(0,6):
    dados.append(str(input("Nome.")).upper().strip())
    dados.append(int(input("idade.")))
    turma2.append(dados[:])
    dados.clear()
print(turma2) 
   
for p in turma2:
    if p[1]>=18:
        print(f'{p[0]} é maior de idade, ele tem {p[1]} anos de idade')
        totmaior+=1
    else:
        print(f'{p[0]} É menor de idade, ele tem {p[1]} anos de idade')
        totmenor+=1   
print("Temos {totmaior} maiores de idade e {totmenor} menores de idade!!")
