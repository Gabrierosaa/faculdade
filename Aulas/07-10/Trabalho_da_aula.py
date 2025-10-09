emailvalido = False
telefonevalido = False
nome = input("Entre com seu nome: ").strip().lower().title()
email = input("Entre com seu email: ").strip().lower()
telefone_input = input("Entre com o seu telefone (apenas 11 dígitos): ")
numero = ''.join(filter(str.isdigit, telefone_input)) 
senha = input("Entre com sua senha: ").strip()
if '@' in email and '.' in email:   
    if email.find('@') > 0 and email.find('@') < email.find('.'): 
        emailvalido = True
if len(numero) == 11:
    telefonevalido = True
else:
    telefonevalido = False
if emailvalido and telefonevalido:   
    dd = numero[0:2]
    parte1 = numero[2:7] 
    parte2 = numero[7:11] 
    print("\n Cadastro Validado com Sucesso!")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Telefone: ({dd}) {parte1}-{parte2}")
else:
    print("\n Ops, algum erro foi encontrado:")
    if not emailvalido:
        print(" - Email inválido ou no formato incorreto.")
    if not telefonevalido:
        print(" - Telefone inválido (deve ter 11 dígitos).")