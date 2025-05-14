
galera = list () #gerando uma lista vazia 
soma = media = 0 #as variáveis soma e média inicializadas com 0

while (True): #enquanto for verdadeiro, o loop irá rodar os seguintes comandos
    pessoa = dict()
    pessoa.clear() #limpa o dicionário para não acumular dados
    pessoa ['nome'] = input ('Nome: ') #armazenando o nome da pessoa no dicionário

    while (True): #enuqnato for verdadeiro, o loop irá rodar os seguintes comandos 
        pessoa ['sexo'] = input ('Sexo [M/F]: ').upper()[0] #armazenando o sexo da pessoa no dicionário
        if pessoa ['sexo'] in 'MF': #se sexo estiver em M ou F, o loop irá parar
            #se não, o loop irá continuar rodando
            break
        print ('ERRO! Digite apenas M ou F.') #se o sexo não for M ou F, irá imprimir a mensagem de erro

    pessoa ['idade'] = int(input ('Idade: ')) #armazenando a idade da pessoa no dicionário
    soma += pessoa ['idade'] #a cada iteração, a idade da pessoa é adicionada a soma
    #soma = soma + pessoa ['idade'] #outra forma de fazer a soma
    galera.append(pessoa.copy()) #adiciona o dicionário com os dados da pessoa na lista galera

    while (True): #enquanto for verdadeiro, o loop irá rodar os seguintes comandos
        resp = input ('Quer continuar? [S/N] ').upper()[0] #pergunta se o usuário quer continuar
        if resp in 'SN': #se a resposta for S ou N, o loop irá parar
            #se não, o loop irá continuar rodando
            break
        print ('ERRO! Digite apenas S ou N.') #se a resposta não estiver em S ou N, irá imprimir a mensagem de erro

    if resp == 'N': #se a resposta for N, o loop parará
        break

print ('=-'*30)
print (galera) #exibe a lista galera com todos os dados cadastrados de cada pessoa

print(f'A) Ao todos temos {len(galera)} pessoas cadastradas.') #o len() conta quantos elementos tem na lista galera
media = soma / len(galera) #cálculo da média de idade
print (f'B) A média de idade de {media:5.2f} anos.')
print ("C) As mulheres cadastradas foram: ", end = '')
for p in galera: #para cada pessoa na lista galera, o loop irá rodar os seguintes comandos
    if p ['sexo'] in 'F': #se o sexo da pessoa for F, o loop irá printar o nome dela
        print (f'{p["nome"]} | ', end = '') 

print (f'\nD) Lista de pessoas que estão acima da média: ')
for p in galera: #para cada pessoa na lista galera, o loop irá verificar se a idade está acima da média
    if p['idade'] >= media:
        print ('   ')
        for k, v in p.items():
            print (f'{k} = {v}; ',end = '')
        print ()
        
print ('<< ENCERRADO >>')




