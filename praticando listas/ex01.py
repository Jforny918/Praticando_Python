num = [2, 5, 9, 1]
num[2] = 3  # substituindo o valor na posição 2 da lista por 3
num.append(7)  # adicionando o valor 7 a lista
num.sort(reverse=True)  # ordenando a lista em ordem decrescente
num.insert(4, 2)  # adicionando o valor 2 na posição 4 da lista
# num.insert(2,0) #adicionando o valor 0 na posição 2 da lista
# num.pop (2) #removendo o valor na posição 2 da lista
if 5 in num:  # verificando se o valor 5 está na lista
    num.remove(5)  # removendo o 5 da lista
else:
    print('Não encontrei o valor 5!')
print(num)
print(f'Essa lista tem {len(num)} elementos!')  # mostrando o tamanho da lista
