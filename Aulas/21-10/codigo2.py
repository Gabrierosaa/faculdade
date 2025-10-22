def impar_ou_par(entrada):
    if entrada % 2 == 0:
        res = "par"
    else:
        res = "impar"
    return res
num = input("DIgite um numero")
print(impar_ou_par(num))