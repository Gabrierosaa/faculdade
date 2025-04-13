def criar_conta():
    nome1 = input("Entre com seu nome: ")
    saldo1 = int(input("Entre com seu saldo: "))
    
    class ContaBancaria:
        def __init__(self):
            self.nome = nome1
            self._saldo = saldo1
            
    return ContaBancaria()

def deposito():
    global minha_conta
    valor = int(input("Entre com o valor: "))
    if valor > 0:
        minha_conta._saldo += valor
        print(f"Depósito feito. Seu novo saldo é R${minha_conta._saldo}")
    else:
        print("Erro: valor inválido para depósito.")

def sacar():
    global minha_conta
    valor = int(input("Entre com o valor: "))
    if valor > 0:
        if minha_conta._saldo >= valor:
            minha_conta._saldo -= valor
            print(f"Saque realizado. Novo saldo: R${minha_conta._saldo}")
        else:
            print("Saldo insuficiente.")
    else:
        print("Erro: valor inválido para saque.")

def ver_saldo():
    global minha_conta
    print(f"Nome: {minha_conta.nome}, Saldo: R${minha_conta._saldo}")

# Menu principal
escolha = int(input("[1]Criar Conta [2]Depositar [3]Sacar [4]Ver saldo "))

while escolha == 1:
    minha_conta = criar_conta()
    escolha = int(input("[1]Criar Conta [2]Depositar [3]Sacar [4]Ver saldo "))

while escolha == 2:
    deposito()
    escolha = int(input("[1]Criar Conta [2]Depositar [3]Sacar [4]Ver saldo "))

while escolha == 3:
    sacar()
    escolha = int(input("[1]Criar Conta [2]Depositar [3]Sacar [4]Ver saldo "))

while escolha == 4:
    ver_saldo()
    escolha = int(input("[1]Criar Conta [2]Depositar [3]Sacar [4]Ver saldo "))
