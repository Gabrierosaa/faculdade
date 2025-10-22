#a função len() vai contar quantos caracteres tem, não importa se é numero ou letra . se é int float ou string

emailvalido = False
telefonevalido = False
senhavalida = False
nome = input("Entre com seu nome: ").strip().title()
email = input("Entre com seu email: ").strip().lower()
telefone_input = input("Entre com o seu telefone (apenas 11 dígitos): ")
numero = ''.join(filter(str.isdigit, telefone_input)) 
senha = input("Entre com sua senha: ").strip()

if '@' in email and '.' in email:
    if email.find('@') > 0 and email.find('@') < email.find('.'): 
        emailvalido = True

if len(numero) == 11:
    telefonevalido = True

if len(senha) >= 6:
    senhavalida = True
print("\n" + "=" * 40)
print("RELATÓRIO DE CADASTRO")
print("=" * 40)
print(f"Nome: {nome}")
print(f"Email: {email} (Status: {'Válido' if emailvalido else 'Inválido - Formato incorreto'})")
if telefonevalido:
    dd = numero[0:2]
    parte1 = numero[2:7] 
    parte2 = numero[7:11] 
    print(f"Telefone: ({dd}) {parte1}-{parte2} (Status: Válido)")
else:
    print(f"Telefone: {telefone_input} (Status: Inválido - Deve ter 11 dígitos)")
    print(f"Senha: {'Válida' if senhavalida else 'Inválida - Pelo menos 6 caracteres'} (Não exibida por segurança)")
if emailvalido and telefonevalido and senhavalida:
    print("\nCadastro Validado com Sucesso!")
else:
    print("\nOps, algum erro foi encontrado nos dados:")
    if not emailvalido:
        print(" - Email inválido ou no formato incorreto.")
    if not telefonevalido:
        print(" - Telefone inválido (deve ter 11 dígitos).")
    if not senhavalida:
        print(" - Senha inválida (deve ter pelo menos 6 caracteres).")
print("=" * 40)