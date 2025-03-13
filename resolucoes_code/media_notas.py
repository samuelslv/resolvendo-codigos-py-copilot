#Agora vamos calcular a média de três notas fornecidas na entrada do usuário.
#Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

def media_notas(nota1, nota2, nota3):
    """
    Calcula a média de três notas.
    
    :param nota1: Primeira nota
    :param nota2: Segunda nota
    :param nota3: Terceira nota
    :return: Média das três notas
    """

    return (nota1 + nota2 + nota3) / 3

def main():
    nota1 = int(input("Digite a nota 1: "))
    nota2 = int(input("Digite a nota 2: "))
    nota3 = int(input("Digite a nota 3: "))
    resultado = media_notas(nota1, nota2, nota3);
    print(f"Resultado da media das notas: {resultado}")

if __name__ == "__main__":
    main()