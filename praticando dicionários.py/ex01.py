boletim = {}
boletim ['nome']= str(input('Nome: '))
boletim ['media'] = float( input('Média: '))

print (f'O aluno {boletim['nome']} ficou com média {boletim['media']}')
for k, v in boletim.items():
    print (f'{k} = {v}')

if boletim ['media'] >= 7:
    print ('A situação é de APROVADA')
else: 
    print ('A situação é de REPROVADA')

