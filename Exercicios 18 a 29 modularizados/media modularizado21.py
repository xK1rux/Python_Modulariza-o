def media():
    media = (nota1 + nota2 + nota3 + nota4)/4
    if media >= 6:
        print(f" APROVADO: {media:.2f}")
    elif media >= 3:
        print(f"EXAME: {media:.2f}")
    else:
        print(f"REPROVADO: {media:.2f}")

def main ():
    global nota1, nota2, nota3, nota4
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media()

if __name__ == "__main__":
    main()