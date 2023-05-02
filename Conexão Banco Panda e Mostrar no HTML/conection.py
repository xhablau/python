import pandas as pd
from flask import Flask, render_template

# Carrega os dados do arquivo CSV ou do banco de dados em um DataFrame do Pandas
df = pd.read_csv('meu_dataframe.csv') # ou substitua com a conexão do seu banco de dados

# Cria um aplicativo Flask
app = Flask(__name__)

# Cria uma rota para exibir os dados em uma página HTML
@app.route('/')
def index():
    return render_template('index.html', data=df.to_html())

# Inicia o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)


