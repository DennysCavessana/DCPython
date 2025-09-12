# Pede ao usuário para digitar o nome completo
nome = input("Digite seu nome completo: ")

# Mostra o nome em letras maiúsculas
print("Nome em maiúsculas:", nome.upper())

# Mostra o nome em letras minúsculas
print("Nome em minúsculas:", nome.lower())

# Conta quantas letras o nome tem (desconsiderando espaços)
quantidade_letras = len(nome.replace(" ", ""))  # remove espaços antes de contar
print("Quantidade de letras do nome:", quantidade_letras)

# Divide o nome em partes (palavras) para pegar o primeiro nome
partes_nome = nome.split()
primeiro_nome = partes_nome[0]  # pega a primeira palavra do nome
print("Quantidade de letras do primeiro nome:", len(primeiro_nome))