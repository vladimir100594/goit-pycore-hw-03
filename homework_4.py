from datetime import datetime, timedelta

# Константи для покращення читабельності коду
DAYS_AHEAD = 7
WEEKEND_DAYS = (5, 6)  # субота=5, неділя=6
DATE_FORMAT = "%Y.%m.%d"


def get_upcoming_birthdays(birthdays):
    """
    Знаходить дні народження на наступні 7 днів і переносить їх з вихідних на понеділок.
    
    Args:
        birthdays (list): Список словників з ключами 'name' та 'birthday'
 
    Returns:
        list: Список словників з ключами 'name' та 'congratulation_date'
    """
    if not isinstance(birthdays, list):
        return []
        
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in birthdays:
        if not _is_valid_user(user):
            continue
            
        try:
            birthday = datetime.strptime(user["birthday"], DATE_FORMAT).date()
        except ValueError:
            continue
            
        # Визначаємо день народження в цьому або наступному році
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
        days_until = (birthday_this_year - today).days
        
        # Перевіряємо чи день народження в наступні 7 днів
        if 0 <= days_until <= DAYS_AHEAD:
            congratulation_date = _move_to_next_monday(birthday_this_year)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime(DATE_FORMAT)
            })
    
    return upcoming_birthdays


def _is_valid_user(user):
    """Перевіряє чи користувач має правильну структуру."""
    return (isinstance(user, dict) and 
            "name" in user and 
            "birthday" in user)


def _move_to_next_monday(date):
    """Переносить дату на наступний понеділок, якщо вона припадає на вихідні."""
    if date.weekday() in WEEKEND_DAYS:
        days_to_monday = 7 - date.weekday()
        return date + timedelta(days=days_to_monday)
    return date


def print_upcoming_birthdays(users):
    """Гарно форматує та виводить результати."""
    upcoming = get_upcoming_birthdays(users)
    
    print("Список привітань на цьому тижні:")
    print("=" * 45)
    
    if upcoming:
        for i, person in enumerate(upcoming, 1):
            print(f"{i:2d}. {person['name']:<10} - {person['congratulation_date']}")
    else:
        print("   Немає днів народження на наступні 7 днів")
    
    print("=" * 45)
    print(f"Сьогоднішня дата: {datetime.today().date()}")


if __name__ == "__main__":
    # Тестові дані з різними сценаріями
    test_users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Will Smith", "birthday": "2024.10.12"},      # субота
        {"name": "Brad Pitt", "birthday": "2024.10.13"},       # неділя
        {"name": "Test Invalid", "birthday": "invalid-date"},  # помилкова дата
        {"name": "Future Test", "birthday": "2024.12.25"}      # далеке майбутнє
    ]
    
    # Виводимо результати в гарному форматі
    print_upcoming_birthdays(test_users)