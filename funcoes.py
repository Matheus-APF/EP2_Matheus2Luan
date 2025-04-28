import random
def rolar_dados(vezes):
    dados = []
    for i in range(vezes):
        dado = random.randint(1,6)
        dados.append(dado)
    return dados

def guardar_dado(rolados,estoque, i_guarda):
    dado = rolados[i_guarda] #encontra o dado
    del rolados[i_guarda]    #remove dos rolados
    estoque.append(dado)     #adiciona ao estoque
    return [rolados, estoque]