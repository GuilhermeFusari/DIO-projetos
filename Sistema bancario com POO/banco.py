from abc import ABC

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self) -> float:
        return self.saldo
    

    @classmethod
    def nova_conta(cls, cliente, numero) -> object:
        return cls(cliente, numero)
    

    def sacar(self, valor)-> bool:
        ...


    def depositar(self, valor)-> bool:
        ...



class Conta_Corrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limites_saques = limite_saques
        self._limites= limite



class Historico:
    def transacao(self, transacao):
        ...



class Transacao(ABC):

    @staticmethod
    def registrar(self, conta):
        ...



class Depostio(Transacao):

    def __init__(self, valor):
        self._valor - valor

    def registrar(self, conta):
        ...



class Saque(Transacao):

    def __init__(self, valor):
        self._valor - valor

    def registrar(self, conta):
        ...



class Cliente:

    def __init__(self, endereco, contas):
        self.endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta, transacao):
        ...

    def adicionar_conta(self,conta):
        ...



class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento ):
        super().__init__(endereco, contas)
        self._cpf= cpf
        self._nome= nome
        self._data_nascimento= data_nascimento