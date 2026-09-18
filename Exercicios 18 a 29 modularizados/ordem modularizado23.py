def ordem():
    if num3 > num2 > num1:
        if num4 < num1:
            print(f"{num4}, {num1}, {num2}, {num3}")
        elif num4 > num1 and num4 < num2:
            print(f"{num1}, {num4}, {num2}, {num3}")
        elif num4 > num2 and num4 < num3:
            print(f"{num1}, {num2}, {num4}, {num3}")
        else:
            print(f"{num1}, {num2}, {num3}, {num4}")
    else:
        print("Os 3 primeiros números não estão em ordem crescente.")

def main ():
    global num1, num2, num3, num4
    num1 = int(input("Digite os 3 primeiros números em ordem crescente: "))
    num2 = int(input("Digite os 3 primeiros números em ordem crescente: "))
    num3 = int(input("Digite os 3 primeiros números em ordem crescente: "))
    num4 = int(input("Digite um número não necessariamente na ordem: "))
    ordem()

if __name__ == "__main__":
    main()