import sqlite3
from classes.DataBase.Database import Database
class Medicamento_db(Database):
    def __init__(self,db_file):
        self.name="medicamento"
        super().__init__(db_file)
    
    def init_table(self):
        sql = f'''
        CREATE TABLE IF NOT EXISTS {self.name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            principio_ativo TEXT NOT NULL,
            dosagem TEXT NOT NULL,
            forma TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            UNIQUE(nome, principio_ativo, dosagem, forma, quantidade)
        );
        '''
        return super().init_table(sql)
    
    def get_all(self):
        sql = f'SELECT * FROM {self.name} ORDER BY id'
        return super().get_all(sql)
    
    def create(self,**inputs):
        return super().create(self.name,inputs)