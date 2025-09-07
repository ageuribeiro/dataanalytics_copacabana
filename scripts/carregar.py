import logging
from pathlib import Path

logging.basicConfig(filename="logs/etl.log", level=logging.INFO)

PROCESSED_PATH = Path("../dados/processed/")
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

def carregar(df_mensal, df_total=None):
    logging.info("Iniciando o carregamento dos dados...")

    # Colunas que costumam causar erro no parquet
    text_cols = ["id", "license", "host_listings_count", "host_total_listings_count"]

    for col in text_cols:
        if col in df_mensal.columns:
            df_mensal[col] = df_mensal[col].astype(str)
        if df_total is not None and col in df_total.columns:
            df_total[col] = df_total[col].astype(str)

        print(df_mensal.columns)
        break
    # salvar todos os mensais consolidados
    df_mensal.to_parquet(PROCESSED_PATH / "listing_mensal.parquet", index=False, engine='pyarrow')
    df_mensal.to_csv(PROCESSED_PATH / "listing_mensal.csv", index=False)

    # salvar total (gigante)]
    if df_total is not None:
        df_total.to_parquet(PROCESSED_PATH / "listing_total.parquet", index=False, engine='pyarrow')
        df_total.to_csv(PROCESSED_PATH / "listing_total.csv", index=False)

    # criar dataset curado com apenas colunas essenciais
    cols_essenciais = ["id", "ano", "mes", "neighbourhood_cleansed", "room_type", "price", "number_of_reviews", "reviews_scores_rating"]
    df_curado = df_mensal[cols_essenciais]
    df_curado.to_parquet(PROCESSED_PATH / "listing_mensal_curado.parquet", index=False, engine='pyarrow')
    df_curado.to_csv(PROCESSED_PATH / "listing_mensal_curado.csv", index=False)

    logging.info("Carga concluída")