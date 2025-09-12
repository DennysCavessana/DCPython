# Programa para verificar se três retas podem formar um triângulo

# Lê os comprimentos das retas
reta1 = float(input("Digite a medida da primeira reta: "))
reta2 = float(input("Digite a medida da segunda reta: "))
reta3 = float(input("Digite a medida da terceira reta: "))

# Verifica a condição para formar um triângulo
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("✅ As retas podem formar um triângulo!")
else:
    print("❌ As retas NÃO podem formar um triângulo.")
