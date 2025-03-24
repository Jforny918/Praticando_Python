a1 = int (input ('Digite o primeiro termo da PA: '))
r = int (input ('Digite a razão da PA: '))
cont = 1
termo = a1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total: 
        print ('{} -> '.format (termo), end='')
        termo += r
        cont += 1
    print ('PAUSA')
    mais = int (input ('Quantos termos você quer mostrar a mais? '))
print ('Progressão finalizada com {} termos mostrados'.format (total))
#O programa é um gerador de PA, onde o usuário insere o primeiro termo e a razão da PA.
#Depois o programa solicita ao usuário quantos termos ele deseja mostrar.
#Depois ele imprime a PA e pergunta ao usuário quantos termos ele deseja mostrar a mais.
#Caso o usuário digite 0, o programa finaliza.
