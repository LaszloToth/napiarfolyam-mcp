
import requests
from fastapi import FastAPI

app = FastAPI()
BASE_URL = "https://www.napiarfolyam.hu"

@app.get("/rates")
def get_rates(currency: str, date: str):
    """
    Fetch exchange rate for a given currency and date.
    Example: /rates?currency=EUR&date=2025-12-03
    """
    url = f"{BASE_URL}/napiapi/rates?currency={currency}&date={date}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

@app.get("/currencies")
def get_currencies():
    """
    Fetch list of available currencies.
    Example: /currencies
    """
    url = f"{BASE_URL}/napiapi/currencies"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
