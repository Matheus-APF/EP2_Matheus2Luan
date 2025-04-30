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

def calcula_pontos_regra_simples(dados_rolados):
    pontos = {}
    for categoria in range(1, 7):   # Verifica dados em cada categoria
        pontos[categoria] = dados_rolados.count(categoria) * categoria # Pontos: categoria * n° dados se enquadram nela(.count)
    return pontos
def calcula_pontos_soma(dados):
    soma = 0
    for i in dados:
        soma += i
    return soma