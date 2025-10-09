texto = "Python É Incrivel"

print(texto.upper())#deixa em caixa alta
print(texto.lower())#deixa em caixa baixa
print(texto.title())#deixa as primeiras letra maiusculas
print(texto.capitalize())# deixa a primeira letra maiuscula
print(texto.isupper())#false
print(texto.islower())#false
print(texto.istitle())#true
print(texto.swapcase())#tudo que é maiuscula vira minuscula e vice versa

texto_espaco = "   Ola.classe!    "
print(texto_espaco.strip())#remove os espaços
print(texto_espaco.lstrip())#remove só da esquerda
print(texto_espaco.rstrip())#remove só da direita
print(texto_espaco.strip(" .!"))#remove tudo que tiver .!

nome_usuario = input("Digite seu nome: ").strip().title()
print(nome_usuario)

texto1 = "Python é uma linguagem de programação"
posicao = texto1.find("linguagem") #mostrou aonde esta a primeira letra da palavra
print(posicao)
novo_texto = texto1.replace("python", __new="java")#troca uma palavra
print(novo_texto)
palavras = texto1.split()# faz listas para palavras
print(palavras)

frase = " ".join(palavras)# junta as listas
print(frase)
