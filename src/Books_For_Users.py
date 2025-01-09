import csv
import json
from files import JSON_FILE_PATH, CSV_FILE_PATH

# Списки для хранения данных
books_list = []
users_list = []

# Чтение пользователей из JSON файла
with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
    users = json.load(f)
    for user in users:
        users_list.append({
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": []  # Инициализация пустого списка для книг
        })

# Чтение книг из CSV файла
with open(CSV_FILE_PATH, newline="", encoding="utf-8") as data:
    for row in csv.DictReader(data):
        books_list.append({
            "title": row.get("Title"),
            "author": row.get("Author"),
            "pages": int(row.get("Pages")),
            "genre": row.get("Genre")
        })

# Распределение книг между пользователями
while books_list:
    for user in users_list:
        if not books_list:
            break
        user["books"].append(books_list.pop(0))  # Добавление книги в список

# Запись результата в JSON файл
with open("result.json", "w", encoding="utf-8") as final_json:
    json.dump(users_list, final_json, indent=4, ensure_ascii=False)
