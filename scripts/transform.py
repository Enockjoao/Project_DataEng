import duckdb

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    data = data.dropna() #remove linhas com valores nulos
    data['price'] = data['price'].astype(float) #converte o tipo da coluna 'price' para float
    data['points'] = data['points'].astype(int) #converte o tipo da coluna 'points' para int
    return data

def save_to_duckdb(data: pd.DataFrame, db_path: str, table_name: str):
    conn = duckdb.connect(db_path)
    conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM data")
