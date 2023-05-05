# EP - Jogadas do Oponente
import random as rd
rd.seed(2)
# EP2 - Jogadas do jogador
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

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
def afundados(frota, tabuleiro):
    total_afundados = 0
    for navio, posições_gerais in frota.items():
        for posição_umbarco in posições_gerais: 
            for posição in posição_umbarco:
                if tabuleiro[posição[0]][posição[1]] == 'X':
                  total_afundados += 1
    return total_afundados
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
def posiciona_frota(frota):
    tabuleiro = [[0]*10 for i in range(10)]
    for barco, posições in frota.items():
        for posição in posições:
            for linha, coluna in posição:
                tabuleiro[linha][coluna] = 1
    return tabuleiro  

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto
a = 0
jogando = 1
ataques = []
ataques_oponente = []
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
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
while jogando == 1:
    if afundados(frota, tabuleiro_jogador) == 20:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = 0
            continue
    if afundados(frota_oponente, tabuleiro_oponente) == 20:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = 0
            continue
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    linha_atk_oponente = rd.randint(0,9)
    coluna_atk_oponente = rd.randint(0,9)
    atk_o = [linha_atk_oponente, coluna_atk_oponente]
    while atk_o in ataques_oponente:
        linha_atk_oponente = rd.randint(0,9)
        coluna_atk_oponente = rd.randint(0,9)
        atk_o = [linha_atk_oponente, coluna_atk_oponente] 
    ataques_oponente.append(atk_o)
    print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_atk_oponente, coluna_atk_oponente))
    tabuleiro_jogador = faz_jogada(tabuleiro_jogador,linha_atk_oponente,coluna_atk_oponente)
    linha_atk = (input('Qual linha deseja atacar? '))
    while linha_atk == '' or int(linha_atk) < 0 or int(linha_atk) > 9:
        print('Linha inválida!')
        linha_atk = (input('Qual linha deseja atacar? '))
    coluna_atk = (input('Qual coluna deseja atacar? '))
    while coluna_atk == '' or int(coluna_atk) < 0 or int(coluna_atk) > 9:
        print('Coluna inválida!')
        coluna_atk = (input('Qual coluna deseja atacar? '))        
    linha_atk = int(linha_atk)
    coluna_atk = int(coluna_atk)
    while [linha_atk,coluna_atk] in ataques:
        print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha_atk, coluna_atk))
        linha_atk = (input('Qual linha deseja atacar? '))
        while linha_atk == '' or int(linha_atk) < 0 or int(linha_atk) > 9:
            print('Linha inválida!')
            linha_atk = (input('Qual linha deseja atacar? '))
        coluna_atk = (input('Qual coluna deseja atacar? '))
        while coluna_atk == '' or int(coluna_atk) < 0 or int(coluna_atk) > 9:
            print('Coluna inválida!')
            coluna_atk = (input('Qual coluna deseja atacar? '))        
        linha_atk = int(linha_atk)
        coluna_atk = int(coluna_atk)
    ataques.append([linha_atk,coluna_atk])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_atk, coluna_atk)

