#Importando bibliotecas e funcções e base de palavras
from palavras import palavras
from inicializa_termo import inicializa
from filtra_palavras import filtra
from indica_posicao import indica_posicao
from random import choice

#Defindo algumas novas funções
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

#Definindo as cores que serão utilizadas
class ANSI():
    def color_text(code=''):
        return "\33[{code}m".format(code=code)

azul = ANSI.color_text(96) 
amarela = ANSI.color_text(93) 
escura = ANSI.color_text(90) 
reset = ANSI.color_text()


print('Níveis: Facíl (5 letras)\n        Médio (6 letras)\n        Difícil (7 letras)')
print()

dificuldade = int(input('Com quantas letras deseja jogar? '))
palavras_do_jogo = filtra(palavras, 5)


if dificuldade == 5:
    #Iniciando o jogo
    palavras_do_jogo = filtra(palavras, 5)
    ganhou = False
    perdeu = False
    novamente = 's'
    certeza = ''
    #Jogo Rodando Inifinitamente até a decisão do jogador
    while novamente == 's':
        dados_jogo = inicializa(palavras_do_jogo)
        sorteada = dados_jogo['sorteada']
        tentativas = 6
        lista_colorida = ['     ', '     ', '     ', '     ', '     ', '     ']
        while True:
            #Testando se o jogador ainda tem tentativas disponíveis
            if tentativas == 0:
                print(f'Você perdeu, a palavra era: {sorteada}')
                print()
                perdeu = True
                break
            print(f'Você tem {tentativas} tentativa (s)')
            palpite = input('Qual seu palpite? ')
            palpite = formata_entrada(palpite)
            #Testando se a palavra já foi usada
            if palpite in dados_jogo['especuladas']:
                print('Palavra já testada')
                print()
                validacao = False
            else:
                validacao = valida_palpite(palpite, 5)
            #Testando se o jogador desistiu
            if validacao == 'desistiu':
                certeza = input('Tem certeza que deseja desistir? [s/n] ')
                if certeza == 's':
                    print(f'>>> Que deselegante desistir, a palavra era: {sorteada}')
                    print()
                    break
            #Validando a entrada do jogador
            if validacao != True and validacao != 'desistiu' and validacao != False:
                print(validacao)
            #Rodando o jogo quando o jogador chutar uma palavra válida
            if validacao == True:
                dados_jogo['especuladas'].append(palpite)
                dados_posicoes = indica_posicao(sorteada, palpite)
                palpite_colorido = []
                #Colorindo as letras
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
                #Printando a interface do jogo
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
        #Jogando novamente
        novamente = input('Deseja jogar novamente? [s|n] ')
        if novamente == 'n':
            print()
            print()
            print()
            print()
            print('Até a próxima!')

