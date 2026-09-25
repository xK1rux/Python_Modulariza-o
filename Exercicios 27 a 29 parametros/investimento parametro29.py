def calcRendimento(tipo, valor):
    if tipo == 1:
        rend =valor * 1.03
    elif tipo == 2:
        rend = valor * 1.05
    return rend

def main():
    tipoInv = int(input("Digite o tipo de investimento (1 - Poupança, 2 - Renda Fixa): "))
    if tipoInv == 1 or tipoInv == 2:
        valorInv = int(input("Digite o valor do investimento: "))
        rendimento = calcRendimento(tipoInv, valorInv)
        print(f"O rendimento do investimento é R$ {rendimento:.2f}.")
    else:
        print("Tipo de investimento inválido. Por favor, escolha 1 para Poupança ou 2 para Renda Fixa.")

if __name__ == "__main__":
    main()