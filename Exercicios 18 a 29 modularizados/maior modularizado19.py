def maior():
    if num1 > num2:
        print(f"O maior número é: {num1}.")
    else:
        print(f"O maior número é: {num2}.")

def main():
    global num1, num2
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    maior()

if __name__ == "__main__":
    main()