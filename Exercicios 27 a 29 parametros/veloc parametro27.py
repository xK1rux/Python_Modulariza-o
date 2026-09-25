def velocKm(nVoltas, dist, temp):
    vel = ((nVoltas * dist) / temp) * 0.06
    return vel

def main():
    numVoltas = int(input("Digite o número de voltas: "))
    distancia = int(input("Digite a extensão do circuito (em m): "))
    tempo = int(input("Digite o tempo gasto (em min): "))
    velocidade = velocKm(numVoltas, distancia, tempo)
    print(f"A velocidade média foi de {velocidade:.2f} km/h.")

if __name__ == "__main__":
    main()