elif dificuldade == 6:
    #Iniciando o jogo
    palavras_do_jogo = filtra(palavras, 6)
    ganhou = False
    perdeu = False
    novamente = 's'
    certeza = ''
    #Jogo Rodando Inifinitamente até a decisão do jogador
    while novamente == 's':
        dados_jogo = inicializa(palavras_do_jogo)
        sorteada = dados_jogo['sorteada']
        tentativas = 7
        lista_colorida = ['      ', '      ', '      ', '      ', '      ', '      ', '      ']
        while True:
            #Testando se o jogador ainda tem tentativas disponíveis
            if tentativas == 0:
                print(f'Você perdeu, a palavra era: {sorteada}')
                print()
                perdeu = True
                break
            print(f'Você tem {tentativas} tentativa (s)')
            palpite = input('Qual seu palpite? ')
            palpite = formata_entrada(palpite)
            #Testando se a palavra já foi usada
            if palpite in dados_jogo['especuladas']:
                print('Palavra já testada')
                print()
                validacao = False
            else:
                validacao = valida_palpite(palpite, 6)
            #Testando se o jogador desistiu
            if validacao == 'desistiu':
                certeza = input('Tem certeza que deseja desistir? [s/n] ')
                if certeza == 's':
                    print(f'>>> Que deselegante desistir, a palavra era: {sorteada}')
                    print()
                    break
            #Validando a entrada do jogador
            if validacao != True and validacao != 'desistiu' and validacao != False:
                print(validacao)
            #Rodando o jogo quando o jogador chutar uma palavra válida
            if validacao == True:
                dados_jogo['especuladas'].append(palpite)
                dados_posicoes = indica_posicao(sorteada, palpite)
                palpite_colorido = []
                #Colorindo as letras
                for i in range(len(palpite)):
                    if dados_posicoes[i] == 0:
                        letra = azul + palpite[i] + reset

                    elif dados_posicoes[i] == 1:
                        letra = amarela + palpite[i] + reset
                    
                    else:
                        letra = escura + palpite[i] + reset
                    
                    palpite_colorido.append(letra)
                lista_colorida[7-tentativas] = palpite_colorido
                tentativas -= 1
                #Printando a interface do jogo
                print(' --- --- --- --- ---')
                print(f'| {lista_colorida[0][0]} | {lista_colorida[0][1]} | {lista_colorida[0][2]} | {lista_colorida[0][3]} | {lista_colorida[0][4]} | {lista_colorida[0][5]} |')
                print(' --- --- --- --- --- ---')
                print(f'| {lista_colorida[1][0]} | {lista_colorida[1][1]} | {lista_colorida[1][2]} | {lista_colorida[1][3]} | {lista_colorida[1][4]} | {lista_colorida[1][5]} |')
                print(' --- --- --- --- --- ---')
                print(f'| {lista_colorida[2][0]} | {lista_colorida[2][1]} | {lista_colorida[2][2]} | {lista_colorida[2][3]} | {lista_colorida[2][4]} | {lista_colorida[2][5]} |')
                print(' --- --- --- --- --- ---')
                print(f'| {lista_colorida[3][0]} | {lista_colorida[3][1]} | {lista_colorida[3][2]} | {lista_colorida[3][3]} | {lista_colorida[3][4]} | {lista_colorida[3][5]} |')
                print(' --- --- --- --- --- ---')
                print(f'| {lista_colorida[4][0]} | {lista_colorida[4][1]} | {lista_colorida[4][2]} | {lista_colorida[4][3]} | {lista_colorida[4][4]} | {lista_colorida[4][5]} |')
                print(' --- --- --- --- --- ---')
                print(f'| {lista_colorida[5][0]} | {lista_colorida[5][1]} | {lista_colorida[5][2]} | {lista_colorida[5][3]} | {lista_colorida[5][4]} | {lista_colorida[5][5]} |')
                print(' --- --- --- --- --- ---')
                print(f'| {lista_colorida[6][0]} | {lista_colorida[6][1]} | {lista_colorida[6][2]} | {lista_colorida[6][3]} | {lista_colorida[6][4]} | {lista_colorida[6][5]} |')
                print(' --- --- --- --- --- ---')
                if palpite == sorteada:
                    tentativas_feitas = 7 - tentativas
                    print(f'*** Parabéns! Você acertou depois de {tentativas_feitas} tentativas!')
                    print()
                    ganhou = True
                    break
            if certeza == 's':
                break
        #Jogando novamente
        novamente = input('Deseja jogar novamente? [s|n] ')
        if novamente == 'n':
            print()
            print()
            print()
            print()
            print('Até a próxima!')

