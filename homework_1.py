import datetime

def get_days_from_today (date):
    if not isinstance(date, str):
        raise TypeError("Параметр повинен бути рядком")
    try:
        # тут буде парсинг дати
        given_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        given_date = given_date.date()
        today = datetime.date.today()
        difference = today - given_date
        return difference.days
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'YYYY-MM-DD'")
# тестування функції
if __name__ == "__main__":
    print(get_days_from_today("2020-10-09"))
    print(get_days_from_today("2025-12-31"))
    try:
        print(get_days_from_today("2020/10/09"))
    except ValueError as e:
        print(f"Помилка: {e}")

    