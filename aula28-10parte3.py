import random as r

numero = r.randint(1, 100)
resposta = 0
tentativas = int(input("Quantas tentativas deseja arriscar: "))
#print("DEBUG: ", numero)

while resposta != numero:
    resposta = int(input("Entre com o numero: "))
    try:
        if resposta > numero:
          print("Menor")
        elif resposta < numero:
            print("Maior")
        tentativas = tentativas + 1 
        if tentativas == 3:
            print("Maximo de tentativas")
        break
    except ValueError:
        print("Valor invalido, tente novamente ")

if resposta == numero:
    print(f"Você acertou parabens em {tentativas}")
