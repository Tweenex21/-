from data_download import fetch_stock_data, add_moving_average
from data_plotting import create_and_save_plot


def main():
    ticker = input("Введите тикер акции (например, 'AAPL'): ")
    period = input("Введите временной период (например, '1mo'): ")

    data = fetch_stock_data(ticker, period)
    if data is not None:
        data = add_moving_average(data)
        create_and_save_plot(data, ticker, period)


if __name__ == "__main__":
    main()