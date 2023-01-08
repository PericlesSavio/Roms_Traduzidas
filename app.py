from flask import Flask, render_template
import pandas as pd


# dados
roms = pd.read_csv('roms.csv', sep=',')
sistemas = roms[['sistema', 'sistema_slug']]
lista_sistemas = sistemas.drop_duplicates()
n_jogos_sistemas = roms[['jogo', 'sistema']].groupby(['sistema']).count().reset_index()
n_jogos_generos = roms[['jogo', 'genero']].groupby(['genero']).count().reset_index()


# aplicação
app = Flask(__name__)

@app.route('/')
@app.route('/sistema')
@app.route('/sistema/')
@app.route('/genero')
@app.route('/genero/')
def index():    
     return render_template('index.html',
        index = 1,
        roms = roms.to_dict('records'),
        n_jogos_sistemas = n_jogos_sistemas.to_dict('records'),
        n_jogos_generos = n_jogos_generos.to_dict('records'),
        sistemas = roms[['sistema', 'sistema_slug']].drop_duplicates().to_dict('records'),
        generos = roms[['genero', 'genero_slug']].drop_duplicates().to_dict('records'),
        )


@app.route('/sistema/<_sistema_>')
def sistema(_sistema_):    
     return render_template('index.html',
        index = 0,
        titulo = roms[roms['sistema_slug'] == _sistema_]['sistema'].values[0],
        roms = roms[roms['sistema_slug'] == _sistema_].to_dict('records'),
        sistemas = roms[['sistema', 'sistema_slug']].drop_duplicates().to_dict('records'),
        generos = roms[['genero', 'genero_slug']].drop_duplicates().to_dict('records'),
        )

@app.route('/genero/<_genero_>')
def genero(_genero_):    
     return render_template('index.html',
        index = 0,
        titulo = roms[roms['genero_slug'] == _genero_]['genero'].values[0],
        roms = roms[roms['genero_slug'] == _genero_].to_dict('records'),
        sistemas = roms[['sistema', 'sistema_slug']].drop_duplicates().to_dict('records'),
        generos = roms[['genero', 'genero_slug']].drop_duplicates().to_dict('records'),
        )


if __name__ == '__main__':
    app.run(debug=True)