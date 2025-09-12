import random

print("==== JOKENPÔ ====")
print("Opções: Pedra, Papel ou Tesoura")

# Lista com as opções possíveis
opcoes = ["pedra", "papel", "tesoura"]

while True:
    # Jogador escolhe
    jogador = input("Digite sua escolha: ").strip().lower()
    
    # Verifica se a escolha é válida
    if jogador not in opcoes:
        print("Opção inválida! Tente novamente.")
        continue
    
    # Computador escolhe aleatoriamente
    computador = random.choice(opcoes)
    
    print(f"Você escolheu: {jogador.capitalize()}")
    print(f"O computador escolheu: {computador.capitalize()}")
    
    # Verifica o resultado
    if jogador == computador:
        print("🔄 Empate!\n")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        print("🎉 Você venceu!\n")
    else:
        print("😢 Você perdeu!\n")
    
    # Pergunta se o jogador quer continuar
    continuar = input("Deseja jogar novamente? (s/n): ").strip().lower()
    if continuar != "s":
        print("👋 Obrigado por jogar!")
        break
