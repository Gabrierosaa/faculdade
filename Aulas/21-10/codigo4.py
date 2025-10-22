def primo(numero):
    if numero % numero != 0:
        res = True
    else:
        res = False
    return res

num = int(input("Entre com um numero: "))
print(primo(num))