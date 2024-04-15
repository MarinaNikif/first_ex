def calculate_and_display_average_price(data):
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия акций за заданный период: {average_price:.3f}")


def notify_if_strong_fluctuations(data, threshold):
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    price_diff = (max_price - min_price) / min_price * 100

    if price_diff > threshold:
        print(f"Цена акций колебалась более чем на {threshold}% за период.")
    else:
        print("Колебания цены акций не превысили заданный порог.")


def export_data_to_csv(data, filename):
    data.to_csv(filename, index=False)
    print(f"Данные сохранены в файл {filename}")
