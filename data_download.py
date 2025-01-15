import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, period):
    """Загружает исторические данные об акциях."""
    try:
        data = yf.download(ticker, period=period)
        return data
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return None

def add_moving_average(data, window_size=20):
    """Добавляет скользящее среднее в DataFrame."""
    if data is not None:
        data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data