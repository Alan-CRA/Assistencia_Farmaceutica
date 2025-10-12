import Remedio

class Receita:
    def __init__(self,vencimento,remedios=[]):
        self.__vencimento = vencimento
        self.__remedios = remedios
      
    def getVencimento(self):
        return self.__vencimento

    def getRemedios(self):
        return self.__remedios
    
    def setVencimento(self,vencimento):
        self.__vencimento = vencimento

    def setRemedios(self,remedios):
        self.__remedios = remedios
