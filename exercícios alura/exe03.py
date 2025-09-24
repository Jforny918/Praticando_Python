cpf_usuario = input ("Digite o seu CPF (somente números): ")
if len(cpf_usuario) == 11 and cpf_usuario.isdigit():
    print("CPF válido.")
elif len(cpf_usuario) != 11:
    print("CPF inválido. O CPF deve conter 11 dígitos.")
else:
    print("CPF inválido. O CPF deve conter apenas números.")

