import textwrap

def menu(): 
    menu = '''
    ======= MENU =======
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar usuário
    [c] Abrir conta
    [q] Sair
    ==>
    '''
    return input(textwrap.dedent(menu))

def depositar(conta, extrato, valor, /):
    if valor > 0:
        conta += valor
        extrato += f"Valor do depósito: R${valor:.2f}\n"
        print(extrato)
        print("=== Depósito realizado com sucesso ===")
    else:
        print("=== O valor do depósito deve ser maior que zero ===")
    return conta, extrato

def sacar(*, conta, valor, extrato, numero_saques):
    if numero_saques >= 3:
        print("=== Limite de saques diários atingido. Tente novamente outro dia ===")
    if valor > int(conta):
        print("=== Saldo insuficiente ===")
    elif valor > 500:
        print("=== O valor máximo de saque é de 500 reais ===")
    elif valor > 0:
        conta -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
        print("\n === Saque realizado com sucesso ===")
    else:
        print("O valor informado é inválido.")
    return conta, extrato

def tirar_extrato(conta, /, *, extrato):
    print(f"Extrato: \n{extrato}\n")
    print(f"Saldo total: {conta}\n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n Já existe um usuário cadastrado com esse CPF")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereco completo: ")

    usuarios.append(
        {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário cadastrado com sucesso ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(usuarios, numero_conta):
    numero = numero_conta + 1
    cpf = input("Digite o seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n === Conta criada com sucesso ===")
        return {"agencia": "0001", "numero_conta": numero, "usuario": usuario}

    print("\n === Usuário não encontrado ===")

def main():
    conta = 0.0
    extrato = ""
    numero_saques = 0
    usuarios = []
    numero_conta = 0
    
    while True:
        opcao = menu()

        if (opcao == "d"):
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            conta, extrato = depositar(conta, extrato, valor_deposito)
        elif opcao == "s":
            valor_saque = float(input("Digite o valor a ser sacado: "))
            conta, extrato = sacar(conta=conta, valor=valor_saque, extrato=extrato, numero_saques=numero_saques)
        elif opcao == "e":
            tirar_extrato(conta, extrato=extrato)
        elif opcao == "u":
            criar_usuario(usuarios)
        elif opcao == "c":
            criar_conta(usuarios, numero_conta)
        elif opcao == "q":
            break
        else:
            print("=== Operação inválida. Selecione novamente a operação desejada. ===")

main()