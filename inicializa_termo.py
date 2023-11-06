from random import choice
def inicializa(palavras):
    n = len(palavras[0])
    sorteada = choice(palavras)
    out = {'n': n, 'sorteada': sorteada, 'especuladas': [], 'tentativas': n+1}
    return out