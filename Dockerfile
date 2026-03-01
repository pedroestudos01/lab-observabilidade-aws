# 1. A nossa imagem base (É um Linux super leve que já traz o Python 3.9 instalado)
FROM python:3.9-slim

# 2. Definimos a pasta de trabalho dentro do contentor (como se fizéssemos um 'cd /app')
WORKDIR /app

# 3. Copiamos apenas o ficheiro de requisitos primeiro (Boa prática para usar o cache do Docker)
COPY requirements.txt .

# 4. Instalamos as bibliotecas (O Flask)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Agora sim, copiamos o nosso código da API para dentro do contentor
COPY app.py .

# 6. Avisamos que o contentor vai comunicar através da porta 5000
EXPOSE 5000

# 7. O comando que será executado quando a máquina ligar
CMD ["python", "app.py"]