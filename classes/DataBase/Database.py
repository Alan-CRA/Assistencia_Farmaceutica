import sqlite3

class Database:
    def __init__(self, db_file):
        """Salva o nome do arquivo do banco quando a classe é criada."""
        self.db_file = db_file

    def _get_conn(self):
        """Função privada para criar e configurar a conexão."""
        conn = sqlite3.connect(self.db_file)
        conn.execute("PRAGMA foreign_keys = 1")
        conn.row_factory = sqlite3.Row
        return conn

    def init_table(self,sql):

        sql_receitaItem = '''
        CREATE TABLE IF NOT EXISTS receita_item (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            receita_id INTEGER NOT NULL,
            medicamento_id INTEGER NOT NULL,
            dose_num INTEGER NOT NULL,
            dose_unidade TEXT NOT NULL,
            frequencia_horas INTEGER NOT NULL,
            duracao_dia INTEGER NOT NULL,
            posologia TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            FOREIGN KEY(receita_id) REFERENCES receita(id)
            FOREIGN KEY(medicamento_id) REFERENCES medicamento(id)
        );
        '''

        try:
            conn=self._get_conn()
            conn.execute(sql)
            print("Tabela inicializada com sucesso.")
        except Exception as e:
            print(f"Erro ao inicializar o banco: {e}")

    def get_all(self,sql):
        try:
            conn=self._get_conn()
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar pacientes: {e}")
            return [] # Retorna lista vazia em caso de erro
        finally:
            conn.close()

    def create(self, table,inputs):
        """Adiciona um novo paciente ao banco de dados."""
        chaves=list(inputs.keys())
        n=len(chaves)
        sql = f'INSERT INTO {table} ('
        for i in range(n-1):
            sql=sql+chaves[i]+", "
        sql=sql+chaves[-1]+")"
        sql=f"{sql} VALUES ({"?, "*(n-1)}?)"
        values = tuple(inputs.values())
        try:
            conn=self._get_conn()
            conn.execute(sql, values)
            conn.commit()
            return True # Sucesso
        except sqlite3.IntegrityError as e:
            print(f"Erro: {e}")
            return False # Falha (CPF duplicado)
        except Exception as e:
            print(f"Erro ao criar {table}: {e}")
            return False # Falha (outro erro)]
        finally:
            conn.close()


    # Você poderia adicionar outros métodos aqui:
    # def get_patient_by_id(self, id): ...
    # def update_patient(self, id, ...): ...
    # def delete_patient(self, id): ...