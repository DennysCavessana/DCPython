# Programa que verifica se o nome da pessoa contém "Silva"

# Lê o nome completo da pessoa
nome = input("Digite seu nome completo: ").strip()

# Verifica se existe "silva" no nome (ignora maiúsculas/minúsculas)
if "silva" in nome.lower():
    print("Sim! O nome contém 'Silva'.")
else:
    print("Não! O nome não contém 'Silva'.")
