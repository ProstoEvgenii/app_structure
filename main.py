from application.salary import *
from application.db.people import get_employees
from datetime import datetime

aa = datetime.today().strftime('%d/%m/%Y')
print(aa)

if __name__ == '__main__':
    print('PyCharm')
    calculate_salary()
    get_employees()
