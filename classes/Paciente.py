from classes.Medicamento import Remedio
from classes.Receita import Receita

class Paciente:
    def __init__(self,nome,nascimento,sexo,telefone,email,endereco,doencas=[],receitas=[],remedios=[]):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__sexo = sexo
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco
        self.__doencas = doencas
        self.__receitas = receitas
        self.__remedios = remedios

    def getNome(self):
        return self.__nome
    
    def getNascimento(self):
        return self.__nascimento
    
    def getSexo(self):
        return self.__sexo
    
    def getTelefone(self):
        return self.__telefone
    
    def getEmail(self):
        return self.__email
    
    def getEndereco(self):
        return self.__endereco

    def getDoencas(self):
        return self.__doencas
    
    def getReceitas(self):
        return self.__receitas
    
    def getRemedios(self):
        return self.__remedios
  
    def setNome(self,nome):
        self.__nome = nome

    def setNascimento(self,nascimento):
        self.__nome = nascimento

    def setSexo(self,sexo):
        self.__nome = sexo

    def setTelefone(self,telefone):
        self.__nome = telefone
    
    def setEmail(self,email):
        self.__nome = email
    
    def setEndereco(self,endereco):
        self.__nome = endereco

    def setDoencas(self,doencas):
        self.__nome = doencas

    def setReceitas(self,receitas):
        self.__nome = receitas

    def setRemedios(self,remedios):
        self.__nome = remedios