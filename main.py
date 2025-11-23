from classes.Receita import Receita
from classes.Medicamento import Medicamento
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash
import re
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


app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui_123' 
def calcula_tempo_restante(dose_total_mg,intervalo_horas, dose_por_tomada_mg,  inicio):
    doses_totais = dose_total_mg / dose_por_tomada_mg
    tempo_total = timedelta(hours=doses_totais * intervalo_horas)
    fim = inicio + tempo_total
    agora = datetime.now()

    diff = fim - agora
    return diff.days 

@app.route('/')
def home():
    """Renderiza a página HTML inicial."""
    return render_template('home.html')

@app.route('/cadastrar_paciente')
def cadastrar_paciente():
    return render_template('cadastro_paciente.html')


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
    """Recebe os dados do formulário e salva a receita E OS ITENS."""
    
    
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
        
        descricoes = request.form.getlist('descricao_item')
        dias_lista = request.form.getlist('dias_tratamento')
        usos_continuos = request.form.getlist('uso_continuo_item') 

        for i in range(len(descricoes)):
            descricao = descricoes[i].strip()
            if not descricao: continue
            
            
            try:
                dias = int(dias_lista[i])
            except:
                dias = 0
            
            
            try:
                uso = usos_continuos[i]
            except:
                uso = "Nao"

            novo_item = {
                'receita_id': receita_id,
                'descricao': descricao,
                'dias_tratamento': dias,
                'uso_continuo': uso 
            }
            
            receita_item.create(novo_item) 
            
        flash('Receita salva!', 'success')
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


@app.route('/registros')
def listar_registros():
    receitas = receita.get_all()
    itens = receita_item.get_all()
    pacientes = paciente.get_all()

    registros = []
    for item in itens:
        
        if item.get('uso_continuo') != 'Sim':
            continue
    for item in itens:
        numeros = re.findall(r'\d+', item["descricao"])
        numeros = list(map(int, numeros))

        if len(numeros) == 4:
            for r in receitas:
                if r['id'] == item['receita_id']:

                    
                    paciente_encontrado = None
                    for p in pacientes:
                        if p['id'] == r['paciente_id']:
                            nome_paciente = p['nome']
                            break

                    
                    inicio = datetime.strptime(r["data_emissao"], "%Y-%m-%d")

                    
                    restante = calcula_tempo_restante(numeros[0],numeros[1],numeros[3],inicio=inicio)

                    
                    registros.append({
                        "paciente": nome_paciente,
                        "medicamento": item["descricao"].split("-")[0].strip(),
                        "restante": restante,
                        'telefone': p['telefone']
                    })
    return render_template("lista_registros.html", registros=registros)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')