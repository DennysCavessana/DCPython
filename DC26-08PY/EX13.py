#faça um programa que leia um angulo qualquer e mostre na tela o seu seno cosceno e tangente desse ângulo
import math

# Entrada do ângulo em graus
angulo_graus = float(input("Digite o ângulo em graus: "))

# Conversão para radianos (necessária para as funções trigonométricas do módulo math)
angulo_radianos = math.radians(angulo_graus)

# Cálculo das funções trigonométricas
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Exibição dos resultados
print(f"Seno de {angulo_graus}°: {seno:.4f}")
print(f"Cosseno de {angulo_graus}°: {cosseno:.4f}")
print(f"Tangente de {angulo_graus}°: {tangente:.4f}")