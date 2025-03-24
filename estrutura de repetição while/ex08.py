print ('='*30)
print ('Sequência de Fibonacci')
print ('='*30)
n = int (input ("Quantos termos você quer mostrar? "))
#Pede ao usuário que digite quantos termos ele deseja mostrar
t1 = 0 
#o primeiro termo é sempre 0
t2 = 1 
#o segundo termo é sempre 1
t3 = t1 + t2
#o terceiro termo é a soma dos dois primeiros termos e assim consecutivamente
cont = 3 
#contador inicializa em 3 pois já mostrei o primeiro e segundo termo
print ('{} -> {} -> '.format (t1, t2), end='') 
#vai exibir o t1 e t2 sempre antes de iniciar a sequência
while cont <= n: 
    #enquanto o contador for menor ou igual ao número que o usuário digitou, ele vai executar o bloco de comandos abaixo
    print ('{} -> '.format (t3), end='')
    t1 = t2 #t1 passa a ser  t2, depois passa a ser o t3...
    t2 = t3 #t2 passa a ser t3, depois passa a ser o t4...
    t3 = t1 + t2 
    cont += 1
print ('FIM')

