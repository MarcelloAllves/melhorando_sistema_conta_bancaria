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
