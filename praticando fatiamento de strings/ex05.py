print('Exercício 5 - primeira e última ocorrência de uma string')
var_strFrase = (input('Digite uma frase: '))
var_strFrase = var_strFrase.replace(' ', '').replace(
    'á', 'a').replace('ã', 'a').replace('â', 'a').replace('à', 'a')
var_strFrase = var_strFrase.upper()
print('A letra A aparece {} vezes na frase.'.format(var_strFrase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(
    var_strFrase.find('A') + 1))
print('A última letra A apareceu na posição {}'.format(var_strFrase.rfind('A')+1))
# usamos o replace (' ', '') para eliminar os espaços entre as palavras
#usamos o replace para substituir tal letra por outra 
