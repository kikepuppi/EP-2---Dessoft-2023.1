# EP2 - Preenche Frota
frota = {}
nome_navio = 'navio-tanque'
linha = 6
coluna = 1
orientacao = 'horizontal'
tamanho = 3

def define_posicoes(linha, coluna, orientacao, tamanho):
    listresult = []
    if orientacao == 'vertical':
        for i in range (tamanho):
            listresult.append([linha+i,coluna])
    if orientacao == 'horizontal':
        for i in range (tamanho):
            listresult.append([linha,coluna+i])
    return listresult

def preenche_frota(linha, coluna, orientacao, tamanho, nome_navio, frota):
    if nome_navio not in frota.keys():
        frota[nome_navio] = define_posicoes(linha, coluna, orientacao, tamanho)
    else:
        frota[nome_navio] += define_posicoes(linha, coluna, orientacao, tamanho)
    return frota
print(preenche_frota(linha, coluna, orientacao, tamanho, nome_navio, frota))