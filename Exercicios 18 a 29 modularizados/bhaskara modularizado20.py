def bhaskara():
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"A única raiz real é: {x}")
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f"As raízes reais são: {x1} e {x2}")

def main ():
    global a, b, c
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    bhaskara()

if __name__ == "__main__":
    main()