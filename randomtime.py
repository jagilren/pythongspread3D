from datetime import datetime, timedelta
import random

def get_random_datetime_in_current_month():
    # Get the current date and time
    now = datetime.now()

    # Calculate the first day of the current month
    first_day_of_month = now.replace(day=1)

    # Calculate the last day of the current month
    last_day_of_month = (first_day_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    # Generate a random date within the current month
    random_date = first_day_of_month + timedelta(days=random.randint(0, (last_day_of_month - first_day_of_month).days))

    # Generate random hours, minutes, and seconds
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)

    # Combine the random date with the random time
    random_datetime = random_date.replace(hour=random_hour, minute=random_minute, second=random_second)

    return random_datetime

# Example usage
random_datetime = get_random_datetime_in_current_month()
print("Random Datetime in Current Month:", random_datetime)
