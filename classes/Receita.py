from classes.Medicamento import Medicamento

class Receita:
    def __init__(self,id,paciente_id,nome_medico,crm_medico,data_emissao):
        self.id = id
        self.paciente_id = paciente_id
        self.nome_medico = nome_medico
        self.crm_medico = crm_medico
        self.data_emissao = data_emissao
    
    def setVencimento(self,vencimento):
        self.vencimento = vencimento

    def setRemedios(self,remedios):
        self.remedios = remedios
