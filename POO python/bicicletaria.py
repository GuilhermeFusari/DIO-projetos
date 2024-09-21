class Bicileta:
    def __init__(self,cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


    def buzinar(self):
        print("plim plim")


    def parar(self):
        print("Bicicleta parando...")
        print("Bicicleta parada")


    def correr(self):
        print("vrummmm")
   
    #def __str__(self):
     #   return f"----------\nBicicleta \nCor: {self.cor} \nModelo: {self.modelo} \nAno: {self.ano} \nValor: {self.valor}\n-----------"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}'for chave, valor in self.__dict__.items()])}"

b1 = Bicileta("vermelha","caloi",2022,600)
b1.buzinar()
b1.correr()
b1.parar()

print(b1)