#Crie um programa que recebe uma lista de números inteiros e realiza as seguintes operações:
#Remova os números duplicados da lista, mantendo apenas a primeira ocorrência de cada número.[✅]
#Ordene a lista em ordem crescente. [✅]
#Calcule a soma de todos os elementos.[✅]
#Retorne a lista modificada e a soma dos números. [✅]

numero = []
resposta = input("Vamos começar? (S/N) ")

while resposta.lower() == 's':  # Aceita 's' ou 'S'
    n1 = int(input('Entre com o seu número: '))
    numero.append(n1)  # Adiciona o número diretamente à lista
    resposta = input("Deseja adicionar outro número? (S/N) ")

# Removendo duplicatas mantendo a ordem
numero = list(dict.fromkeys(numero))

# Ordenando a lista
numero.sort()

# Calculando a soma dos elementos
soma = sum(numero)

# Exibindo os resultados
print(f"Lista final: {numero}")
print(f"Soma dos elementos: {soma}")
