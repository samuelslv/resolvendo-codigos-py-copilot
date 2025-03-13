# Vamos testar se uma palavra é um palíndromo?!
# Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

def palindromo(palavra):
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        return "É um palíndromo!"
    else:
        return "Não é um palíndromo!"

def main():
    palavra = input("Digite a palavra: ")
    resultado = palindromo(palavra)
    print(f"Resultado da verificação: {resultado}")

if __name__ == "__main__":
    main()