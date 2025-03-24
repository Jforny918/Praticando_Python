a1 = int (input ('Digite o primeiro termo da PA: ')) 
#Pede ao usuário para inserir o primeiro termo da PA
print ('=-=' * 10) 
#imprime 10 vezes o sinal de igual para deixar o programa mais bonito
r = int (input ('Digite a razão da PA: ')) 
#Pede ao usuário que digite a razão da PA
cont = 1 
#Incializa o contador com o valor 1
termo = a1 
#Inicializa o termo com o valor de a1
while cont <= 10: 
    #Enquanto o contador for menor ou igual a 10, ele irá imprimir o termo e incrementar o termo com a razão
    print ('{} -> '.format (termo), end='') 
    cont+= 1
    termo += r
print ('FIM') 
#Imprime FIM
#O programa solicita ao usuário o primeiro termo da PA e a razão da PA, depois ele imprime os 10 primeiros termos da PA
#o print ('{} -> '.format (termo), end='') serve para imprimir o termo e não pular linha 
#Vai ocorrer que vai ser inserido o a1, que é o primeiro termo.
#Depois vai ser inserido ao termo a razão, que é o r.
#e isso vai ocorrer até o contador ser menor ou igual a 10, pois foi a quantidade de termos que foi solicitado.
#Depois ele vai imprimir FIM.
#O programa é um gerador de PA.