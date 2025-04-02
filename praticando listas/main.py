lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
#listas são representados por [] e tuplas por ()
#listas são mutáveis, logo podemos substituir valores
lanche [3] = 'Picolé' #substituindo o 'Pudim' por 'Picolé'
print (lanche)
lanche.append('Batata frita') #adicionando 'Batata frita' na lista
lanche.insert (0, 'Cachorro quente') #adicionando o 'Cachorro quente' na poisçõa 0 na lista
#atente- se que ao adicionar o 'Chachorro quente' na posição 0, o 'Hamburguer' foi para
#a posição 1 e assim por diante.
print (lanche)
lanche.remove('Pizza') #removendo um item da lista pelo índice dele, ou seja, o nome do item.
del lanche [3] #eliminando o item da posição inserida dentro do []
lanche.pop(3) #remove o valor na posição que você inserir dentro dos parenteses
#caso esteja vazio () serve para eliminar o último elemento/item da lista - uso mais comum do pop
print (lanche)

valores = list(range(4,11)) #cria uma lista com os valores de 4 até 10 
valores.sort() #ordena a lista em ordem crescente
valores.sort(reverse= True) #ordena a lista em ordem descrescente
len (valores) #mostra o tamanho da lista, ou seja, quantos itens tem dentro dela
print (valores)