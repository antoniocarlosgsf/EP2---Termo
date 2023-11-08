from palavras import palavras
from inicializa_termo import inicializa
from filtra_palavras import filtra
from indica_posicao import indica_posicao
from random import choice
class ANSI():
    def color_text(code):
        return "\33[{code}m".format(code=code)

azul = ANSI.color_text(96) 
amarela = ANSI.color_text(93) 
escura = ANSI.color_text(90) 
branca = ANSI.color_text(37)
vermelha = ANSI.color_text(91)

def valida_palpite(string, tamanho_sorteada):
    if len(string) != tamanho_sorteada:
        return 'apenas palavras de 5 letras'
    elif string not in palavras_do_jogo:
        return 'palavra desconhecida'
    else:
        return True
    

palavras_do_jogo = filtra(palavras, 5)



novamente = 's'
while novamente == 's':
    dados_jogo = inicializa(palavras_do_jogo)
    sorteada = dados_jogo['sorteada']
    tentativas = 6
    print(dados_jogo)
    print(branca)
    print('Você tem {tentativas} tentativa (s)')
    palpite = input('Qual seu palpite')
    validacao = valida_palpite(palpite, 5)
    while validacao != True:
        print('Você tem {tentativas} tentativa (s)')
        palpite = input('Qual seu palpite')
        validacao = valida_palpite(palpite, 5)
    if validacao == True:
        tentativas -= 1
        dados_jogo['especuladas'].append(palpite)
        dados_posicoes = indica_posicao(sorteada, palpite)
        print(' --- --- --- --- ---')
        print('| {} | {} | {} | {} | {}')
        print(' --- --- --- --- ---')
        print('| {} | {} | {} | {} | {}')
        print(' --- --- --- --- ---')
        print('| {} | {} | {} | {} | {}')
        print(' --- --- --- --- ---')
        print('| {} | {} | {} | {} | {}')
        print(' --- --- --- --- ---')
        print('| {} | {} | {} | {} | {}')
        print(' --- --- --- --- ---')
        print('| {} | {} | {} | {} | {}')
        print(' --- --- --- --- ---')



