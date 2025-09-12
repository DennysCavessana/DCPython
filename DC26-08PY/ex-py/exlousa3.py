# Programa para calcular velocidade média e multa

# Lê os dados do usuário
km_saida = float(input("Digite a quilometragem de saída do veículo: "))
km_chegada = float(input("Digite a quilometragem de chegada do veículo: "))

hora_saida = float(input("Digite a hora de saída (formato 24h, ex: 14.5 = 14h30): "))
hora_chegada = float(input("Digite a hora de chegada (formato 24h, ex: 16.25 = 16h15): "))

# Calcula a distância percorrida
distancia = km_chegada - km_saida

# Calcula o tempo gasto
tempo = hora_chegada - hora_saida

# Evita divisão por zero
if tempo <= 0:
    print("Erro: hora de chegada deve ser maior que a hora de saída.")
else:
    # Calcula a velocidade média
    velocidade_media = distancia / tempo
    print(f"Velocidade média: {velocidade_media:.2f} km/h")

    # Verifica se excedeu 80 km/h
    if velocidade_media > 80:
        excesso = velocidade_media - 80
        multa = excesso * 5  # R$5 por km acima do limite
        print(f"Atenção! Velocidade acima do limite. Multa: R${multa:.2f}")
    else:
        print("Velocidade dentro do limite. Sem multa.")