elif dificuldade == 7:
        #Iniciando o jogo
    palavras_do_jogo = filtra(palavras, 7)
    ganhou = False
    perdeu = False
    novamente = 's'
    certeza = ''
    #Jogo Rodando Inifinitamente até a decisão do jogador
    while novamente == 's':
        dados_jogo = inicializa(palavras_do_jogo)
        sorteada = dados_jogo['sorteada']
        tentativas = 8
        lista_colorida = ['       ', '       ', '       ', '       ', '       ', '       ', '       ']
        while True:
            #Testando se o jogador ainda tem tentativas disponíveis
            if tentativas == 0:
                print(f'Você perdeu, a palavra era: {sorteada}')
                print()
                perdeu = True
                break
            print(f'Você tem {tentativas} tentativa (s)')
            palpite = input('Qual seu palpite? ')
            palpite = formata_entrada(palpite)
            #Testando se a palavra já foi usada
            if palpite in dados_jogo['especuladas']:
                print('Palavra já testada')
                print()
                validacao = False
            else:
                validacao = valida_palpite(palpite, 7)
            #Testando se o jogador desistiu
            if validacao == 'desistiu':
                certeza = input('Tem certeza que deseja desistir? [s/n] ')
                if certeza == 's':
                    print(f'>>> Que deselegante desistir, a palavra era: {sorteada}')
                    print()
                    break
            #Validando a entrada do jogador
            if validacao != True and validacao != 'desistiu' and validacao != False:
                print(validacao)
            #Rodando o jogo quando o jogador chutar uma palavra válida
            if validacao == True:
                dados_jogo['especuladas'].append(palpite)
                dados_posicoes = indica_posicao(sorteada, palpite)
                palpite_colorido = []
                #Colorindo as letras
                for i in range(len(palpite)):
                    if dados_posicoes[i] == 0:
                        letra = azul + palpite[i] + reset

                    elif dados_posicoes[i] == 1:
                        letra = amarela + palpite[i] + reset
                    
                    else:
                        letra = escura + palpite[i] + reset
                    
                    palpite_colorido.append(letra)
                lista_colorida[8-tentativas] = palpite_colorido
                tentativas -= 1
                #Printando a interface do jogo
                print(' --- --- --- --- ---')
                print(f'| {lista_colorida[0][0]} | {lista_colorida[0][1]} | {lista_colorida[0][2]} | {lista_colorida[0][3]} | {lista_colorida[0][4]} | {lista_colorida[0][5]} |')
                print(' --- --- --- --- --- ---')
                print(f'| {lista_colorida[1][0]} | {lista_colorida[1][1]} | {lista_colorida[1][2]} | {lista_colorida[1][3]} | {lista_colorida[1][4]} | {lista_colorida[1][5]} |')
                print(' --- --- --- --- --- ---')
                print(f'| {lista_colorida[2][0]} | {lista_colorida[2][1]} | {lista_colorida[2][2]} | {lista_colorida[2][3]} | {lista_colorida[2][4]} | {lista_colorida[2][5]} |')
                print(' --- --- --- --- --- ---')
                print(f'| {lista_colorida[3][0]} | {lista_colorida[3][1]} | {lista_colorida[3][2]} | {lista_colorida[3][3]} | {lista_colorida[3][4]} | {lista_colorida[3][5]} |')
                print(' --- --- --- --- --- ---')
                print(f'| {lista_colorida[4][0]} | {lista_colorida[4][1]} | {lista_colorida[4][2]} | {lista_colorida[4][3]} | {lista_colorida[4][4]} | {lista_colorida[4][5]} |')
                print(' --- --- --- --- --- ---')
                print(f'| {lista_colorida[5][0]} | {lista_colorida[5][1]} | {lista_colorida[5][2]} | {lista_colorida[5][3]} | {lista_colorida[5][4]} | {lista_colorida[5][5]} |')
                print(' --- --- --- --- --- ---')
                print(f'| {lista_colorida[6][0]} | {lista_colorida[6][1]} | {lista_colorida[6][2]} | {lista_colorida[6][3]} | {lista_colorida[6][4]} | {lista_colorida[6][5]} |')
                print(' --- --- --- --- --- ---')
                if palpite == sorteada:
                    tentativas_feitas = 8 - tentativas
                    print(f'*** Parabéns! Você acertou depois de {tentativas_feitas} tentativas!')
                    print()
                    ganhou = True
                    break
            if certeza == 's':
                break
        #Jogando novamente
        novamente = input('Deseja jogar novamente? [s|n] ')
        if novamente == 'n':
            print()
            print()
            print()
            print()
            print('Até a próxima!')



