v1= int (input ("Digite o primeiro valor: "))
v2 = int (input ("Digite o segundo valor: "))
opcao = 0
while opcao != 6:
    print ("[1] Somar")
    print ("[2] Multiplicar")
    print ("[3] Dividir ")
    print ("[4] Maior ")
    print ("[5] Menor ")
    print ("[6] Sair do programa")
    opcao = int (input ("Qual é a sua opção? "))
    if opcao == 1:
        soma = v1 + v2
        print (" A soma entre {} e {} é igual a {}".format (v1, v2, soma))
    elif opcao == 2:
        multiplicação = v1 * v2
        print ("A multiplicação entre {} e {} é igual a {}".format (v1, v2, multiplicação))
    elif opcao == 3:
        divisão = v1 / v2
        print ("A divisão entre {} e {} é igual a {:.2f}".format (v1, v2, divisão))
    elif opcao == 4:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print ("Entre {} e {} o maior valor é {}".format (v2, v2, maior))
    elif opcao == 5:
        if v1 < v2:
            menor = v1
        else:
            menor = v2
        print ("Entre {} e {} o menor valor é {}".format (v1, v2, menor))
    elif opcao == 6:
        print ("Finalizando o programa...")
    else:
        print ("Opção inválida. Tente novamente!")
print ("Fim do programa! Volte sempre!")