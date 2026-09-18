def divisivel():
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num} é divisível por 2 e por 3.")
    elif num % 2 == 0:
        print(f"{num} é divisível apenas por 2.")
    elif num % 3 == 0:
        print(f"{num} é divisível apenas por 3.")
    else:
        print(f"{num} não é divisível por 2 nem por 3.")
            
def main():
    global num
    num = int(input("Digite um número: "))
    divisivel()

if __name__ == "__main__":
    main()