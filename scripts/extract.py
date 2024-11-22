import pandas as pd
import requests


def extract_data(filepach: srt) -> pd.DataFrame:
    data = pd.read_csv(filepach)
    return data

def extract_from_api(url: str, params: dict) -> dict:
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
