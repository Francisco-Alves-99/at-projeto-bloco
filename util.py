def input_numero(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
