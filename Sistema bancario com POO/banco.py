from abc import ABC, abstractmethod

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self) -> float:
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente, numero, agencia, saldo_inicial=0) -> object:
        return cls(saldo_inicial, numero, agencia, cliente, Historico())
    
    def sacar(self, valor) -> bool:
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        return False

    def depositar(self, valor) -> bool:
        if valor > 0:
            self._saldo += valor
            return True
        return False

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite_saques = limite_saques 
        self._limite = limite

    def sacar(self, valor) -> bool:
        if valor <= self._saldo + self._limite:
            return super().sacar(valor)
        return False

class Historico:
    def __init__(self):
        self.transacoes = []

    def transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if conta.depositar(self._valor):
            conta._historico.transacao(f"Depósito de {self._valor}")
            return True
        return False

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if conta.sacar(self._valor):
            conta._historico.transacao(f"Saque de {self._valor}")
            return True
        return False

class Cliente:
    def __init__(self, endereco, contas):
        self.endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta, transacao):
        if transacao.registrar(conta):
            print("Transação realizada com sucesso.")
        else:
            print("Falha ao realizar a transação.")

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento


