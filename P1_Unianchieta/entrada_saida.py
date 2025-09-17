nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))

print(f"\nOlá {nome}, você tem {idade} anos e mede {altura:.2f} metros de altura.")
print(f"O dobro da sua idade é {idade * 2}.")

resposta = idade >= 18
print("Maior de idade?", resposta)
