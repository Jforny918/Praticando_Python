
times = ('Fortaleza', 'Juventude', 'Vasco', 'Cruzeiro', 'Grêmio',
         'Red Bull Bragantino', 'Ceará', 'Corinthians', 'Flamengo',
         'Internacional','Bahia', 'São Paulo', 'Sport', 'Botafogo', 
         'Palmeiras', 'Atlético - MG', 'Santos', 'Mirassol', 'Fluminense',
         'Vitória')
#times é a tupla dos times do Brasileirão 2025
print ('=-'*30)
print (f'Lista de Times Do Brasileirão 2025: {times}')
print ('=-'*30)
print (f'Os primeiros 5 times são: {times[0:5]}') #vai exibir os valores de 0 até 5 (não inclui o 5)
print ('=-'*30)
print (f'Os últimos 4 times são: {times[-4:]}') #vai exibir os últimos 4 valores da tupla
print ('=-'*30)
print (f'Os times em ordem alfabética são: {sorted(times)}') #vai colocar os nomes da tupla em ordem alfabética
print ('=-'*30)
print (f'O Botafogo está na posição {times.index('Botafogo')+1}') #vai exibir a posição em que a chapecoense está na tupla
#o +1 è para adicionar mais 1 na posição, porque a contagem começa do 0.
print ('=-'*30)
