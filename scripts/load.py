import psycopg2
from psycopg2 import execute_values

def load_to_postgres(data: pd.DataFrame, table_name: str, conn_params: dict):
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursos()
    records = data.to_records(index=False)
    execute_values(cursor, f"INSERT INTO {table_name} VALUES %s", records)
    conn.commit()
    cursor.close()
    conn.close()

