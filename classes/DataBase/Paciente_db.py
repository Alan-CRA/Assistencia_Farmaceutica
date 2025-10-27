import sqlite3
from classes.DataBase.Database import Database
class Paciente_db(Database):
    def __init__(self,db_file):
        self.name="paciente"
        super().__init__(db_file)

    def init_table(self):
        sql = f'''
        CREATE TABLE IF NOT EXISTS {self.name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nascimento TEXT NOT NULL,
            sexo TEXT NOT NULL,
            telefone TEXT,
            email TEXT UNIQUE,
            endereco TEXT,
            doencas TEXT,
            alergias TEXT
        );
        '''
        return super().init_table(sql)
    
    def get_all(self):
        sql = f'SELECT * FROM {self.name} ORDER BY id'
        return super().get_all(sql)
    
    def create(self,**inputs):
        return super().create(self.name,inputs)