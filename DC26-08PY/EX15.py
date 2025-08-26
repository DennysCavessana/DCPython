#O Professor quer sortear a ordem de apresentação de trabalho dos alunos ,faça um programa que le o nome de 4 alunos e mostre a ordem de cada um
import random
Lis = ["Dennys","Fernando","Julia","Kauê"]
print(random.choices(Lis , k = 4))