from prefect import flow, task
import pandas as pd
from scripts.extract import extract_data
from scripts.transform import clean_data
from scripts.load import load_to_postgres

@task
def extract():
    return extract_data('data/raw/Wines.csv')

@task
def transform(data):
    return clean_data(data)

@task
def load(data):
    conn_params = {
        'dbname': 'datalake',
        'user' : 'user',
        'password' : 'password',
        'host' : 'localhost',
        'port' : '5432'
    }
    load_to_postgres(data, 'wine_data', conn_params)

@flow
def wine_pipeline():
    raw_data = extract()
    clean_data = transform(raw_data)
    load(clean_data)

if __name__ == "__main__":
    wine_pipeline()

