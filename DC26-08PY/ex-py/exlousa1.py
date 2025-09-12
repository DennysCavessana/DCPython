import random

print("==== JOGO DA ADIVINHAÇÃO ====")
print("Tente adivinhar o número que o computador está pensando!")

# Computador escolhe um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

tentativas = 0

while True:
    # Usuário faz um palpite
    palpite = int(input("Digite um número entre 1 e 10: "))
    tentativas += 1
    
    if palpite == numero_secreto:
        print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s).")
        break
    elif palpite < numero_secreto:
        print("🔼 O número é maior! Tente novamente.")
    else:
        print("🔽 O número é menor! Tente novamente.")
