#bibliotecas
import os
import time as time
#variavel global

saldo = 0
limite = 3
movimentacoes = {"Operações": []}
clientes = []
contador_contas = 1

def criar_conta(nome_cliente):
    global contador_contas  # Usamos a variável global para incrementar o número da conta
    for cliente in clientes:
        if nome_cliente in cliente:
            nova_conta = {
                "Número da Conta": f"{contador_contas:06d}",  # Conta com 6 dígitos
                "Número da Agência": "0001"
            }
            cliente[nome_cliente]["Contas Correntes"].append(nova_conta)
            contador_contas += 1  # Incrementa o número da conta
            print(f"Conta {nova_conta['Número da Conta']} criada para {nome_cliente}")
            return
    print("Cliente não encontrado")


def cadastra_cliente():
    global clientes
    nome = input("\nNome: ")
    endereco = input("\nEndereço: ")
    cpf = input("\nCPF: ")
    data_nasc = input("\nData de Nascimento: ")
    for cliente in clientes:
        for nome, info in cliente.items():
            if cpf in info["CPF"]:
                print("CPF já cadastrado")
                break
    else:
        clientes.append({
                        nome: { 
                            "Endereço": [endereco],
                            "CPF": [cpf],
                            "Data de Nascimento": [data_nasc],
                            "Contas Correntes": []
                        }   
                        })
    print("Cliente Cadastrado com sucesso!")
    return clientes

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
        choice = int(input("Seleciona a operação desejada\n 1 - Depósito\n 2 - Saque\n 3 - Checar Extrato\n 4 - Cadastrar Cliente\n 5 - Criar conta(CC)\n 6 - Sair\n"))
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
                cadastra_cliente()
                os.system('PAUSE')
            case 5:
                os.system('cls')
                nome = input("Nome do cliente:")
                criar_conta(nome)
                os.system('PAUSE')
            case 6:
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