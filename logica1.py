#Crie um programa que leia uma lista de números inteiros e realize as seguintes tarefas:
#Calcule a soma de todos os números.[✅]
#Encontre o maior número da lista.[✅]
#Encontre o menor número da lista.[✅]
#Calcule a média dos números.[✅]
#O programa deve:
#Solicitar ao usuário a quantidade de números que ele deseja inserir na lista.[✅]
#Solicitar os números inteiros um por um.[✅]
#Exibir a soma, o maior número, o menor número e a média dos números inseridos.[✅]
#Dicas:
#Você pode usar listas em Python para armazenar os números.
#Use funções como max(), min() e sum() para facilitar as operações.
#A média pode ser calculada dividindo a soma dos números pela quantidade de números.

lista = []
escolha = int(input('Quantos numeros deseja inserir ? :'))
i = int(0)


while(i != escolha):
    i = i + 1 
    n = int(input('Entre com o numero: '))
    lista.append(n)
       
def max():
    lista.sort(reverse = True)
    print('Maior numero: ' , lista[0])

def min():
    lista.sort(reverse = False)
    print('Menor numero: ' , lista[0])

def med():
    soma = sum(lista)
    medi = soma/escolha
    print('a soma dos numeros:' , soma)
    print('a media dos numeros: ' , medi) 


print(lista)
max()
min()
med()
