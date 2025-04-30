import random
def rolar_dados(vezes):
    dados = []                       #Estoque dos dados
    for i in range(vezes):           #Rola o dado o numero de vezes requisitada
        dado = random.randint(1,6)   #Rola o dado
        dados.append(dado)           #Armazena o valor no Estoque
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
def calcula_pontos_sequencia_baixa(dados):
    um = dois = tres = quatro = cinco = seis = False
    for i in dados:
        if i == 1:
            um =  True
        elif i == 2:
            dois = True
        elif i == 3:
            tres = True
        elif i == 4:
            quatro = True
        elif i == 5:
            cinco = True
        else:
            seis = True
    if um == True and dois == True and tres == True and quatro == True:
        return 15
    elif dois == True and tres == True and quatro == True and cinco == True:
        return 15
    elif tres == True and quatro == True and cinco == True and seis == True:
        return 15
    else:
        return 0