class Estudante:
    escola = "DIO"
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objts):
    for obj in objts:
        print(obj)

    
aluno_1 = Estudante("Guiherme", 1)
aluno_2 = Estudante("Giovanna", 2)

print(aluno_1)
print(aluno_2)

Estudante.escola = "Python" #troca de todos os objts criados

aluno_3 = Estudante("carlos", 3)

aluno_1.matricula = 3 #troca apenas da instancia

mostrar_valores(aluno_1,aluno_2,aluno_3)

