from classes.Receita import Receita
from classes.Medicamento import Medicamento

from flask import Flask, render_template, request, redirect, url_for

from classes.DataBase.Paciente_db import Paciente_db
from classes.DataBase.Receita_db import Receita_db
from classes.DataBase.Medicamento_db import Medicamento_db 


paciente = Paciente_db("farmacia.db")
receita = Receita_db("farmacia.db")
medicamento = Medicamento_db("farmacia.db")

paciente.init_table()
receita.init_table()
medicamento.init_table()

# paciente.create(nome="Alan",nascimento="27-08-2004",sexo="masculino",telefone="84999816810",email="alan.ac10.ac@gmail.com")
# receita.create(paciente_id=1,nome_medico="goku",crm_medico="123",data_emissao="01-01-2001")
# medicamento.create(nome="ibuprofeno",principio_ativo="ibuprofeno",dosagem="50mg",forma="comprimido",quantidade="10")

# 1. Inicializa a aplicação Flask
app = Flask(__name__)

# 2. "Banco de dados" temporário em memória (uma lista simples)
# Cada paciente será um dicionário adicionado a esta lista.

# 3. Define a rota para a página principal (o formulário de cadastro)
@app.route('/')
def home():
    """Renderiza a página HTML com o formulário."""
    return render_template('home.html')

@app.route('/cadastrar_paciente')
def cadastar_paciente():
    return render_template('cadastro_paciente.html')

# 4. Define a rota para receber os dados do formulário
@app.route('/salvar', methods=['POST'])
def salvar_paciente():

    """Recebe os dados do formulário e salva na nossa lista."""
    nome = request.form['nome']
    nascimento = request.form['nascimento']
    sexo = request.form['sexo']
    telefone = request.form['telefone']
    email = request.form['email']
    endereco = request.form['endereco']
    doencas = request.form['doencas']
    
    alergias = request.form['alergias']

    # Cria um dicionário para o novo paciente
    novo_paciente = {
        'nome': nome,
        'nascimento': nascimento,
        'sexo': sexo,
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
        'doencas': doencas,
        'alergias': alergias
    }
    flag = paciente.create(novo_paciente)

    if flag:
        return redirect(url_for('listar_pacientes'))
    return redirect(url_for('cadastrar_paciente'))


@app.route('/cadastrar_medicamento')
def cadastar_medicamento():
    return render_template('cadastro_medicamento.html')

@app.route('/salvar_medicamento', methods=['POST'])
def salvar_medicamento():

    """Recebe os dados do formulário e salva na nossa lista."""
    nome = request.form['nome']
    principio_ativo = request.form['principio_ativo']
    dosagem = request.form['dosagem']
    forma = request.form['forma']
    quantidade = request.form['quantidade']
    # Cria um dicionário para o novo paciente
    novo_paciente = {
        'nome': nome,
        'principio_ativo': principio_ativo,
        'dosagem': dosagem,
        'forma': forma,
        'quantidade': quantidade
    }
    flag = medicamento.create(novo_paciente)

    if flag:
        return redirect(url_for('home'))
    return render_template('cadastro_medicamento.html')

@app.route('/cadastrar_receita')
def cadastar_Receita():
    return render_template('cadastro_receita.html')

# 4. Define a rota para receber os dados do formulário
@app.route('/salvar_receita', methods=['POST'])
def salvar_receita():

    """Recebe os dados do formulário e salva na nossa lista."""
    paciente_id = request.form['paciente_id']
    nome_medico = request.form['nome_medico']
    crm_medico = request.form['crm_medico']
    data_emissao = request.form['data_emissao']

    # Cria um dicionário para o novo paciente
    nova_receita = {
        'paciente_id': paciente_id,
        'nome_medico': nome_medico,
        'crm_medico': crm_medico,
        'data_emissao': data_emissao
    }
    
    flag = receita.create(nova_receita)

    if flag:
        return redirect(url_for('home.html'))
    return render_template('cadastro_receita.html')

# 5. Define a rota para mostrar a lista de pacientes cadastrados
@app.route('/pacientes')
def listar_pacientes():
    """Renderiza a página que exibe todos os pacientes cadastrados."""
    pacientes=paciente.get_all()
    return render_template('lista_pacientes.html', pacientes_cadastrados=pacientes)

# 5. Define a rota para mostrar a lista de pacientes cadastrados
@app.route('/receitas')
def listar_receitas():
    """Renderiza a página que exibe todos os pacientes cadastrados."""
    receitas=receita.get_all()
    return render_template('lista_receitas.html', receitas_cadastradas= receitas)

# 6. Roda a aplicação
if __name__ == '__main__':
    # O debug=True faz o servidor reiniciar automaticamente quando você altera o código
    app.run(debug=True)