# EP2 - Posição Válida

frota = {
    "navio-tanque":[
      [[6,1],[6,2],[6,3]],
      [[4,7],[5,7],[6,7]]
    ],
    "contratorpedeiro":[
      [[1,1],[2,1]],
      [[2,3],[3,3]],
      [[9,1],[9,2]]
    ],
    "submarino": [
      [[0,3]],
      [[4,5]],
      [[8,9]],
      [[8,4]]
    ],
}
linha = 8
coluna = 8
orientacao = 'horizontal'
tamanho = 4

def define_posicoes(linha, coluna, orientacao, tamanho):
    listresult = []
    if orientacao == 'vertical':
        for i in range (tamanho):
            listresult.append([linha+i,coluna])
    if orientacao == 'horizontal':
        for i in range (tamanho):
            listresult.append([linha,coluna+i])
    return listresult
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    if frota == {}:
        return False
    for k , v in frota.items():
        for k in frota.keys():
            for i in range(len(v)):
                for j in range (len(v[i])):
                    if v[i][j] in define_posicoes(linha, coluna, orientacao, tamanho):
                        return False
    for valores in define_posicoes(linha, coluna, orientacao, tamanho):
        for numeros in valores:
            if valores[0] > 9 or valores[1] > 9:
                return False
    return True
                    
resultado = posicao_valida(frota, linha, coluna, orientacao, tamanho)
print(resultado)

