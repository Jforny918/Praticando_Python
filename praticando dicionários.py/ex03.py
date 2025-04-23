from datetime import date

# Coleta das informações
info = {}
info['nome'] = str(input('Nome: '))
info['genero'] = str(input('Gênero (F/M): '))
info['ano_nascimento'] = int(input('Ano de Nascimento: '))
info['carteira'] = int(input('Carteira de Trabalho (Digite 0 caso não tenha): '))

# Se a pessoa tiver carteira, pede os dados adicionais
if info['carteira'] != 0:
    info['contratacao'] = int(input('Ano de Contratação: '))
    info['salario'] = float(input('Salário: R$ '))

# Ano atual e idade
ano_atual = date.today().year
idade = ano_atual - info['ano_nascimento']

# Função para verificar aposentadoria
def pode_aposentar(idade, ano_contratacao, genero):
    #def é a função que irá definir se pode ou não aposentar
    tempo_contribuicao = ano_atual - ano_contratacao #calcula quantos anos a pessoa já contribuiu 
    #desde o ano da contratação

    #define os requisitos para cada gênero
    if genero.lower() in ['m', 'masculino', 'homem']:
    #se o genero for masculino, a idade mínima é 65 e a contribição mínima é 35
        idade_minima = 65
        contribuicao_minima = 35
    elif genero.lower() in ['f', 'feminino', 'mulher']:
    #se o gênero for feminino, a idade mínima é 62 e a contribuição mínima é 30
        idade_minima = 62
        contribuicao_minima = 30
    else:
        #se não for nenhum dos dois gêneros informado, irá imprimir a mensagem abaixo
        return "Gênero inválido. Use 'M' ou 'F'."

    falta_idade = max(0, idade_minima - idade)
    #calculo para dizer quanto tempo ainda falta para se aposentar de acordo com a idade mínima
    falta_contribuicao = max(0, contribuicao_minima - tempo_contribuicao)
    #calculo para dizer quanto tempo ainda falta para se aposentar de acordo com a contribuição mínima
    #max garante que nunca apareça um valor negativo como resultado

    if idade >= idade_minima or tempo_contribuicao >= contribuicao_minima:
    #se os requisitos para se aposentar forem todos verdadeiros, irá imprimir a mensagem abaixo
        
        return f"Pode se aposentar!\nIdade: {idade} anos\nTempo de contribuição: {tempo_contribuicao} anos"

    else:
        return (
            f"Ainda não pode se aposentar.\n"
            
            f"Idade: {idade} anos (faltam {falta_idade} anos)\n"
            
            f"Contribuição: {tempo_contribuicao} anos (faltam {falta_contribuicao} anos)\n"
           
            f"A aposentadoria poderá acontecer em no máximo {min(falta_idade, falta_contribuicao)} anos.\n"
            
        )

# Exibição
print(f"{info['nome']} tem {idade} anos.")

if info['carteira'] != 0:
    print(f"A CTPS informada é {info['carteira']}\n")
    
    print(f"{info['nome']} foi contratado(a) em {info['contratacao']}\n")
    
    print(f"O salário é de R$ {info['salario']:.2f}\n")
   
    print(pode_aposentar(idade, info['contratacao'], info['genero']))
    
else:
    
    print("Sem carteira de trabalho. Não é possível calcular aposentadoria.")
   
