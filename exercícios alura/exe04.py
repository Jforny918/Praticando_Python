texto = input("Digite um texto: ")

print ("O texto digitado possui {} vogais.".format(len([letra for letra in texto if letra.lower() in 'aeiouáéíóúãõâêîôûàèìòù'])))