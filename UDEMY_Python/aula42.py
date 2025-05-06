frase = 'O Python é uma linguagem de programação'\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum e lançado em 1991.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_mais_frequente = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_mais_frequente = letra_atual
    i += 1

print(f'A letra que mais apareceu foi "{letra_mais_frequente}" e apareceu {qtd_apareceu_mais_vezes} vezes')