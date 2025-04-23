
pessoas = {'nome': 'Julia', 'idade': '21', 'sexo': 'F'}
print (F'A {pessoas['nome']} tem {pessoas['idade']} e é do sexo {pessoas['sexo']}')
pessoas['peso'] = 65.7 
for k, v in pessoas.items(): #pessoas.items() retorna uma lista de tuplas, onde cada tupla
#contém uma chave e um valor do dicionário
#adicionando o peso ao dicionário pessoas
    print (f'{k} = {v}') #k é a chave e v é o valor