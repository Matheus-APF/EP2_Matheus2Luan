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
    # Cria variaveis p operações
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

# 9
def calcula_pontos_quadra(dados):
    #Cria váriaveis
    soma = 0
    quadra = {}
    quadraa = False
    
    #Conta a quantidade de cada dado
    for dado in dados:
        if dado not in quadra:
            quadra[dado] = 1
        else:
            quadra[dado] += 1
    
    #Testa se a quadra existe
    for i in quadra.values():
        if i >= 4:
            quadraa = True
    
    #Retorna os Valores
    if quadraa == True:
        for ndado,qntd in quadra.items():
            soma += ndado*qntd
        return soma
    else:
        return 0

# 10
def calcula_pontos_quina(dados):
    # Cria váriaveis p operações
    quina = {}
    
   # Cria dicionário com ocorrência de cada face
    for d in dados:
        if d not in quina.keys():
            quina[d] = 1
        else:
            quina[d] += 1
    
    # Verifica ocorrência de quina (valor ocorrencia >= 5)
    for valor in quina.values():
        if valor >= 5:
            return 50

    # Fim do fluxo --> Não há quina --> Retorna 0
    return 0

#11
def calcula_pontos_regra_avancada(dices):
    #Puxa as funcoes anteriores e calcula as pontuações
    pontuacoes = {}
    pontuacoes["cinco_iguais"] = calcula_pontos_quina(dices)
    pontuacoes["full_house"] = calcula_pontos_full_house(dices)
    pontuacoes["quadra"] = calcula_pontos_quadra(dices)
    pontuacoes["sem_combinacao"] = calcula_pontos_soma(dices)
    pontuacoes["sequencia_alta"] = calcula_pontos_sequencia_alta(dices)
    pontuacoes["sequencia_baixa"] = calcula_pontos_sequencia_baixa(dices)

    return pontuacoes

# 12
def faz_jogada(dados, categoria, cartela):

    # Verifica se a categoria se enquadra na regra simples
    if len(categoria) == 1:        # String com um numero apenas enquadra essa categoria (ex: 1, 2, 5, 6)
        # Calcula os pontos para a categoria simples
        pontos = calcula_pontos_regra_simples(dados)
        cartela['regra_simples'][int(categoria)] = pontos[int(categoria)]
    else:
        # Calcula os pontos para a categoria avançada
        pontos = calcula_pontos_regra_avancada(dados)
        cartela['regra_avancada'][categoria] = pontos[categoria]
    return cartela

# 13 (professor)
def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)

#Jogo
#Cria as cartelas
cartela = {
        'regra_simples': {i: -1 for i in range(1, 7)},
        'regra_avancada': {
            'sem_combinacao': -1,
            'quadra': -1,
            'full_house': -1,
            'sequencia_baixa': -1,
            'sequencia_alta': -1,
            'cinco_iguais': -1
        }
    }
#Cria as váriaveis permanentes
rodada = 1
usadas = []
comb_simples_vald = ["1",'2','3','4','5','6',]
comb_avanc_vald = ['sem_combinacao','quadra',"full_house",'sequencia_baixa',"sequencia_alta","cinco_iguais",]
comb_vald = comb_avanc_vald +comb_simples_vald
imprime_cartela(cartela)
#Contador para encerrar o jogo após as 12 rodadas
while rodada < 13:
    #Cria variaveis resetadas a cada rodada
    opcoes = True
    rerolagens = 0
    guardados = []
    rolados = rolar_dados(5)
    print("Dados rolados: {}".format(rolados))
    print("Dados guardados: {}".format(guardados))
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    opcao = input()
    #Opções de comando que o usuário pode executar no jogo
    while opcoes == True:
        #Opção 1
        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indicie = int(input())
            operacao = guardar_dado(rolados,guardados,indicie)
            rolados = operacao[0]
            guardados = operacao[1]
            print("Dados rolados: {}".format(rolados))
            print("Dados guardados: {}".format(guardados))
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            opcao = input()
        #Opção 2
        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indicie = int(input())
            operacao = remover_dado(rolados,guardados,indicie)
            rolados = operacao[0]
            guardados = operacao[1]
            print("Dados rolados: {}".format(rolados))
            print("Dados guardados: {}".format(guardados))
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            opcao = input()
        #Opção 3
        elif opcao == "3":
            if rerolagens !=2:
                rolados = rolar_dados(len(rolados))
                rerolagens +=1
                print("Dados rolados: {}".format(rolados))
                print("Dados guardados: {}".format(guardados))
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
                opcao = input()
            else:
                print("Você já usou todas as rerrolagens.")
                print("Dados rolados: {}".format(rolados))
                print("Dados guardados: {}".format(guardados))
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
                opcao = (input())
        #Opção 4
        elif opcao == "4":
            imprime_cartela(cartela)
            print("Dados rolados: {}".format(rolados))
            print("Dados guardados: {}".format(guardados))
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            opcao = input()
        #Opção 0 que encerra a rodada
        elif opcao == "0":
            opcoes = False
        #Caso o usuário utilize uma opção não valida
        else:
            print("Opção inválida. Tente novamente.")
            opcao = input()
    #Testa se a combinação é valida e ainda não foi utilizada
    vald_combinacao = False
    print("Digite a combinação desejada:")
    while vald_combinacao == False:
        combinacao = input()
        if combinacao in usadas:
            print("Essa combinação já foi utilizada.")
        elif combinacao in comb_vald:
            vald_combinacao = True
            usadas.append(combinacao)
        else:
            print("Combinação inválida. Tente novamente.")
    #Agrupa todos os dados e faz a jogada
    dados = guardados + rolados
    cartela = faz_jogada(dados,combinacao,cartela)
    rodada += 1
#Encerra o jogo
imprime_cartela(cartela)
pontuacao_simples = calcula_pontos_soma(cartela["regra_simples"].values())
pontuacao_avancada = calcula_pontos_soma(cartela["regra_avancada"].values())
if pontuacao_simples >= 63:
    pontuacao_simples += 35
pontuacao = pontuacao_simples +pontuacao_avancada
print("Pontuação total: {}".format(pontuacao))
    