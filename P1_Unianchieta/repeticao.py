tabuada = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    print(f"{tabuada} x {i} = {tabuada * i}")

senha = input("Escolha sua senha")
senhareal = input("Digite a sua senha")
tentativa = 3
while senha != senhareal:
    print("Senha incorreta, tente novamente")
    senhareal = input("Digite a sua senha")
    tentativa -= 1
    if tentativa == 0:
        print("Número de tentativas excedido")
        break

