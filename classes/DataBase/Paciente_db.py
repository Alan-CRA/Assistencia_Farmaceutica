import sqlite3
from classes.DataBase.Database import Database

class Paciente_db(Database):
    def __init__(self,db_file):
        super().__init__(db_file)
        self.name="paciente" 

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
    
    def create(self,inputs):
        return super().create(self.name,inputs)
    
    def get_all(self):
        """Busca todos os pacientes da tabela 'paciente'."""
        conn = None
        try:
            # CORREÇÃO AQUI:
            conn = self._get_conn() # Usando _get_conn
            
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.name}")
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar todos os {self.name}: {e}")
            return []
        finally:
            if conn:
                conn.close()
    
    def delete(self,id):
        return super().delete(self.name,id)