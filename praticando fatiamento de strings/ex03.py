print ('Exercício 3 - Verificando as primeiras letras de um texto')
cid = str(input('Em que cidade você nasceu? ')).strip() #strip elimina os espaços 
print (cid[:5].upper() == 'SANTO') #usamos o upper para jogar tudo para maiúsculo e na hora de testar ele verifica se tem essa palavra ou não.