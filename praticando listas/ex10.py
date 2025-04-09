expressao = input ('Digite uma expressão algébrica: ')
pilha = []
for simb in expressao: #verifica se o símbolo é um parêntese
    if simb == '(': #se o símbolo for um parentese aberto, adiciona na pilha
        pilha.append('(') #adiciona na pilha
    elif simb == ')': #senao for parentese aberto e sim fechado, então ele remove o último elemento da pilhA
        if len(pilha) > 0: #verifica se a pilha não está vazia
            pilha.pop() #remove o último elemento da pilha
        else: #se a pilha estiver vazia, adiciona o parentese fechado na pilha
            pilha.append(')')
            break
if len(pilha) == 0:
    print ('A expressão está correta!')
else:
    print ('A expressão está incorreta!')