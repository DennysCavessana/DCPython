#faça um programa que leai o comprimento do cateto aposto e do adjacente de um triangulo retângulo, calcule e mostre o comprimento hipotenusa.
import math

# Entrada dos catetos
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Cálculo da hipotenusa usando o Teorema de Pitágoras
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

# Exibição do resultado
print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")
