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




def posiciona_frota(p):
    l = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(10):
        l[i] += [0 for x in range(10)]
    for barco, cordenadas_geral in p.items():
        for cordenada_umbarco in cordenadas_geral:
            for posicao in cordenada_umbarco:
                for T in range(10):
                    for j in range(10):
                        if [T,j] == [posicao[0],posicao[1]]:
                            l[T][j] = 1
    return l

resultado = posiciona_frota(frota)
print(resultado)