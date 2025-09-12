# Programa para calcular salário com bônus e valor por filhos

# Lê o salário do funcionário
salario = float(input("Digite o salário do funcionário: R$ "))

# Pergunta se ele tem filhos
tem_filhos = input("O funcionário tem filhos? (s/n): ").strip().lower()

# Inicializa valor total do bônus
bonus = 0

# Verifica se salário é menor que R$2000
if salario < 2000:
    bonus += 151  # adiciona bônus de 151

# Se tiver filhos, pergunta quantos e adiciona R$200 por filho
if tem_filhos == "s":
    quantidade_filhos = int(input("Quantos filhos o funcionário tem? "))
    bonus += quantidade_filhos * 200

# Calcula o salário final
salario_final = salario + bonus

# Mostra o resultado
print(f"Salário original: R${salario:.2f}")
print(f"Total de bônus e valores por filhos: R${bonus:.2f}")
print(f"Salário final: R${salario_final:.2f}")
