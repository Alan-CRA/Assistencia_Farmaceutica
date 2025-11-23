from .Database import Database

class ReceitaItem_db(Database):
    
    def __init__(self, db_file):
        super().__init__(db_file)
        self.name = 'receita_item'

    def init_table(self):
        conn = None
        try:
            conn = self._get_conn()
            cursor = conn.cursor()
            
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                receita_id INTEGER NOT NULL,
                descricao TEXT NOT NULL,
                dias_tratamento INTEGER,
                uso_continuo TEXT, 
                FOREIGN KEY(receita_id) REFERENCES receita(id)
            )
            """)
            conn.commit()
        except Exception as e:
            print(f"Erro tabela: {e}")
        finally:
            if conn: conn.close()

    def create(self, item):
        conn = None
        try:
            conn = self._get_conn()
            cursor = conn.cursor()
            
            cursor.execute(
                f"INSERT INTO {self.name} (receita_id, descricao, dias_tratamento, uso_continuo) VALUES (?, ?, ?, ?)",
                (item['receita_id'], item['descricao'], item['dias_tratamento'], item['uso_continuo'])
            )
            
            novo_id = cursor.lastrowid
            conn.commit()
            return novo_id
        except Exception as e:
            print(f"Erro create: {e}")
            if conn: conn.rollback()
            return None
        finally:
            if conn: conn.close()

    def get_by_receita_id(self, receita_id):
        conn = None
        try:
            conn = self._get_conn()
            conn.row_factory = self.dict_factory
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.name} WHERE receita_id = ?", (receita_id,))
            return cursor.fetchall()
        except Exception:
            return []
        finally:
            if conn: conn.close()
            
    def get_all(self):
        conn = None
        try:
            conn = self._get_conn()
            conn.row_factory = self.dict_factory
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.name}")
            return cursor.fetchall()
        except Exception:
            return []
        finally:
            if conn: conn.close()