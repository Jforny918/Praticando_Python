from time import sleep
alunos = []
dados = []

while True:
    nome = input('Nome: ').strip().title()  
    #o title() deixa a primeira letra de cada palavra em maiúscula e o strip() remove os espaços em branco no início e no fim da string
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))        
    media = (nota1 + nota2) / 2             
    dados.append([nome, nota1, nota2, media])
    alunos.append(nome)
    
    resp = input('Deseja continuar? [S/N]: ').strip().upper()  
    if resp == 'N':
        break

print('-' * 40)
print('Nº  NOME       MÉDIA')
print('-' * 40)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')   
    #i:<4} formata o índice com 4 espaços à esquerda'
    #{a[0]:<10} formata o nome com 10 espaços à esquerda
    #{a[3]:>8.1f} formata a média com 8 espaços à direita e 1 casa decimal
print('-' * 40)
print('<< ENCERRADO >>')
print('-' * 40)
print('ALUNOS CADASTRADOS')
print('-' * 40)

for nome in alunos: 
    #para cada nome em alunos escreva o nome de cada um nos alunos cadastrados
    print(nome)
print('-' * 40)
print('NOTAS DOS ALUNOS')
print('-' * 40)
exibir = int (input ('Mostar notas de qual aluno? (999 para sair): '))
while exibir != 999:
    if exibir >= len(dados) or exibir < 0:
    #se o número digitado da posição do aluno não existir na lista, ele vai imprimir a mensagema abaixo
        print('Aluno não encontrado!')
    else:
        print(f'Notas de {dados[exibir][0]}: {dados[exibir][1]}, {dados[exibir][2]}')
        #se o número digitado existir, ele vai imprimir o nome e as notas do respectivo aluno
        #{dados[exibir][0]} é o nome do aluno, {dados[exibir][1]} e {dados[exibir][2]} são as notas
    exibir = int (input ('Mostar notas de qual aluno? (999 para sair): '))
print('FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')


