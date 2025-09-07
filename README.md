# 📊 Análise de Dados - Copacabana

## 📌 Sobre
Este projeto implementa um **pipeline ETL** para processar e analisar dados do Airbnb em Copacabana, gerando datasets limpos e visualizações exploratórias.

## 🛠️ Tecnologias

- Python 3.12
- Pandas, NumPy
- Matplotilib, Seaborn
- Jupyter Notebook
- Docker

## 📂 Estrutura

|---- dados/ # Dados originais (não versionados), dados tratados pelo ETL
|---- docker/
|---- logs/ # logs de pipeline
|---- notebooks/  # análises exploratórias e gráficos
|---- scripts/ # scripts Python(extrai, transformar, carregar, etl.py)
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
