#Crie um programa que lê um número descimal e mostre a sua porção enteira -> Digite 5,55 -> sai 5

import math
Nu = float(input("Digite o seu número ----->>"))
Nu = math.trunc(Nu) 
print(Nu)