from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Настя — Python App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                text-align: center;
                padding-top: 100px;
            }
            .card {
                background: rgba(255,255,255,0.15);
                padding: 40px;
                margin: auto;
                width: 60%;
                border-radius: 20px;
            }
            h1 {
                font-size: 36px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Добро пожаловать!</h1>
            <h2>Python Flask Application</h2>
            <p>Проект Anastasiya Mazur</p>
            <p>Автоматизация CI/CD с использованием Docker</p>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
