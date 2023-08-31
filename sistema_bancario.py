menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''

conta = 0
extrato = ""
numero_saques = 0

def depositar(valor):
    if valor > 0:
        conta += valor
        extrato += f"Depósito: R${valor:.2f}\n"
    else:
        print("O valor do depósito deve ser maior que zero")
    
    
def sacar(valor):
    if numero_saques >=3:
        print("Limite de saques diários atingido. Tente novamente outro dia")
    if conta < valor:
        print("Saldo insuficiente")
    elif valor > 500:
        print("O valor máximo de saque é de 500 reais")
    else:
        conta -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1

while True:
    opcao = input(menu)
    
    if(opcao == "d"):
        valor_deposito = input("Digite o valor a ser depositado")
        depositar(float(valor_deposito))
    elif opcao == "s":
        valor_saque = input("Digite o valor a ser sacado")
        sacar((float(valor_saque)))
    elif opcao == "e":
        print(extrato)
        print(f"Saldo: {conta:.2f}")
    elif opcao == "q":
        break
    else:
        print("Operação inválida. Selecione novamente a operação desejada.")