# Programa que lê um número entre 0 e 9999 e mostra cada dígito separado

# Lê o número digitado pelo usuário
numero = int(input("Digite um número entre 0 e 9999: "))

# Garante que o número esteja dentro do intervalo permitido
if 0 <= numero <= 9999:
    # Usando operações matemáticas (divisão inteira e módulo)
    unidade = numero % 10                # pega o último dígito
    dezena = (numero // 10) % 10         # pega o penúltimo dígito
    centena = (numero // 100) % 10       # pega o antepenúltimo dígito
    milhar = (numero // 1000) % 10       # pega o primeiro dígito (se houver)

    # Mostra os resultados
    print("Unidade:", unidade)
    print("Dezena :", dezena)
    print("Centena:", centena)
    print("Milhar :", milhar)

else:
    print("Número inválido! Digite entre 0 e 9999.")
