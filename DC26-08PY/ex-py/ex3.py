# Programa que verifica se o nome de uma cidade começa com "Santo"

# Lê o nome da cidade digitado pelo usuário
cidade = input("Digite o nome de uma cidade: ").strip()  # strip remove espaços extras no início e no fim

# Verifica se os primeiros 5 caracteres são "Santo"
# .lower() deixa tudo minúsculo para evitar erro de maiúscula/minúscula
if cidade.lower().startswith("santo"):
    print("Sim! A cidade começa com 'Santo'.")
else:
    print("Não! A cidade não começa com 'Santo'.")
