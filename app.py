from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


# Dados simulados de criptomoedas
cryptos = [
    {"name": "Bitcoin", "symbol": "BTC", "price": 57000},
    {"name": "Ethereum", "symbol": "ETH", "price": 3600},
    {"name": "Binance Coin", "symbol": "BNB", "price": 500},
]

@app.route('/')
def home():
    ab =" sidao"
    brind= ''' 
            fgsdfgsdf
            asdfasdf
            dsfsda
            dfasd
            fa
                        ''' f'{ab}' '''
        '''    

    print(brind)
    return render_template('index.html', cryptos=cryptos)



@app.route('/pg1')
def pg1():
    return render_template('pagina1.html', cryptos=cryptos)


@app.route('/pgEx')
def pgEx():
    return render_template('exemploDATATABLE.html')


@app.route("/fetch")
def fetch():
    # Criando o DataFrame
    data = {
        "codigo": [101, 102, 103],
        "Juncao": ["Dept A", "Dept B", "Dept C"],
        "Juncao": ["Dept A", "Dept B", "Dept C"],
        "Juncao": ["Dept A", "Dept B", "Dept C"],
        "nm_func": ["Alice", "Bob", "Carlos"]
    }

    df = pd.DataFrame(data)
    # Exibindo o DataFrame
    print(df)

    return df.to_json(orient='records')


@app.route("/usuario/<usuario>")
def validaUsuario(usuario):
    return render_template("Usuario.html", nm_usu = usuario) 
    

if __name__ == '__main__':
    app.run(debug=True)
