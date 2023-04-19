# EP2 - Define posições
linha = 2
coluna = 4
orientacao = "horizontal"
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
print(define_posicoes(linha, coluna, orientacao, tamanho))
        

