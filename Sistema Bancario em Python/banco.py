#bibliotecas
import os
import time as time
#variavel global

saldo = 0
limite = 3
movimentacoes = {"Operações": []}

def checa_limite():
    return limite > 0



def checa_valor(valor):
    return valor <= saldo




def extrato(valor=0, saque=False):
    global movimentacoes
    if valor != 0:
        if saque:
            movimentacoes["Operações"].append({"Operação": "saque", "Valor": valor})
        else:
            movimentacoes["Operações"].append({"Operação": "depósito", "Valor": valor})
        return movimentacoes

    return movimentacoes




def saque(valor_saque):
    global saldo, limite 
    
    if not checa_valor(valor_saque):
        return f"Você não possui o valor de R$ {valor_saque:.2f} na sua conta."
    
    elif not checa_limite():
        return f"Você já atingiu o limite de 3 saques por dia, por favor tente novamente amanhã."
    

    extrato(valor_saque, saque=True)
    saldo -= valor_saque
    limite -= 1 
    return f"Saque de R$ {valor_saque:.2f} realizado com sucesso."




def deposito(valor_deposito):
    global saldo
    extrato(valor_deposito, saque = False)
    saldo += valor_deposito

    return f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!"




def menu():

    print("Bem vindo ao Banco\n")

    while True:
        choice = int(input("Seleciona a operação desejada\n 1 - Depósito\n 2 - Saque\n 3 - Checar Extrato\n 4 - Sair\n"))
        match choice:
            case 1:
                os.system('cls')
                valor_deposito = int(input("Qual o valor que deseja depositar?\nR$:"))
                print(deposito(valor_deposito))
                os.system("PAUSE")
                os.system('cls')

            case 2:
                os.system('cls')
                valor_saque = int(input("Qual o valor que deseja sacar?\nR$:"))
                print(saque(valor_saque))
                os.system("PAUSE")
                os.system('cls')
            
            case 3:
                os.system('cls')
                global movimentacoes

                if not movimentacoes["Operações"]:
                    print("Nenhuma movimentação realizada.")

                print("Extrato de movimentações:")
   
                for operacao in movimentacoes["Operações"]:
                    print(f"Operação: {operacao['Operação']}, Valor: R$ {operacao['Valor']:.2f}\n")
                print(f"Saldo na conta: R$ {saldo:.2f}")
                os.system("PAUSE")
                os.system('cls')

            case 4:
                os.system('cls')
                print("Saindo....")
                time.sleep(2)
                return False
            
            case _:
                os.system('cls')
                print("Por favor selecione uma opção válida.")




def main():
    menu()
    os.system('cls')




if __name__ == "__main__":
    main()