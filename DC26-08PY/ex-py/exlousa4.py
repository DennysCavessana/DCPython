# Programa para verificar se um ano é bissexto

# Lê o ano do usuário
ano = int(input("Digite um ano: "))

# Verifica as regras do ano bissexto:
# - Divisível por 4 e não por 100, ou divisível por 400
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto.")
