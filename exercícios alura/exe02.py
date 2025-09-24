valor_conta = float (input ("Digite o valor da conta: "))
gorjeta_indicada = valor_conta * 0.10
resposta_gorjeta = input("O valor da gorjeta indicada é de: R$ {:.2f}, deseja pagar? [S/N] ".format(gorjeta_indicada)).upper()

if resposta_gorjeta == "S":
    print("1- Pagar a conta com a gorjeta indicada")
    print("2- Pagar a conta com outra gorjeta")
    
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        total = valor_conta + gorjeta_indicada
        print("O valor total da conta com a gorjeta é de: R$ {:.2f}".format(total))
    elif escolha == 2:
        outra_gorjeta = float(input("Digite o valor da gorjeta que deseja pagar: R$ "))
        total = valor_conta + outra_gorjeta
        print("O valor total da conta com a gorjeta é de: R$ {:.2f}".format(total))
    else:
        print("Opção inválida. A gorjeta não será adicionada.")
        print("O valor total da conta é de: R$ {:.2f}".format(valor_conta))

else:
    print("Você optou por não pagar a gorjeta.")
    print("O valor total da conta é de: R$ {:.2f}".format(valor_conta))

print("Obrigado pela preferência! Volte sempre!")
