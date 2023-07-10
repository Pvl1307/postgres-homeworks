"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os

# Пароль от PG из переменных окружения
password = os.getenv('PG_Admin')

# Пути к CSV файлам
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_employees = os.path.join(script_dir, 'north_data', 'employees_data.csv')
csv_customers = os.path.join(script_dir, 'north_data', 'customers_data.csv')
csv_orders = os.path.join(script_dir, 'north_data', 'orders_data.csv')

# Подключение к БД
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password=password
)

# Создание курсора
cur = conn.cursor()

# Загрузка данных из CSV файла employees_data.csv
with open(csv_employees, 'r', encoding='utf-8') as employees:
    reader = csv.reader(employees)
    next(reader)  # Пропуск заголовка

    for row in reader:
        employee_id, first_name, last_name, title, birth_date, notes = row

        # Выполнение запроса
        cur.execute('INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) '
                    'VALUES (%s, %s, %s, %s, %s, %s)',
                    (employee_id, first_name, last_name, title, birth_date, notes))

# Загрузка данных из CSV файла customers_data.csv
with open(csv_customers, 'r', encoding='utf-8') as customers:
    reader = csv.reader(customers)
    next(reader)  # Пропуск заголовка

    for row in reader:
        customer_id, company_name, contact_name = row

        # Выполнение запроса
        cur.execute('INSERT INTO customers (customer_id, company_name, contact_name) '
                    'VALUES (%s, %s, %s)',
                    (customer_id, company_name, contact_name))

# Загрузка данных из CSV файла orders_data.csv
with open(csv_orders, 'r', encoding='utf-8') as orders:
    reader = csv.reader(orders)
    next(reader)  # Пропуск заголовка

    for row in reader:
        order_id, customer_id, employee_id, order_date, ship_city = row

        # Выполнение запроса
        cur.execute('INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) '
                    'VALUES (%s, %s, %s, %s, %s)',
                    (order_id, customer_id, employee_id, order_date, ship_city))

# Фиксация изменений и закрытие курсора
conn.commit()
cur.close()

# Закрытие соединения
conn.close()
