"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def file_reader(path):
    with open(path, "r") as file:
        csv_reader = csv.reader(file)
        count = 0
        result = []
        for row in csv_reader:
            if count == 0:
                count += 1
            else:
                result.append(row)
                count += 1
    return result


customers_data = file_reader("north_data/customers_data.csv")
employees_data = file_reader("north_data/employees_data.csv")
orders_data = file_reader("north_data/orders_data.csv")

with psycopg2.connect(host="localhost", database="north", user="postgres", password="1") as conn:
    with conn.cursor() as cur:
        for customer in customers_data:
            cur.execute("INSERT INTO customers VALUES(%s, %s, %s)",
                        (customer[0], customer[1], customer[2]))
        for employees in employees_data:
            cur.execute("INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)",
                        (employees[0], employees[1], employees[2],employees[3], employees[4], employees[5]))
        for orders in orders_data:
            cur.execute("INSERT INTO orders VALUES(%s, %s, %s, %s, %s)",
                        (orders[0], orders[1], orders[2], orders[3], orders[4]))

conn.close()
