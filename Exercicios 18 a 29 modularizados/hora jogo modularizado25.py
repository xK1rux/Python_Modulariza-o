def minutos():
    global duraçaoh, duraçaom
    if mFim < mInicio:
        duraçaom = 60 - mInicio + mFim
        duraçaoh = duraçaoh - 1
    else:
        duraçaom = mFim - mInicio
    print(f"A duração do jogo foi de {duraçaoh} horas e {duraçaom} minutos.")

def horas():
    global duraçaoh
    if hInicio == hFim and mInicio == mFim:
        print("O jogo não pode durar 24 horas.")
    elif hFim < hInicio:
        duraçaoh = 24 - hInicio + hFim
        minutos()
    elif hFim > hInicio:
        duraçaoh = hFim - hInicio
        minutos()
    else:
        duraçaoh = 24
        minutos()

def main ():
    global hInicio, hFim, mInicio, mFim
    hInicio =int(input("Digite a hora de início do jogo (0 a 23): "))
    mInicio = int(input("Digite o minuto de início do jogo (0 a 59): "))
    hFim = int(input("Digite a hora de término do jogo (0 a 23): "))
    mFim = int(input("Digite o minuto de término do jogo (0 a 59): "))
    if hInicio < 0 or hInicio > 23 or hFim < 0 or hFim > 23 or mInicio < 0 or mInicio > 59 or mFim < 0 or mFim > 59:
        print("Hora ou minuto inválido. Digite novamente.")
    else:
        horas()

if __name__ == "__main__":
    main()