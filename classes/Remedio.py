class Remedio:
    # frequencia [1,3,1]
    # 1 unidade pra ingerir,3 comprimidos diariamente("X 1")
    def __init__(self,nome,dose,frequencia,quantidade):
        self.__nome = nome
        self.__dose = dose
        self.__frequencia = frequencia
        self.__quantidade = quantidade

    
    def getNome(self):
        return self.__nome
    
    def getDose(self):
        return self.__dose
    
    def getFrequencia(self):
        return self.__frequencia
    
    def getQuantidade(self):
        return self.__quantidade
    
    
    def setNome(self,nome):
        self.__nome = nome

    def setDose(self,dose):
        self.__dose = dose

    def setFrequencia(self,frequencia):
        self.__frequencia = frequencia

    def setQuantidade(self,quantidade):
        self.__quantidade = quantidade
