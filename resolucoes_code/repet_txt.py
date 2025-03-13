# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

def repeat(text, N):
    """
    Repete uma string N vezes.
    
    :param text: String a ser repetida
    :param N: Número de repetições
    :return: String resultante da repetição
    """
    for i in range(N):
        print(str(i+1) + " - " + text)
    #return text*N

def main():
    text = input("Digite a palavra: ")
    quant = int(input("Digite a quantidade de vezes pra repetir a palavra: "))
    repeat(text, quant)
    #resultado = repeat(text, quant)
    #print(f"Resultado da repetição: {resultado}")"""

if __name__ == "__main__":
    main()