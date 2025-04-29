import random
def rolar_dados(vezes):
    dados = []
    for i in range(vezes):
        dado = random.randint(1,6)
        dados.append(dado)
    return dados

def guardar_dado(rolados, estoque, i_guarda):
    dado = rolados[i_guarda] # Encontra o dado
    del rolados[i_guarda]    # Remove dos rolados
    estoque.append(dado)     # Adiciona ao estoque
    return [rolados, estoque]

def remover_dado(rolados, estoque, i_guarda):
    dado = estoque[i_guarda]  # Encontra o dado no estoque
    del estoque[i_guarda]     # Remove do estoque
    rolados.append(dado)      # Adiciona novamente aos rolados
    return [rolados, estoque]