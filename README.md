# 📊 Análise de Dados - Copacabana

## 📌 Sobre
Este projeto realiza uma análise exploratória de dados sobre a região de Copacabana, com foco em identificar padrões, tendências e gerar visualizações.

## 🛠️ Tecnologias

- Python 3.12
- Pandas, NumPy
- Matplotilib, Seaborn
- Jupyter Notebook
- Docker

## 📂 Estrutura

|---- dados/
|---- docker/
|---- logs/
|---- notebooks/
|---- scripts/
|---- .gitignore
|---- LICENSE
|---- README.md
|---- requirements.txt

## ⚙️ Como Executar

1️⃣ Clonar repositório
```bash
git clone https://github.com/ageuribeiro/dataanalytics_copacabana.git
cd dataanalytics_copacabana
```

2️⃣ Subir ambiente com Docker
```bash
docker build -t copacabana .
docker run -p 8888:8888 copacabana
```

3️⃣ Acessar o Jupyter
Abra no navegador de sua preferência: http://localhost:8888

📊 Exemplos de Visualização

✅ Resultados
* Exploração inicial do dataset Copacabana
* Estatísticas descritivas
* Visualizações para padrões e insights

📜 Licenças
MIT License
