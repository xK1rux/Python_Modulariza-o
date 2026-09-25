def calcFatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat

def main():
    num = int(input("Digite um número inteiro para calcular o fatorial: "))
    fatorial = calcFatorial(num)
    print(f"O fatorial de {num} é {fatorial}")

if __name__ == "__main__":
    main()