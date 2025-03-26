print('=-' * 30)
print('CADASTRE UMA PESSOA')
print('=-' * 30)

total18 = homem = mulher20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [F/M] ').strip().upper()[0]
    
    if idade > 18:
        total18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1

    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    if r == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todo temos {homem} homem(s) cadastrados')
print(f'E temos {mulher20} mulher(es) com menos de 20 anos.')

        
    
    