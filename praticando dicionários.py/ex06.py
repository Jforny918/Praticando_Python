jogador = dict()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome de Jogador: "))
    jogador['partidas'] = int(input(f"Número de partidas que {jogador['nome']} jogou: "))
    jogador['gols'] = []

    for c in range(jogador['partidas']):
        gols = int(input(f"  Número de gols que {jogador['nome']} fez na partida {c + 1}: "))
        jogador['gols'].append(gols)

    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())

    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')

    if resp == 'N':
        break

print('-' * 40)
print(f'{"Cod":<4}{"Nome":<15}{"Gols":<20}{"Total":<6}')
print('-' * 40)
for i, j in enumerate(time):
    print(f'{i:<4}{j["nome"]:<15}{str(j["gols"]):<20}{j["total"]:<6}')
print('-'*40)
while (True):
    busca = int (input ('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        print ("ENCERRANDO...")
        break
    if busca >= len(time):
        print (f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print (f'Levantamento do jogador {time[busca]['nome']}: ')
        for i, g in enumerate(time[busca]['gols']):
            print (f'No jogo {i + 1} fez {g} gols')
    

