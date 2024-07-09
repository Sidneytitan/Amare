from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Função para conectar ao MongoDB
def connect_to_mongodb():
    client = MongoClient("mongodb+srv://sidneycko:titanbetty@cluster0.feenv6t.mongodb.net/?retryWrites=true&w=majority")
    db = client["Amare"]
    collection = db["cliente"]  # Coleção para os clientes
    return collection

# Rota para a página inicial
@app.route('/base')
def base():
    current_year = datetime.now().year  # Obtém o ano atual
    return render_template('base.html', current_year=current_year)

# Rota para a página inicial
@app.route('/')
def index():
    current_year = datetime.now().year  # Obtém o ano atual
    return render_template('home.html', current_year=current_year)

# Rota para listar clientes do MongoDB
@app.route('/clientes')
def listar_clientes():
    collection = connect_to_mongodb()
    clientes = list(collection.find())  # Busca todos os clientes e converte para lista
    total_fornecedores = collection.count_documents({})  # Conta o número total de fornecedores

    return render_template('cliente.html', clientes=clientes, total_fornecedores=total_fornecedores)

# Rota para adicionar um novo cliente
@app.route('/add', methods=['POST'])
def add_cliente():
    collection = connect_to_mongodb()
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    produto = request.form.get('produto')

    if nome and email and telefone and produto:
        collection.insert_one({'nome': nome, 'email': email, 'telefone': telefone, 'produto': produto})

    return redirect(url_for('listar_clientes'))

# Rota para editar um cliente existente
@app.route('/edit/<cliente_id>', methods=['POST'])
def edit_cliente(cliente_id):
    collection = connect_to_mongodb()
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    produto = request.form.get('produto')

    if nome and email and telefone and produto:
        collection.update_one({'_id': ObjectId(cliente_id)}, {'$set': {'nome': nome, 'email': email, 'telefone': telefone, 'produto': produto}})

    return redirect(url_for('listar_clientes'))

# Rota para excluir um cliente
@app.route('/delete/<cliente_id>', methods=['POST'])
def delete_cliente(cliente_id):
    collection = connect_to_mongodb()
    collection.delete_one({'_id': ObjectId(cliente_id)})

    return redirect(url_for('listar_clientes'))

if __name__ == '__main__':
    app.run(debug=True)
