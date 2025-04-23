from random import randint
from time import sleep

jogo = {}
num_jogadores = 4  # Número de jogadores

# Loop para capturar os nomes de cada jogador
for c in range(num_jogadores):
    nome = input(f'Nome do Jogador Número {c + 1}: ')  # Solicita o nome do jogador
    jogo[f'Jogador {c + 1}'] = {'nome': nome, 'dado': 0}  # Armazena o nome e o valor do dado
    #a cada respectivo jogador informado

print('=' * 30)
print('SEJAM BEM-VINDOS AO JOGO!')
print('=' * 30)

# Loop para cada jogador lançar o dado
for c in range(num_jogadores):
    print(f'É a vez de {jogo[f"Jogador {c + 1}"]["nome"]} lançar o dado...') #mostra o nome do jogador que irá lançar
    #o dado por ordem
    sleep(1)  # Pausa para dar um efeito de espera
    dado = randint(1, 6)  # Lança o dado (número aleatório de 1 a 6)
    jogo[f'Jogador {c + 1}']['dado'] = dado  # Armazena o valor do dado no dicionário
    print(f'{jogo[f"Jogador {c + 1}"]["nome"]} tirou {dado}!\n') #infroma o valor tirado no dado pelo respectivo jogador
    sleep(1)  # Pausa para dar um efeito de espera

# Exibir os resultados
print('=' * 30)
print('Resultados dos Lançamentos:')
maior_valor = 0
vencedor = ''

for jogador, info in jogo.items():
    print(f'{info["nome"]} tirou {info["dado"]}')
    if info["dado"] > maior_valor:
        maior_valor = info["dado"]
        vencedor = info["nome"]

# Exibir quem tirou o maior valor
print('=' * 30)
print(f'O maior valor foi {maior_valor}, tirado por {vencedor}!')

 