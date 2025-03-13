#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.
#Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

def ver_impar_par(numero):
    """
    Verifica se um número é par ou ímpar.
    
    :param numero: Número a ser verificado
    :return: String indicando se o número é par ou ímpar
    """
    if numero % 2 == 0:
        return f"O número {numero} é par!"
    else:
        return f"O número {numero} é ímpar!"

def main():
    num = int(input("Digite o numero: "))
    resultado = ver_impar_par(num);
    print(f"Resultado da verificação: {resultado}")

if __name__ == "__main__":
    main()