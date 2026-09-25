def calcPreco(pA, mM):
    if pA < 30 and mM < 500:
        nP = pA * 1.10
    elif 30 <= pA < 80 and 500 < mM < 1000:
        nP = pA * 1.15
    elif pA >= 80 and mM >= 1000:
        nP = pA * 0.95
    else:
        nP = pA
    return nP

def main():
    precoAtual = float(input("Digite o preço atual do produto: "))
    mediaMensal = float(input("Digite a média mensal de vendas do produto: "))
    novoPreco = calcPreco(precoAtual, mediaMensal)
    print(f"O novo preço do produto é: R$ {novoPreco:.2f}")

if __name__ == "__main__":
    main()