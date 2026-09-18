def diferença():
    if num1 > num2:
        conta = num1 - num2
    else:
        conta = num2 - num1
    print(f"A diferença entre {num2} e {num1} é: {conta}.")    

def main ():
    global num1, num2
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    diferença()
    
if __name__ == "__main__":
    main()