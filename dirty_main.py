from application.db.people import *
from application.salary import *

from datetime import datetime

if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print(f"Current time: {datetime.utcnow().strftime('%d.%m.%y %H:%M')} UTC")