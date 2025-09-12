# Programa para calcular o IMC e mostrar a classificação

# Pede os dados do usuário
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Mostra o valor do IMC
print(f"Seu IMC é: {imc:.2f}")

# Verifica a classificação de acordo com o valor do IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso ideal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 40:
    print("Classificação: Obesidade")
else:
    print("Classificação: Obesidade Mórbida")
