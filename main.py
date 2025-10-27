#from classes.Receita import Receita
#from classes.Medicamento import Medicamento

#from flask import Flask, render_template, request, redirect, url_for

from classes.DataBase.Paciente_db import Paciente_db
from classes.DataBase.Receita_db import Receita_db
from classes.DataBase.Medicamento_db import Medicamento_db


paciente = Paciente_db("TESTE.db")
receita = Receita_db("TESTE.db")
medicamento = Medicamento_db("TESTE.db")

paciente.init_table()
receita.init_table()
medicamento.init_table()

#paciente.create(nome="Alan",nascimento="27-08-2004",sexo="masculino",telefone="84999816810",email="alan.ac10.ac@gmail.com")
receita.create(paciente_id=1,nome_medico="goku",crm_medico="123",data_emissao="01-01-2001")
medicamento.create(nome="ibuprofeno",principio_ativo="ibuprofeno",dosagem="50mg",forma="comprimido",quantidade="10")

#receita.create(paciente_id=21,nome_medico="goku",crm_medico="123",data_emissao="01-01-2001")

getpac=paciente.get_all()
getrec=receita.get_all()
getmed=medicamento.get_all()

for i in getpac:
    print(list(dict(i).items()))
for i in getrec:
    print(list(dict(i).items()))
for i in getmed:
    print(list(dict(i).items()))


# receita = Receita("12-10-2025",[Remedio("dorflex","1g",[1,3,2], 12), Remedio("paracetamol","400mg",[4,2,1], 20)])
# # 1 unidade pra ingerir,3 comprimidos a cada 2 dias 
# # [1,3,2] 

# remedios = receita.getRemedios()
# for i in remedios:
#     print(i.getNome())


# # 1. Inicializa a aplicação Flask
# app = Flask(__name__)

# # 2. "Banco de dados" temporário em memória (uma lista simples)
# # Cada paciente será um dicionário adicionado a esta lista.
# pacientes = []

# # 3. Define a rota para a página principal (o formulário de cadastro)
# @app.route('/')
# def formulario_cadastro():
#     """Renderiza a página HTML com o formulário."""
#     return render_template('cadastro.html')

# # 4. Define a rota para receber os dados do formulário
# @app.route('/salvar', methods=['POST'])
# def salvar_paciente():
#     """Recebe os dados do formulário e salva na nossa lista."""
#     nome = request.form['nome']
#     cpf = request.form['cpf']
#     alergias = request.form['alergias']

#     # Cria um dicionário para o novo paciente
#     novo_paciente = {
#         'nome': nome,
#         'cpf': cpf,
#         'alergias': alergias
#     }

#     # Adiciona o novo paciente à nossa lista "banco de dados"
#     pacientes.append(novo_paciente)

#     # Imprime no terminal para vermos o que foi salvo (ótimo para debug)
#     print("--- Paciente Cadastrado ---")
#     print(novo_paciente)
#     print("---------------------------")
#     print("Todos os pacientes:", pacientes)

#     # Redireciona o usuário para a página que lista os pacientes
#     return redirect(url_for('listar_pacientes'))

# # 5. Define a rota para mostrar a lista de pacientes cadastrados
# @app.route('/pacientes')
# def listar_pacientes():
#     """Renderiza a página que exibe todos os pacientes cadastrados."""
#     return render_template('lista_pacientes.html', pacientes_cadastrados=pacientes)


# # 6. Roda a aplicação
# if __name__ == '__main__':
#     # O debug=True faz o servidor reiniciar automaticamente quando você altera o código
#     app.run(debug=True)