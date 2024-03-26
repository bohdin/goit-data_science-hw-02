import psycopg2
import faker
from random import randint


def generate_fake_data(number_users, number_tasks) -> tuple():
    # Ініціалізація фейкера для генерації випадкових даних
    fake_data = faker.Faker()

    # Генерація випадкових даних для працівників
    fake_users = []
    for _ in range(number_users):
        fake_users.append((fake_data.name(), fake_data.email()))

    # Генерація випадкових даних для завдань
    fake_tasks = []
    for _ in range(number_tasks):
        fake_tasks.append((fake_data.text(max_nb_chars=100), fake_data.text(), randint(1, 3), randint(1, number_users)))

    # Статуси для завдань
    fake_status = [('new', ), ('in progress', ), ('completed', )]
    return fake_users, fake_tasks, fake_status

def insert_data_to_db(users, tasks, status) -> None:
    # Підключення до бази даних PostgreSQL
    with psycopg2.connect(dbname='postgres', user='postgres', password='tsviliy2222', host='localhost') as con:
        cur = con.cursor()

        # Вставка даних в таблицю users
        sql_to_users = """
        INSERT INTO users(fullname, email)VALUES (%s, %s)
        """
        cur.executemany(sql_to_users, users)

        # Вставка даних в таблицю status
        sql_to_status = """
        INSERT INTO status(name)VALUES (%s)
        """
        cur.executemany(sql_to_status, status)

        # Вставка даних в таблицю tasks
        sql_to_tasks = """
        INSERT INTO tasks(title, description, status_id, user_id)VALUES (%s,%s,%s,%s)
        """
        cur.executemany(sql_to_tasks, tasks)

        # Збереження змін у базі даних
        con.commit()

if __name__ == "__main__":
    # Генерація випадкових даних
    users, tasks, status = generate_fake_data(40, 100)

    # Вставка випадкових даних до бази даних
    insert_data_to_db(users, tasks, status)

