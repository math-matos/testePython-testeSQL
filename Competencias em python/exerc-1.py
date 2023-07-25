def encontrar_peca_faltando(N, pecas):
    soma_total = N * (N + 1) // 2
    soma_das_pecas = sum(pecas)
    peca_faltando = soma_total - soma_das_pecas
    return peca_faltando

# Leitura da sua entrada
N = int(input())
pecas = list(map(int, input().split()))

# Chama a função para encontrar a peça faltando
peca_faltando = encontrar_peca_faltando(N, pecas)

# Saída = Resultado
print(peca_faltando)

# Pausa no final para manter a janela do cmd aberta
input("Pressione Enter para fechar...")