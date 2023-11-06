def inidica_posicao(sorteada, especulada):
    if len(especulada) != len(sorteada):
        return []
    out = []
    i = 0
    while i < len(especulada):
        if especulada[i] == sorteada[i]:
            out.append(0)
        elif especulada[i] in sorteada:
            out.append(1)
        else:
            out.append(2)
        i += 1
    return out
