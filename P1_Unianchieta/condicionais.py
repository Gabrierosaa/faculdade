nota = float(input("Digite a nota do aluno: "))

if nota >= 7: print("Aprovado")
else: print("Reprovado")

idade = int(input("Digite a idade: "))
if idade <= 17: 
    print("Menor de idade")
elif idade <= 65: 
    print("Adulto")
else:
    print("Idoso")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 > n2:
    print(f"O maior número é {n1}")
elif n2 == n1:
    print("Os números são iguais")
else:
    print(f"O maior número é {n2}")