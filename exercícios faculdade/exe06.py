from datetime import datetime
agora = datetime.now()
ano_inteiro = agora.year
print (f"O ano inteiro é {ano_inteiro}")
ano_string = agora.strftime('%Y')
print (f"O ano em string é {ano_string}")
y = ano_inteiro - 60
print (f"O ano com 60 anos a menos é {y}")