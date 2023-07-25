def contar_pares_corretos(botas):
    pares_corretos = 0
    for tamanho, pes in botas.items():
        pares_corretos += min(pes['D'], pes['E'])
    return pares_corretos

while True:
    try:
        # Le o número de botas individuais entregues
        n = int(input())

        # Dicionário para contar as botas por tamanho e pé
        botas = {}
        for _ in range(n):
            # Le o número e pé da bota
            numero, pe = map(str, input().split())

            # Incrementa o contador do tamanho e pé da bota no dicionário
            if numero in botas:
                botas[numero][pe] += 1
            else:
                botas[numero] = {'D': 0, 'E': 0}
                botas[numero][pe] = 1

        # Conta os pares corretos e imprimi do resultado
        pares_corretos = contar_pares_corretos(botas)
        print(pares_corretos)

    except EOFError:
        break
