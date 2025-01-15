import matplotlib.pyplot as plt

def create_and_save_plot(data, ticker, period, filename=None):
    """Создаёт и сохраняет график."""
    if data is not None:
        plt.figure(figsize=(10, 6))
        plt.plot(data['Close'], label='Цена закрытия')
        plt.plot(data['Moving_Average'], label='Скользящее среднее')
        plt.title(f"{ticker} Цены за {period}")
        plt.xlabel("Дата")
        plt.ylabel("Цена")
        plt.legend()
        if filename:
            plt.savefig(filename)
        else:
            plt.savefig(f"{ticker}_{period}.png")
        plt.show()