# Use uma imagem base com suporte ao Python
FROM python:3.8-slim

# Configuração do ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Criação do diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY requirements.txt /app/

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código fonte para o diretório de trabalho
COPY . /app/

# Comando para executar a aplicação
CMD ["python", "app.py"]
