# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def soma(dado1, dado2):
    """
    Relizar uma operação de soma entre dois dados.
    """
    return dado1 + dado2

def subt(dado1, dado2):
    """
    Relizar uma operação de subtração entre dois dados.
    """
    return dado1 - dado2

def divi(dado1, dado2):
    """
    Relizar uma operação de divisão entre dois dados.
    """
    return dado1 / dado2

def multi(dado1, dado2):
    """
    Relizar uma operação de multiplicação entre dois dados.
    """
    return dado1 * dado2

def main():
    num1 = int(input("Digite o primeiro dado: "))
    num2 = int(input("Digite o segundo dado: "))
    sum = soma(num1, num2)
    sub = subt(num1, num2)
    mult = multi(num1, num2)
    div = divi(num1, num2)
    print(f"Resultado da soma: {sum}")
    print(f"Resultado da subtração: {sub}")
    print(f"Resultado da multiplicação: {mult}")
    print(f"Resultado da divisão: {div}")

if __name__ == "__main__":
    main()