#relembrando como declaramos cada uma
#para tuplas usamos ()
#para lista usamos []
#para dicionários usamos {}

#dados = dict ()
#dados = {'nome':'Pedro', 'idade':'25'}
#print(dados['nome']) vai imprimir o nome pedro
#print(dados['idade']) vai imprimir 25
#exibição com´leta no terminar vai ficar assim: Pedro 25

#no dicionário não é possível usar append, então para adicionar um novo elememto usamos o seguinte:
#dados['sexo']='M' adicionando o sexo M ao dicionário
#print(dados) vai imprimir {'nome':'Pedro', 'idade':'25', 'sexo':'M'}

#caso eu queira substituir um valor, por exemplo um nome, eu uso:
#del dados['nome'] #deletando o nome do dicionário
#dados['nome']='Maria' #adicionando o nome Maria ao dicionário
#print(dados) vai imprimir {'nome':'Maria', 'idade':'25', 'sexo':'M'}

#vou criar um dicionário para guardar nomes de filmes
#filme = {'título': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}

#print (filme.vaues()) imprime todos os valores do dicionário, ou seja, o que está dentro de 
#título, ano e diretor
#print (filme.keys()) imprime todas as chaves do dicionário, ou seja, título, ano e diretor
#print (filme.items()) imprime todos os itens do dicionário, ou seja, título, ano e diretor e seus respectivos valores

#exemplo:

#for k, v in filme.itens():
#    print(f'O {k} é {v}')
# O k vai ser a chave (key) e o v vai ser o valor (value)
# o resultado vai ser:
#O título é Star Wars
#O ano é 1977
#O diretor é George Lucas

#podemos juntar listas, tuplas e dicionários
#por exemplo:
#brasil = []
#estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
#estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
#estado3 = {'UF': 'Minas Gerais', Sigla': 'MG'}
#brasil.append(estado1) adicionando o estado1 ao brasil
#brasil.append(estado2) adicionando o estado2 ao brasil
#brasil.append(estado3) adicionando o estado3 ao brasil
#for e in brasil: #cada estado dentro da lista brasil ele vai exibir o que está sinalizado abaixo
#    print(f'A sigla do estado {e["UF"]} é {e["Sigla"]}') 

#listas são identificadas por números e dicionários são identificados por chaves (nomes da chave)