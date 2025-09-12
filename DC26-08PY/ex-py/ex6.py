# Programa que analisa a ocorrência de uma letra em uma frase

# Lê a frase digitada pelo usuário
frase = input("Digite uma frase: ").strip()

# Lê a letra que o usuário deseja procurar
letra = input("Digite a letra que deseja procurar: ").strip().lower()

# Coloca a frase toda em minúsculo para evitar problemas com maiúsculas/minúsculas
frase_minuscula = frase.lower()

# Conta quantas vezes a letra aparece
quantidade = frase_minuscula.count(letra)

# Mostra os resultados
if quantidade > 0:
    print(f"A letra '{letra}' aparece {quantidade} vez(es) na frase.")
    print(f"A primeira vez que aparece é na posição: {frase_minuscula.find(letra) + 1}")
    print(f"A última vez que aparece é na posição: {frase_minuscula.rfind(letra) + 1}")
else:
    print(f"A letra '{letra}' não foi encontrada na frase.")
