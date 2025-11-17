from classes.Receita import Receita
from classes.Medicamento import Medicamento

from flask import Flask, render_template, request, redirect, url_for, flash

from classes.DataBase.Paciente_db import Paciente_db
from classes.DataBase.Receita_db import Receita_db
from classes.DataBase.Medicamento_db import Medicamento_db 
from classes.DataBase.ReceitaItem_db import ReceitaItem_db

paciente = Paciente_db("farmacia.db")
receita = Receita_db("farmacia.db")
medicamento = Medicamento_db("farmacia.db")
receita_item = ReceitaItem_db("farmacia.db")

paciente.init_table()
receita.init_table()
medicamento.init_table()
receita_item.init_table()

# 1. Inicializa a aplicação Flask
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui_123' 

# 3. Define a rota para a página principal
@app.route('/')
def home():
    """Renderiza a página HTML inicial."""
    return render_template('home.html')

@app.route('/cadastrar_paciente')
def cadastrar_paciente():
    return render_template('cadastro_paciente.html')

# 4. Define a rota para receber os dados do formulário de paciente
@app.route('/salvar_paciente', methods=['POST'])
def salvar_paciente():
    """Recebe os dados do formulário e salva no banco de dados."""
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
        flash('Paciente cadastrado com sucesso!', 'success')
        return redirect(url_for('listar_pacientes'))
    else:
        flash('Erro ao cadastrar paciente. Verifique se o email já não está cadastrado.', 'error')
        return redirect(url_for('cadastrar_paciente'))


@app.route('/cadastrar_medicamento')
def cadastrar_medicamento():
    return render_template('cadastro_medicamento.html')

@app.route('/salvar_medicamento', methods=['POST'])
def salvar_medicamento():
    """Recebe os dados do formulário e salva o medicamento."""
    nome = request.form['nome']
    principio_ativo = request.form['principio_ativo']
    dosagem = request.form['dosagem']
    forma = request.form['forma']
    quantidade = request.form['quantidade']
    
    # Cria um dicionário para o novo medicamento
    novo_medicamento = {
        'nome': nome,
        'principio_ativo': principio_ativo,
        'dosagem': dosagem,
        'forma': forma,
        'quantidade': quantidade
    }
    flag = medicamento.create(novo_medicamento)

    if flag:
        flash('Medicamento cadastrado com sucesso!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Erro ao cadastrar medicamento. Verifique se já não existe um igual.', 'error')
        return render_template('cadastro_medicamento.html')

@app.route('/cadastrar_receita')
def cadastrar_receita():
    pacientes = paciente.get_all()
    
    return render_template('cadastro_receita.html', pacientes=pacientes)


@app.route('/salvar_receita', methods=['POST'])
def salvar_receita():
    """Salva a receita e os itens como texto simples."""
    
    paciente_id = request.form['paciente_id']
    nome_medico = request.form['nome_medico']
    crm_medico = request.form['crm_medico']
    data_emissao = request.form['data_emissao']

    nova_receita = {
        'paciente_id': paciente_id,
        'nome_medico': nome_medico,
        'crm_medico': crm_medico,
        'data_emissao': data_emissao
    }
    
    receita_id = receita.create(nova_receita) 

    if not receita_id:
        flash('Erro ao cadastrar a receita principal. Tente novamente.', 'error')
        pacientes = paciente.get_all()
        return render_template('cadastro_receita.html', pacientes=pacientes)

   
    try:
        
        descricoes_itens = request.form.getlist('descricao_item')
        for i in range(len(descricoes_itens)):
            
            descricao = descricoes_itens[i].strip()
            
            if not descricao:
                continue
                
           
            novo_item = {
                'receita_id': receita_id,
                'descricao': descricao  
            }
            
            receita_item.create(novo_item) 
            
        flash('Receita e itens cadastrados com sucesso!', 'success')
        return redirect(url_for('listar_receitas'))

    except Exception as e:
        flash(f'Receita salva, mas ocorreu um erro ao salvar os itens: {e}', 'error')
        return redirect(url_for('listar_receitas'))

@app.route('/pacientes')
def listar_pacientes():
    """Renderiza a página que exibe todos os pacientes cadastrados."""
    pacientes = paciente.get_all()
    return render_template('lista_pacientes.html', pacientes_cadastrados=pacientes)

@app.route('/receitas')
def listar_receitas():
    """Renderiza a página que exibe todas as receitas, pacientes e itens."""
    
    receitas = receita.get_all()
    
    todos_itens = receita_item.get_all() 
    
    todos_pacientes = paciente.get_all()

    return render_template(
        'lista_receitas.html', 
        receitas_cadastradas=receitas,
        itens_cadastrados=todos_itens,
        pacientes_cadastrados=todos_pacientes  
    )

@app.route('/deletar/<int:id>/<string:table>')
def deletar(id,table):
    if table == 'paciente':
        paciente.delete(id)
        return redirect(url_for('listar_pacientes'))

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')