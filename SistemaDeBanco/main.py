def deposito():
    print("========================================================================")
    QUANTIA = input("Quanto deseja depositar?> ")
    try:
        QUANTIA = float(QUANTIA)
    except:
        print("Valor inválido.")
        return 0
    if QUANTIA < 0:
        print("Valor inválido.")
        return 0
    return QUANTIA

def saque(SALDO):
    print("========================================================================")
    QUANTIA = input("Quanto deseja tirar?(Limite de 500 R$> ")
    try:
        QUANTIA = float(QUANTIA)
    except:
        print("Valor inválido.")
        return 0
    if QUANTIA > 500:
        print("Acima do limite")
        return 0
    elif QUANTIA < 0:
        print("Valor inválido.")
        return 0
    elif QUANTIA > SALDO:
        print("Saldo insuficiente.")
        return 0
    return QUANTIA

SALDO = 0
SAQUES = 3
EXTRATO = []
while True:
    ESCOLHA = input(f"""
========================================================================
                Sistema Bancário
                Saldo: {SALDO}
                Saques: {SAQUES}
                1. Depositar
                2. Saquear
                3. Extrato
                >""")

    if ESCOLHA == "1":
        SOMA = deposito()
        SALDO += SOMA
        EXTRATO.append(f"Depósito R${SOMA}")

    elif ESCOLHA == "2":
        if SAQUES == 0:
            print("Limite de saques diários alcançado.")
        else:
            SUBTRAÇÂO = saque(SALDO)
            SALDO -= SUBTRAÇÂO
            if SUBTRAÇÂO > 0:
                SAQUES -= 1
                EXTRATO.append(f"Saque R${SUBTRAÇÂO}")

    elif ESCOLHA == "3":
        print("========================================================================")
        for OPERACAO in EXTRATO:
            print(OPERACAO)
        print(f"Saldo atual: R${SALDO}")

