# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

def concatenar_dados(dado1, dado2):
    """
    Concatena dois dados em uma única string.
    
    :param dado1: Primeiro dado a ser concatenado
    :param dado2: Segundo dado a ser concatenado
    :return: String resultante da concatenação dos dois dados
    """
    return f"{dado1}{dado2}"

def main():
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    resultado = concatenar_dados(dado1, dado2)
    print(f"Resultado da concatenação: {resultado}")

if __name__ == "__main__":
    main()