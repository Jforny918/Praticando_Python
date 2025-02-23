print ('Exercício 01 - Analisando um nome qualquer') #analisando um nome
n1=str(input('Digite o seu nome: ')).strip() #strip elimina os espaços em branco antes e depois do nome
#n1=n1.strip() #outra forma de eliminar os espaços em branco
print ('Analisando seu nome...')
print ('seu nome em maiúsculas é {}'.format(n1.upper())) #usamos () para chamar a função upper
print ('Seu nome em minúsculas é {}'.format(n1.lower()))
print ('Seu nome tem ao todo {} letras'.format(len(n1)-n1.count(' ')))
print ('Seu primeiro nome tem {} letras'.format(n1.find(' '))) #o (' ') indica que a contagem de letras é até o primeiro espaço
