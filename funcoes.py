import random
# 1
def rolar_dados(vezes):
    dados = []                       #Estoque dos dados
    for i in range(vezes):           #Rola o dado o numero de vezes requisitada
        dado = random.randint(1,6)   #Rola o dado
        dados.append(dado)           #Armazena o valor no Estoque
    return dados

# 2
def guardar_dado(rolados, estoque, i_guarda):
    dado = rolados[i_guarda] # Encontra o dado
    del rolados[i_guarda]    # Remove dos rolados
    estoque.append(dado)     # Adiciona ao estoque
    return [rolados, estoque]

# 3
def remover_dado(rolados, estoque, i_guarda):
    dado = estoque[i_guarda]  # Encontra o dado no estoque
    del estoque[i_guarda]     # Remove do estoque
    rolados.append(dado)      # Adiciona novamente aos rolados
    return [rolados, estoque]

# 4
def calcula_pontos_regra_simples(dados_rolados):
    pontos = {}
    for categoria in range(1, 7):   # Verifica dados em cada categoria
        pontos[categoria] = dados_rolados.count(categoria) * categoria # Pontos: categoria * n° dados se enquadram nela(.count)
    return pontos

# 5
def calcula_pontos_soma(dados):
    soma = 0               #Váriavel que receberá a soma dos valores
    for i in dados:        #Pega os valores na lista e faz a soma
        soma += i
    return soma

# 6
def calcula_pontos_sequencia_baixa(dados):
    #Cria váriaveis 
    um = dois = tres = quatro = cinco = seis = False

    #Detecta se os valores estão presentes na sequencia de dados enviada
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

    #Testa os casos de sequencia baixa
    if um == True and dois == True and tres == True and quatro == True:
        return 15
    elif dois == True and tres == True and quatro == True and cinco == True:
        return 15
    elif tres == True and quatro == True and cinco == True and seis == True:
        return 15
    else:
        return 0

# 7
def calcula_pontos_sequencia_alta(dados):
    #Cria Váriaveis
    um = dois = tres = quatro = cinco = seis = False

    #Detecta se os valores estão presentes na sequencia de dados enviada
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

    #Testa os casos de sequencia alta
    if um == True and dois == True and tres == True and quatro == True and cinco == True:
        return 30
    elif dois == True and tres == True and quatro == True and cinco == True and seis ==True:
        return 30
    else:
        return 0

# 8   
def calcula_pontos_full_house(dados):
    # Cria variaveis p modificar
    house = {}
    soma = 0

    # Cria dicionário com ocorrência de cada face
    for d in dados:
        soma += d
        if d not in house.keys():
            house[d] = 1
        else:
            house[d] += 1

    # Verifica o caso full_house : duas faces distintas(len() == 2) repetidas 3 e 2 vezes(3 in and 2 in)
    valores = house.values()
    if len(valores) == 2 and (3 in valores and 2 in valores):
        return soma
    else:
        return 0

#9
def calcula_pontos_quadra(dados):
    #Cria váriaveis
    soma = 0
    quadra = {}
    
    #Conta a quantidade de cada dado
    for dado in dados:
        if dado not in quadra:
            quadra[dado] = 1
        else:
            quadra[dado] += 1
    
    #Testa se a quadra existe e retorna os resultados
    if 4 in quadra.values():
        for ndado,qntd in quadra.items():
            soma += ndado*qntd
        return soma
    else:
        return 0