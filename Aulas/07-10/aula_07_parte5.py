email = "paulo.marino@anchieta.br"
usuario = email[:email.find('@')]
dominio = email[email.find('@')+1:]
print(usuario)
print(dominio)
