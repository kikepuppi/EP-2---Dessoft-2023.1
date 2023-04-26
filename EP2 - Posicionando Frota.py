#EP2 - Posicionando Frota
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
def define_posicoes(linha, coluna, orientacao, tamanho):
    listresult = []
    if orientacao == 1:
        for i in range (tamanho):
            listresult.append([linha+i,coluna])
    if orientacao == 2:
        for i in range (tamanho):
            listresult.append([linha,coluna+i])
    return listresult

def preenche_frota(frota,navio, linha, coluna, orientacao, tamanho):
    if navio not in frota.keys():
        frota[navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    else:
        frota[navio] += [define_posicoes(linha, coluna, orientacao, tamanho)]
    return frota

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    x = define_posicoes(linha, coluna, orientacao, tamanho)
    for valores in x:
        for numeros in valores:
            if valores[0] > 9 or valores[1] > 9:
                return False
    if frota == {}:
        return True
    for k , v in frota.items():
        for i in range(len(v)):
            for j in range (len(v[i])):
                if v[i][j] in x:
                    return False   
    return True

def faz_perguntas(navio, tamanho):
    a = 0
    while a == 0:
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio,tamanho))
        linha = (input('Qual linha? '))
        coluna = (input('Qual coluna? '))
        orientacao = '1'
        if navio != 'submarino':
            orientacao = (input('Vertical [1] ou Horizontal [2]? '))
        if linha == '' or coluna == '':
            print('Esta posição não está válida!')
        elif posicao_valida(frota, int(linha), int(coluna), int(orientacao), tamanho) == False:
            print('Esta posição não está válida!')
        elif orientacao != '1' and orientacao != '2':
            print('Esta posição não está válida!')
        else:
            linha = int(linha)
            coluna = int(coluna)
            orientacao = int(orientacao)
            a = 1 
    return [linha,coluna,orientacao]


navio = 'porta-aviões'
tamanho = 4
x = faz_perguntas(navio,tamanho)
frota = preenche_frota(frota,navio,x[0],x[1],x[2],tamanho)
for i in range (2):
    navio = "navio-tanque"
    tamanho = 3
    x = faz_perguntas(navio,tamanho)
    frota = preenche_frota(frota,navio,x[0],x[1],x[2],tamanho)
for i in range (3):
    navio = "contratorpedeiro"
    tamanho = 2
    x = faz_perguntas(navio,tamanho)
    frota = preenche_frota(frota,navio,x[0],x[1],x[2],tamanho)
for i in range(4):
    navio = 'submarino'
    tamanho = 1
    x = faz_perguntas(navio,tamanho)
    frota = preenche_frota(frota,navio,x[0],x[1],x[2],tamanho)
print(frota)






