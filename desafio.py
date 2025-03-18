"""
Sistema Bancário em Python

Descrição:
    Este sistema bancário simula um conjunto de operações financeiras básicas,
    incluindo cadastro de usuários, depósitos, saques e visualização de extrato.
    Ele foi projetado para ser simples e funcional, atendendo aos seguintes requisitos
    principais:

Funcionalidades:
    1. Cadastro de Usuários:
        - Os usuários devem ser registrados antes de realizar quaisquer operações no sistema.
        - Cada usuário possui os seguintes atributos:
            - Nome completo
            - CPF: Deve conter 11 caracteres numéricos e ser único para cada usuário.
            - Número da agência bancária: Representado por 4 caracteres numéricos.
            - Número da conta: Representado por 6 caracteres numéricos e único dentro de
            uma agência.

    2. Validação:
        - O CPF e o número da conta são validados para garantir unicidade e conformidade
        com os formatos exigidos.
        - Não é permitido cadastrar duas contas iguais na mesma agência.

    3. Operações Bancárias:
        - **Depósito**:
            Permite adicionar valores positivos à conta. Transações são limitadas a 10 por dia.
        - **Saque**:
            Permite retirar valores da conta, desde que haja saldo suficiente.
            Transações também são limitadas a 10 por dia.
        - **Extrato**: Exibe o histórico de transações (depósitos e saques), com data, hora
        e descrição. O saldo atual é mostrado ao final.

    4. Controle de Transações:
        - Todas as transações são registradas com a data e hora exatas.
        - É exibido um cabeçalho no extrato contendo informações como nome do titular,
        número da agência e da conta.
        - Apenas 10 transações diárias são permitidas.

Tecnologias e Estrutura:
    - Utiliza a biblioteca `datetime` para manipulação de datas e horários.
    - As informações dos usuários são passadas como parâmetros entre funções.
    - O sistema foi projetado para ser modular e de fácil manutenção, utilizando funções
    para cada funcionalidade.

Menu Principal:
    - O sistema apresenta um menu interativo com as opções:
        1. Cadastrar Usuário
        2. Acessar Conta
        3. Sair do Sistema

    - Dentro de uma conta, o usuário pode:
        1. Depositar
        2. Sacar
        3. Visualizar Extrato
        4. Sair para o menu principal

Como usar:
    - Execute o programa e escolha as opções no menu para interagir com o sistema.
    - O usuário deve fornecer entradas válidas para CPF, número da conta, e valores de
    transações.

Notas:
    - Este sistema é um modelo de exemplo para estudos e pode ser expandido conforme
    necessário.
    - Caso precise de mais funcionalidades, como autenticação ou limite de saldo, elas podem
     ser adicionadas facilmente.
"""

from datetime import datetime

# Função para validar CPF
def validar_cpf(cpf, usuarios):
    return (len(cpf) == 11 and cpf.isdigit()
            and cpf not in [usuario["cpf"] for usuario in usuarios])

# Função para validar número de conta
def validar_conta(numero_conta, agencia_bancaria, usuarios):
    if len(numero_conta) != 6 or not numero_conta.isdigit():
        return False
    for usuario in usuarios:
        if (usuario["numero_conta"] == numero_conta
                and usuario["agencia_bancaria"] == agencia_bancaria):
            return False
    return True

# Função para cadastrar usuário
def cadastrar_usuario(usuarios):
    print("\n--- Cadastro de Usuário ---")
    nome = input("Digite o nome completo: ")
    cpf = input("Digite o CPF (apenas números): ")
    if not validar_cpf(cpf, usuarios):
        print("CPF inválido ou já cadastrado.")
        return usuarios
    agencia_bancaria = input("Digite o número da agência (4 dígitos): ")
    numero_conta = input("Digite o número da conta (6 dígitos): ")
    if not validar_conta(numero_conta, agencia_bancaria, usuarios):
        print("Número de conta inválido ou já existente nessa agência.")
        return usuarios
    usuarios.append({"nome": nome, "cpf": cpf, "agencia_bancaria": agencia_bancaria, "numero_conta": numero_conta, "saldo": 0.0, "transacoes": []})
    print("Usuário cadastrado com sucesso!")
    return usuarios

# Função para buscar conta pelo CPF
def buscar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

# Função para depositar
def depositar(usuario, valor):
    if valor <= 0:
        print("Valor inválido para depósito.")
        return
    if len(usuario["transacoes"]) >= 10:
        print("Limite de transações diárias atingido.")
        return
    usuario["saldo"] += valor
    usuario["transacoes"].append((datetime.now(), f"Depósito: R$ {valor:.2f}"))
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

# Função para sacar
def sacar(usuario, valor):
    if valor <= 0:
        print("Valor inválido para saque.")
        return
    if len(usuario["transacoes"]) >= 10:
        print("Limite de transações diárias atingido.")
        return
    if valor > usuario["saldo"]:
        print("Saldo insuficiente para saque.")
        return
    usuario["saldo"] -= valor
    usuario["transacoes"].append((datetime.now(), f"Saque: R$ {valor:.2f}"))
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

# Função para visualizar extrato
def visualizar_extrato(usuario):
    print("\n=== Extrato ===")
    print(f"Agência: {usuario['agencia_bancaria']} | Conta: {usuario['numero_conta']} | Titular: {usuario['nome']}")
    if not usuario["transacoes"]:
        print("Não há transações.")
    else:
        for data, operacao in usuario["transacoes"]:
            print(f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {operacao}")
    print(f"\nSaldo atual: R$ {usuario['saldo']:.2f}")
    print("================")

# Menu principal
def menu():
    usuarios = []
    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Cadastrar Usuário")
        print("2. Acessar Conta")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            usuarios = cadastrar_usuario(usuarios)
        elif opcao == "2":
            cpf = input("Digite o CPF para acessar a conta: ")
            usuario = buscar_usuario(cpf, usuarios)
            if not usuario:
                print("Usuário não encontrado.")
                continue

            while True:
                print(f"\n--- Bem-vindo(a), {usuario['nome']} ---")
                print("1. Depositar")
                print("2. Sacar")
                print("3. Visualizar Extrato")
                print("4. Sair")

                opcao_conta = input("Escolha uma opção: ")
                if opcao_conta == "1":
                    valor = float(input("Digite o valor do depósito: "))
                    depositar(usuario, valor)
                elif opcao_conta == "2":
                    valor = float(input("Digite o valor do saque: "))
                    sacar(usuario, valor)
                elif opcao_conta == "3":
                    visualizar_extrato(usuario)
                elif opcao_conta == "4":
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif opcao == "3":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema
menu()
