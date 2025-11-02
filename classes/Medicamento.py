class Medicamento:
    # frequencia [1,3,1]
    # 1 unidade pra ingerir,3 comprimidos diariamente("X 1")

    def __init__(self,id,nome,principio_ativo,dosagem,forma,quantidade):
        self.id = id
        self.nome = nome
        self.principio_ativo = principio_ativo
        self.dosagem = dosagem
        self.forma = forma
        self.quantidade = quantidade
        
    def setId(self,id):
        self.id = id

    def setNome(self,nome):
        self.nome = nome

    def setPrincipio_ativo(self,principio_ativo):
        self.principio_ativo = principio_ativo

    def setDose(self,dosagem):
        self.dosagem = dosagem

    def setFrequencia(self,forma):
        self.forma = forma

    def setQuantidade(self,quantidade):
        self.quantidade = quantidade
