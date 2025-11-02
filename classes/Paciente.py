from classes.Medicamento import Medicamento
from classes.Receita import Receita


class Paciente:
    def __init__(self,id,nome,nascimento,sexo,telefone,email,endereco,doencas=[],alergias=[]):
        self.id = id
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.doencas = doencas
        self.alergias = alergias

    def setNome(self,nome):
        self.nome = nome

    def setNascimento(self,nascimento):
        self.nascimento = nascimento

    def setSexo(self,sexo):
        self.sexo = sexo

    def setTelefone(self,telefone):
        self.telefone = telefone
    
    def setEmail(self,email):
        self.email = email
    
    def setEndereco(self,endereco):
        self.endereco = endereco

    def setDoencas(self,doencas):
        self.doencas = doencas

    def setAlergias(self,alergias):
        self.alergias = alergias