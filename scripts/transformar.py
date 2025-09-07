import logging
import pandas as pd

logging.basicConfig(filename="logs/etl.log", level=logging.INFO)

def transformar(df):
    logging.info("Iniciando a transformação dos dados...")

    # padronizar nomes
    df.columns = [col.lower().strip() for col in df.columns]

    # converter colunas monetárias para float
    money_cols = ["price", "weekly_price", "monthly_price", "security_deposit", "cleaning_fee", "extra_people"]

    for col in money_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col].astype(str)
                    .str.replace(r"[^\d.,]", "", regex=True)
                    .str.replace(",", ".", regex=False),
                errors='coerce'
            )
            
    bool_cols = ["host_is_superhost",
                "host_has_profile_pic", 
                "host_identity_verified", 
                "instant_bookable",
                "is_business_travel_ready",
                "require_guest_profile_picture",
                "require_guest_phone_verification",
                "has_availability"    
                ]
    
    for col in bool_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().isin(["t", "true", "yes", "y"])

    # --- colunas númericas gerais ----
    numeric_cols = ["accommodates", "bathrooms", "bedrooms", "beds",
                    "guests_included", "minimum_nights", "maximum_nights",
                    "number_of_reviews", "reviews_per_month"]
    
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # --- colunas strings gerais ---
    text_cols = ["id","license", "zipcode", "street", "host_id", "host_name", "host_location", "host_listings_count"]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str)

    # --- remover duplicadas ---
    if "ano" in df.columns and "mes" in df.columns:
        df = df.drop_duplicates(subset=["id", "ano", "mes"], keep="last")
    else:
        df = df.drop_duplicates(subset=["id"], keep="last")
    
    logging.info("Transformação concluída")
    return df