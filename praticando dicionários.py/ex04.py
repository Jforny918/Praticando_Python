jogador = dict()
partidas = list ()
jogador['nome'] = str(input("Nome de Jogador: ")) #armazenando o nome do jogador
jogador['partidas'] = int(input(f"Número de partidas que {jogador['nome']} jogou: ")) #armazenando o número de partidas jogadas
jogador['gols'] = [] #armazenando os gols em uma lista

for c in range(0, jogador['partidas']): #para cada partida jogada, irá solicitar o número de gols
    partidas.append(int(input(f"Número de gols que {jogador['nome']} fez na partida {c + 1}: "))) #armazena cada número de gols na lista

jogador['gols'] = partidas #armazena a lista de gols no dicionário
jogador['total'] = sum(partidas) #armazena a soma dos gols no dicionário

print("=-" * 30)
print(jogador) #vai exibir o dicionário com todos os dados do jogador
print (partidas) #vai exibir a lista  com os gols 
print("=-" * 30)

for k, v in jogador.items(): #para cada chave e valor no dicionário, irá imprimir
    print(f"O campo {k} tem valor {v}") 
print("=-" * 30)

print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas e fez {jogador ['total']} gols")

for c in range(0, jogador['partidas']): #para cada partida jogada, irá imprimir o número de gols feitos
    print(f" => Na partida {c + 1}, fez {jogador['gols'][c]} gols") #mostra os gols por partida usando a lista

