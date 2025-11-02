import sqlite3
from classes.DataBase.Database import Database

class ReceitaItem_db(Database):
    def __init__(self,db_file):
        self.name="ReceitaItem"
        super().__init__(db_file)

    def init_table(self):
        sql = f'''
        CREATE TABLE IF NOT EXISTS {self.nome} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            receita_id INTEGER NOT NULL,
            medicamento_id INTEGER NOT NULL,
            dose_num INTEGER NOT NULL,
            dose_unidade TEXT NOT NULL,
            frequencia_horas INTEGER NOT NULL,
            duracao_dia INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            posologia TEXT NOT NULL,
            FOREIGN KEY(receita_id) REFERENCES receita(id)
            FOREIGN KEY(medicamento_id) REFERENCES medicamento(id)
        );
        '''
        return super().init_table(sql)
    
    def get_all(self):
        sql = f'SELECT * FROM {self.name} ORDER BY id'
        return super().get_all(sql)
    
    def create(self,inputs):
        return super().create(self.name,inputs)