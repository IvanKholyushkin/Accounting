from application.salary import calculate_salary
from application.db import get_employees

from datetime import datetime

if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print(f"Current time: {datetime.utcnow().strftime('%d.%m.%y %H:%M')} UTC")
