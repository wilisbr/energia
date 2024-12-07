# Usar uma imagem base oficial Python
FROM python:3.11-slim

# Atualize os pacotes e instale o Git
RUN apt-get update && apt-get install -y \
    git \
    pkg-config \
    build-essential \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código do projeto
#COPY . .

# Configurar variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/gestao_energia

# Expor a porta que o Gunicorn vai usar
EXPOSE 8000

# Comando para rodar o Gunicorn
CMD ["gunicorn", "gestaoEnergia.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
