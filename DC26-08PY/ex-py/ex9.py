import random

print("==== Jogo do PAR ou ÍMPAR ====")

# Loop para o jogo continuar até o jogador perder
while True:
    # Usuário escolhe um número
    jogador_num = int(input("Digite um número: "))
    
    # Usuário escolhe Par ou Ímpar
    jogador_escolha = input("Você escolhe PAR ou ÍMPAR? ").strip().lower()
    
    # Computador escolhe um número aleatório entre 0 e 10
    computador_num = random.randint(0, 10)
    
    # Soma dos números
    total = jogador_num + computador_num
    
    # Mostra os números escolhidos
    print(f"Você jogou {jogador_num} e o computador {computador_num}. Total = {total}")
    
    # Verifica se o total é par ou ímpar
    if total % 2 == 0:
        resultado = "par"
    else:
        resultado = "ímpar"
    
    print(f"Resultado: {resultado.upper()}")
    
    # Confere se o jogador venceu
    if jogador_escolha == resultado:
        print("🎉 Você venceu! Vamos jogar de novo...\n")
    else:
        print("😢 Você perdeu! Fim de jogo.")
        break
