import sqlite3
from classes.DataBase.Database import Database

class Receita_db(Database):
    def __init__(self,db_file):
        self.name="receita"
        super().__init__(db_file)

    def init_table(self):
        sql = f'''
        CREATE TABLE IF NOT EXISTS {self.name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER NOT NULL,
            nome_medico TEXT NOT NULL,
            crm_medico TEXT NOT NULL,
            data_emissao TEXT NOT NULL,
            FOREIGN KEY(paciente_id) REFERENCES paciente(id)
        );
        '''
        return super().init_table(sql)
    
    def get_all(self):
        sql = f'SELECT * FROM {self.name} ORDER BY id'
        return super().get_all(sql)
    
    def create(self,inputs):
        return super().create(self.name,inputs)