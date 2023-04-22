frota = {
    "porta-aviões":[
      [[1,5],[1,6],[1,7],[1,8]]
    ],
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


def posiciona_frota(frota):
    tabuleiro = [[0]*10 for i in range(10)]
    for barco, posições in frota.items():
        for posição in posições:
            for linha, coluna in posição:
                tabuleiro[linha][coluna] = 1
    return tabuleiro 

resultado = posiciona_frota(frota)
print(resultado)