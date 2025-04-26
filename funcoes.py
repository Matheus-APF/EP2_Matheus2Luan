import random
def rolar_dados(vezes):
    dados = []
    for i in range(vezes):
        dado = random.randint(1,6)
        dados.append(dado)
    return dados