a1 = int (input ('Digite o primeiro termo da PA: ')) 
#Pede ao usuário para inserir o primeiro termo da PA
print ('=-=' * 10) 
#imprime 10 vezes o sinal de igual para deixar o programa mais bonito
r = int (input ('Digite a razão da PA: ')) 
#Pede ao usuário que digite a razão da PA
n = int (input ("Digite o número de termos que deseja mostrar: ")) 
#Pede ao usuário que digite o número de termos que deseja mostrar
cont = 1 
#Incializa o contador com o valor 1
termo = a1 
#Inicializa o termo com o valor de a1
while cont <= n: 
    #enquanto o contador for menor ou igual ao número de termos que deseja mostrar, ele irá imprimir o termo e incrementar o termo com a razão
    print ('{} -> '.format (termo), end='') 
    #imprime o termo e não pula linha
    cont+= 1 
    #contador incrementa 1 a cada laço
    termo += r 
    #termo incrementa a razão a cada laço
print ('FIM') 
#Imprime FIM