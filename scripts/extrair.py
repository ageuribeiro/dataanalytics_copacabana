import pandas as pd
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_PATH = BASE_DIR / "dados" / "raw"
PROCESSED_PATH = BASE_DIR / "dados" / "processed"
LOGS_PATH = BASE_DIR / "logs"

# Garante que as pastas existam
RAW_PATH.mkdir(parents=True, exist_ok=True)
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
LOGS_PATH.mkdir(parents=True, exist_ok=True)

# Configuração de logs
logging.basicConfig(filename="../logs/etl.log", level=logging.INFO)

def extrair_mensais():
    logging.info("Iniciando extração dos arquivos mensais...")
    mensais = []
    for file in RAW_PATH.glob("*.csv"):
        if "total" not in file.stem.lower():
            df = pd.read_csv(file, delimiter=",")
            # extrair ano e mês do nome do arquivo
            parts = file.stem.split("_")
            if len(parts) >= 3:
                df["ano"] = int(parts[1])
                df["mes"] = int(parts[2])
            df["origem"] = "mensal"
            mensais.append(df)
            logging.info(f"{file.name}: {df.shape[0]} registros.")
    
    df_mensal = pd.concat(mensais, ignore_index=True)
    logging.info(f"Total de registros mensais consolidados: {df_mensal.shape[0]}")
    return df_mensal

def extrair_total(chunksize=500_000):
    logging.info("Iniciando extração do arquivo total em chunks...")
    total_file = next(RAW_PATH.glob("*total*.csv"), None)
    if total_file is None:
        logging.warning("Arquivo total não econtrado")
        return None

    chunks = []
    for chunk in pd.read_csv(total_file, chunksize=chunksize, low_memory=False):
        chunks.append(chunk)
        logging.info(f"Chunk lido: {chunk.shape[0]} registros")
    df_total = pd.concat(chunks, ignore_index=True)
    df_total["origem"] = "total"
    logging.info(f"Total de registros no arquivo total: {df_total.shape[0]}")
    return df_total
            
