from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo</title>
    <style>
        /* Fundo da página */
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #e0f2e9; /* Verde suave */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        /* Card central */
        .curriculo-card {
            background-color: #ffffff;
            padding: 40px 50px;
            border-radius: 12px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
            max-width: 600px;
            width: 100%;
        }

        h1 {
            text-align: center;
            color: #2c6f4a; /* Verde escuro para o título */
            margin-bottom: 25px;
        }

        ul {
            list-style: none;
            padding: 0;
        }

        li {
            margin-bottom: 12px;
            line-height: 1.6;
        }

        .titulo {
            font-weight: bold;
            color: #2c6f4a; /* Verde escuro para os títulos dos campos */
        }
    </style>
</head>
<body>
    <div class="curriculo-card">
        <h1>Meu Currículo</h1>
        <ul>
            <li><span class="titulo">Nome:</span> Roger Eduardo Rocha de Souza</li>
            <li><span class="titulo">E-mail:</span> 12502642@aluno.cotemig.com.br</li>
            <li><span class="titulo">Telefone:</span> (11) 98765-4321</li>
            <li><span class="titulo">Ocupação:</span> Estudante - Colégio e Faculdade Cotemig (2017-2019)</li>
            <li><span class="titulo">Educação:</span> Colégio Cotemig - Barroca (Cotemig - MG) <br>
                Cursando 3° Ensino Médio (Fevereiro 2025 - Dezembro 2026)
            </li>
        </ul>
    </div>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
