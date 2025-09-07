from extrair import extrair_mensais, extrair_total
from transformar import transformar
from carregar import carregar

if __name__ == "__main__":
    df_mensal = extrair_mensais()
    df_total = extrair_total()

    df_mensal = transformar(df_mensal)
    if df_mensal is not None:
        df_total = transformar(df_total)

    carregar(df_mensal, df_total)