from datetime import date
def voto (idade):
    if idade < 16:
        return f'Você tem {idade} anos. NÃO VOTA!'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Você tem {idade} anos. VOTO OPCIONAL!'
    else:
        return f'Você tem {idade} anos. VOTO OBRIGATÓRIO!'
    
#programa principal
ano = int (input ('Em que ano você nasceu? ')) #interação com o usuário
ano_atual = date.today().year #obtendo o ano atual
idade = ano_atual - ano #cálculo da idade
resultado = voto (idade) #chamando a função voto e passando idade como parâmetro
print (resultado) #exibindo o resultado 
