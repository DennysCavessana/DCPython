# Programa que verifica se um número é par ou ímpar

# Lê o número do usuário
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar usando o operador módulo (%)
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
