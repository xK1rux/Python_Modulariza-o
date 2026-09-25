def calcFatorial(num):
    fat = 1
    soma = 1
    for i in range(1, num + 1):
        fat *= i
        soma += calcSerie(fat)
    return fat, soma

def calcSerie(f):
    somaSerie = 1 / f
    return somaSerie

def main():
    numero = int(input("Digite um número inteiro para calcular o fatorial: "))
    fatorial, soma = calcFatorial(numero)
    print(f"O fatorial de {numero} é: {fatorial}")
    print(f"A soma das frações de 1 + 1/1! + ... 1/{numero}! é: {soma:.2f}")

if __name__ == "__main__":
    main()