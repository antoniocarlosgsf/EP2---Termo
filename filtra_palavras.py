def filtra(palavras, n):
    out = []
    for palavra in palavras:
        palavra = palavra.lower()
        if len(palavra) == n and (palavra not in out):
            out.append(palavra)
    return out