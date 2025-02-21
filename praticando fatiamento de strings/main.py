#fatiamento de strings

#frase = 'Curso em Vídeo Python'
#frase[9] #retorna o caractere na posição 9, que é o V
#frase[9:13] #retorna os caracteres da posição 9 até a posição 12, que é Víde
#frase[9:21:2] #retorna os caracteres da posição 9 até a posição 20, pulando de 2 em 2, que é VdoPto
#frase[:5] #retorna os caracteres da posição 0 até a posição 4, que é Curso
#frase[15:] #retorna os caracteres da posição 15 até o final, que é Python
#frase[9::3] #retorna os caracteres da posição 9 até o final, pulando de 3 em 3, que é VPh

#tamanho da string

#len(frase) #retorna o tamanho da string, que é 21
#contagem de caracteres
#frase.count('o') #conta quantas vezes a letra o aparece na string, que é 3
#frase.count('o',0,13) #conta quantas vezes a letra o aparece na string, do início até a posição 12, que é 1
#encontrar a posição de um caractere
#frase.find('deo') #retorna a posição onde a string deo começa, que é 11
#frase.find('Android') #retorna -1, pois a string Android não foi encontrada
#verificar se uma string contém outra
#'Curso' in frase #retorna True, pois a string Curso está contida em frase

#transformação

#frase.replace('Python','Android') #substitui a string Python por Android, que é Curso em Vídeo Android
#frase.upper() #transforma todos os caracteres em maiúsculos, que é CURSO EM VÍDEO PYTHON
#frase.lower() #transforma todos os caracteres em minúsculos, que é curso em vídeo python
#frase.capitalize() #transforma o primeiro caractere em maiúsculo e os demais em minúsculos, que é Curso em vídeo python
#frase.title() #transforma o primeiro caractere de cada palavra em maiúsculo e os demais em minúsculos, que é Curso Em Vídeo Python
#frase.strip() #remove os espaços em branco no início e no final da string, que é Curso em Vídeo Python
#frase.rstrip() #remove os espaços em branco à direita da string, que é Curso em Vídeo Python
#frase.lstrip() #remove os espaços em branco à esquerda da string, que é Curso em Vídeo Python

#divisão

#frase.split() #divide a string em uma lista de palavras, que é ['Curso', 'em', 'Vídeo', 'Python']

#junção

#'-'.join(frase) #junta as palavras da lista com o caractere -, que é C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n


