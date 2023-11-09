from palavras import palavras
from inicializa_termo import inicializa
from filtra_palavras import filtra
from indica_posicao import indica_posicao
from random import choice

class ANSI():
    def color_text(code=''):
        return "\33[{code}m".format(code=code)

azul = ANSI.color_text(96) 
amarela = ANSI.color_text(93) 
escura = ANSI.color_text(90) 
branca = ANSI.color_text(37)
vermelha = ANSI.color_text(91)
reset = ANSI.color_text()
letra = azul + 'a' + reset

def valida_palpite(string, tamanho_sorteada):
    if string == 'desisto':
        return 'desistiu'
    if len(string) != tamanho_sorteada:
        return 'apenas palavras de 5 letras'
    elif string not in palavras_do_jogo:
        return 'palavra desconhecida'
    else:
        return True
    
def formata_entrada(entrada):
    out = entrada.strip()
    out = out.lower()
    return out



palavras_do_jogo = filtra(palavras, 5)



ganhou = False
perdeu = False
novamente = 's'
certeza = ''
while novamente == 's':
    dados_jogo = inicializa(palavras_do_jogo)
    sorteada = dados_jogo['sorteada']
    tentativas = 6
    print(dados_jogo)
    print(branca)
    lista_colorida = ['     ', '     ', '     ', '     ', '     ', '     ']
    while True:
        if tentativas == 0:
            print(f'Você perdeu, a palavra era: {sorteada}')
            print()
            perdeu = True
            break
        print(f'Você tem {tentativas} tentativa (s)')
        palpite = input('Qual seu palpite? ')
        palpite = formata_entrada(palpite)
        print(palpite)
        validacao = valida_palpite(palpite, 5)
        while validacao == 'desistiu':
            certeza = input('Tem certeza que deseja desistir? [s/n] ')
            if certeza == 's':
                print(f'>>> Que deselegante desistir, a palavra era: {sorteada}')
                print()
                break
            else:
                print(f'Você tem {tentativas} tentativa (s)')
                palpite = input('Qual seu palpite? ')
                validacao = valida_palpite(palpite, 5)
        while validacao != True and validacao != 'desistiu':
            print(validacao)
            print(f'Você tem {tentativas} tentativa (s)')
            palpite = input('Qual seu palpite? ')
            validacao = valida_palpite(palpite, 5)
        if validacao == True:
            dados_jogo['especuladas'].append(palpite)
            dados_posicoes = indica_posicao(sorteada, palpite)
            palpite_colorido = []
            for i in range(len(palpite)):
                if dados_posicoes[i] == 0:
                    letra = azul + palpite[i] + reset

                elif dados_posicoes[i] == 1:
                    letra = amarela + palpite[i] + reset
                
                else:
                    letra = escura + palpite[i] + reset
                
                palpite_colorido.append(letra)
            lista_colorida[6-tentativas] = palpite_colorido
            tentativas -= 1
    

            print(lista_colorida)

            print(' --- --- --- --- ---')
            print(f'| {lista_colorida[0][0]} | {lista_colorida[0][1]} | {lista_colorida[0][2]} | {lista_colorida[0][3]} | {lista_colorida[0][4]} |')
            print(' --- --- --- --- ---')
            print(f'| {lista_colorida[1][0]} | {lista_colorida[1][1]} | {lista_colorida[1][2]} | {lista_colorida[1][3]} | {lista_colorida[1][4]} |')
            print(' --- --- --- --- ---')
            print(f'| {lista_colorida[2][0]} | {lista_colorida[2][1]} | {lista_colorida[2][2]} | {lista_colorida[2][3]} | {lista_colorida[2][4]} |')
            print(' --- --- --- --- ---')
            print(f'| {lista_colorida[3][0]} | {lista_colorida[3][1]} | {lista_colorida[3][2]} | {lista_colorida[3][3]} | {lista_colorida[3][4]} |')
            print(' --- --- --- --- ---')
            print(f'| {lista_colorida[4][0]} | {lista_colorida[4][1]} | {lista_colorida[4][2]} | {lista_colorida[4][3]} | {lista_colorida[4][4]} |')
            print(' --- --- --- --- ---')
            print(f'| {lista_colorida[5][0]} | {lista_colorida[5][1]} | {lista_colorida[5][2]} | {lista_colorida[5][3]} | {lista_colorida[5][4]} |')
            print(' --- --- --- --- ---')
            if palpite == sorteada:
                tentativas_feitas = 6 - tentativas
                print(f'*** Parabéns! Você acertou depois de {tentativas_feitas} tentativas!')
                print()
                ganhou = True
                break
        if certeza == 's':
            break

    if validacao == 'desistiu':
        novamente = input('Deseja jogar novamente? [s|n] ')
        if novamente == 'n':
            print()
            print()
            print()
            print()
            print('Até a próxima!')
    if ganhou:
        novamente = input('Deseja jogar novamente? [s|n] ')
        if novamente == 'n':
            print()
            print()
            print()
            print()
            print('Até a próxima!')
    if perdeu:
        novamente = input('Deseja jogar novamente? [s|n] ')
        if novamente == 'n':
            print()
            print()
            print()
            print()
            print('Até a próxima!')
            
        



