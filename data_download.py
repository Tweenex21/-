import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    """
    Вычисляет и выводит среднюю цену закрытия акций.
    :param data: DataFrame с историческими данными акций
    """
    if 'Close' in data.columns:
        average_price = data['Close'].mean()
        print(f"Средняя цена закрытия за период: {average_price:.2f}")
    else:
        print("Данные о ценах отсутствуют.")

