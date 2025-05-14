
galera = list ()
soma = media = 0

while (True):
    pessoa = dict()
    pessoa.clear() #limpa o dicionário para não acumular dados
    pessoa ['nome'] = input ('Nome: ')

    while (True):
        pessoa ['sexo'] = input ('Sexo [M/F]: ').upper()[0]
        if pessoa ['sexo'] in 'MF':
            break
        print ('ERRO! Digite apenas M ou F.')

    pessoa ['idade'] = int(input ('Idade: '))
    soma += pessoa ['idade']
    galera.append(pessoa.copy()) #adiciona o dicionário com os dados da pessoa na lista galera

    while (True):
        resp = input ('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print ('ERRO! Digite apenas S ou N.')

    if resp == 'N':
        break

print ('=-'*30)
print (galera)

print(f'A) Ao todos temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print (f'B) A média de idade de {media:5.2f} anos.')
print ("C) As mulheres cadastradas foram: ", end = '')
for p in galera:
    if p ['sexo'] in 'F':
        print (f'{p["nome"]} | ', end = '') 

print (f'\nD) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print ('   ')
        for k, v in p.items():
            print (f'{k} = {v}; ',end = '')
        print ()
        
print ('<< ENCERRADO >>')




