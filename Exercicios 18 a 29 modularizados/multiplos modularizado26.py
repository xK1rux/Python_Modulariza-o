def multiplos():
    if num1 > num2:
        if num1 % num2 == 0:
            print (f"{num1} é múltiplo de {num2}.")
        else:
            print (f"{num1} não é múltiplo de {num2}.")
    else:
        if num2 % num1 == 0:
            print (f"{num2} é múltiplo de {num1}.")
        else:
            print (f"{num2} não é múltiplo de {num1}.")

def main ():
    global num1, num2
    num1 = int (input("Digite o primeiro número: "))
    num2 = int (input("Digite o segundo número: "))
    multiplos()

if __name__ == "__main__":
    main()