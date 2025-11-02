from classes.Medicamento import Medicamento
from classes.Receita import Receita


class ReceitaItem:
    def __init__(self,id,receita_id,medicamento_id,dose_num,dose_unidade,frequencia_horas,duracao_dia,quantidade,posologia):
        self.id = id
        self.receita_id = receita_id
        self.medicamento_id = medicamento_id
        self.dose_num = dose_num
        self.dose_unidade = dose_unidade
        self.frequencia_horas = frequencia_horas
        self.duracao_dia = duracao_dia
        self.quantidade = quantidade
        self.posologia = posologia

    def set_id(self,id):
        self.id = id

    def set_id(self,receita_id):
        self.receita_id = receita_id

    def set_id(self,medicamento_id):
        self.medicamento_id = medicamento_id

    def set_id(self,dose_num):
        self.dose_num = dose_num

    def set_id(self,dose_unidade):
        self.dose_unidade = dose_unidade

    def set_id(self,frequencia_horas):
        self.frequencia_horas = frequencia_horas

    def set_id(self,duracao_dia):
        self.duracao_dia = duracao_dia

    def set_id(self,quantidade):
        self.quantidade = quantidade

    def set_id(self,posologia):
        self.posologia = posologia