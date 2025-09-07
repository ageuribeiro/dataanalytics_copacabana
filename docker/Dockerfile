FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cahe -r requirements.txt

COPY scripts/ ./scripts
COPY notebooks/ ./notebooks
COPY dados/ ./dados

CMD ["jupyter", "notebok", "--ip=0.0.0.0", "--port=8888", "--allow-root"]