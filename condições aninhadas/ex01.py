print ('Prática da aula 012')
print ()
nome=input('Qual é o seu nome? ')
if nome == 'Júlia':
    print ('Seu nome é tão lindo!')
elif nome == 'Pedro' or nome == 'Bruno' or nome == 'Cláudia':
    print ('O seu nome é bem popular no Brasil!')
elif nome in 'Juliana Ana Elaine Luiza Jennifer':
    print ('Belo nome feminino!')
elif nome == 'João Lucas José Cláudio Vinicius Mateus Matheus Mario':
    print ('Belo nome masculino!')
else:
    print ('Seu nome é bem comum')
    print ('Tenha um ótimo dia, {}'.format(nome))

