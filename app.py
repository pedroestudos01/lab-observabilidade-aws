from flask import Flask, jsonify
from flask_cors import CORS  # <-- NOVA LINHA AQUI
import time
import math

app = Flask(__name__)
CORS(app) # <-- NOVA LINHA AQUI (Isso libera a alfândega para o S3!)
# Rota 1: Tudo certo (Para gerar logs de sucesso - 200 OK)
@app.route('/')
def home():
    return jsonify({"status": "sucesso", "mensagem": "API rodando perfeitamente!"}), 200

# Rota 2: O Caos (Para testarmos Alertas de Erro no CloudWatch/Datadog - 500 Error)
@app.route('/erro')
def erro_intencional():
    # Isso vai forçar um erro de divisão por zero!
    1 / 0 
    return "Isso nunca vai aparecer", 500

# Rota 3: Lentidão (Para testarmos latência e APM no Datadog)
@app.route('/lento')
def rota_lenta():
    time.sleep(3) # Pausa a aplicação por 3 segundos
    return jsonify({"status": "sucesso", "mensagem": "Isso demorou 3 segundos!"}), 200

# Rota 4: Estresse de CPU (Para forçar o Auto Scaling a criar novas máquinas depois)
@app.route('/stress')
def estresse_cpu():
    resultado = 0
    # Um loop matemático pesado para queimar CPU
    for i in range(1, 5000000):
        resultado += math.sqrt(i)
    return jsonify({"status": "sucesso", "mensagem": "CPU fritando!"}), 200

if __name__ == '__main__':
    # Roda na porta 5000, acessível de qualquer IP (0.0.0.0)
    app.run(host='0.0.0.0', port=5000)