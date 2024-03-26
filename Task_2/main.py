from pymongo import MongoClient
from pymongo.server_api import ServerApi


class Cat_db:
    def __init__(self, link: str) -> None:
        # Підключення до бази даних MongoDB за вказаним посиланням
        client = MongoClient(link, server_api=ServerApi("1"))
        self.__db = client.book.cats

    def Create_one(self, name: str, age: int, features: list) -> None:
        # Створення одного документа у колекції з вказаними даними про кота
        result = self.__db.insert_one({"name": name, "age": age, "features": features})

        if result.inserted_id:
            print(f"Кіт {name} створений успішно")
        else:
            print("Помилка при створенні кота")

    def Create_many(self, cats: list[dict]) -> None:
         # Створення багатьох документів у колекції з вказаними даними про котів
        result = self.__db.insert_many(cats)

        if result.inserted_ids:
            print(f"Створено {len(result.inserted_ids)} котів успішно")
        else:
            print("Помилка при створенні котів")

    def Read_all(self) -> None:
        # Читання всіх документів у колекції та виведення їхньої інформації
        cats = self.__db.find({})

        for cat in cats:
            print("Ім'я:", cat["name"])
            print("Вік:", cat["age"])
            print("Характеристики:", cat["features"])

    def Read_by_name(self, name: str) -> None:
        # Пошук та виведення інформації про кота за його ім'ям
        cat = self.__db.find_one({"name": name})
        if cat:
            print("Ім'я:", cat["name"])
            print("Вік:", cat["age"])
            print("Характеристики:", cat["features"])
        else:
            print("Кіт з ім'ям", name, "не знайдено")

    def Update_age(self, name: str, new_age: int) -> None:
        # Оновлення віку кота за його ім'ям
        result = self.__db.update_one({"name": name}, {"$set": {"age": new_age}})

        if result.modified_count:
            print("Вік кота з ім'ям", name, "оновлено успішно")
        else:
            print("Кіт з ім'ям", name, "не знайдено")

    def Add_feature(self, name: str, new_feature: str) -> None:
        # Додавання нової характеристики до списку features кота за його ім'ям
        result = self.__db.update_one(
            {"name": name}, {"$push": {"features": new_feature}}
        )

        if result.modified_count:
            print("Нова характеристика додана до кота з ім'ям", name)
        else:
            print("Кіт з ім'ям", name, "не знайдено")

    def Delete_by_name(self, name: str):
        # Видалення документа з колекції за ім'ям кота
        result = self.__db.delete_one({"name": name})

        if result.deleted_count:
            print("Кота з ім'ям", name, "видалено успішно")
        else:
            print("Кіт з ім'ям", name, "не знайдено")

    def Delete_all(self):
        # Видалення всіх документів у колекції
        result = self.__db.delete_many({})

        print(
            f"Всі записи про котів видалено. Кількість видалених документів: {result.deleted_count}"
        )


if __name__ == "__main__":
    # Підключення до бази даних та створення екземпляру класу Cat_db
    cats = Cat_db("mongodb+srv://goitlearn:1234@cluster0.pwocrpk.mongodb.net/")

    # Створення котів
    cats.Create_one("Барсік", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    cats.Create_one("Мурзік", 5, ["спить на дереві", "любить мишей", "сірий"])
    new_cats = [
        {"name": "Том", "age": 2, "features": ["муркотить", "грається з м'ячем"]},
        {"name": "Віскер", "age": 4, "features": ["любить рибу", "ловить мишей"]},
    ]
    cats.Create_many(new_cats)

    # Читання всіх котів та пошук за ім'ям
    cats.Read_all()
    cats.Read_by_name("Барсік")

    # Оновлення віку та додавання характеристики
    cats.Update_age("Барсік", 4)
    cats.Add_feature("Барсік", "любить спати на дивані")

    # Видалення кота за ім'ям та всіх котів
    cats.Delete_by_name("Барсік")
    cats.Delete_all()
