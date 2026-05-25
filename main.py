import json
import os
books_json = "books.json"

def list_books(books):
    """Отображение списка книг"""
    if not books:
        print("\nКниги не найдены")
        return None
    print("-" * 80)
    for i, book in enumerate(books, 1):
        print(f"{book['name']:<15}")
def stats_books(books):
    if len(books) != 0:
        count = len(books)
    sum_rating = 0
    average = 0
    for i in range(len(books)):
        sum_rating += books[i]["rating"]
    average = (sum_rating/count)
    print(average)
def stats_author(books):
    kolvo = 0
    author_kolvo = {}
    for i in range(len(books)):
        if books[i]["author"] in author_kolvo:
            author_kolvo[books[i]["author"]] += 1
        else:
            author_kolvo[books[i]["author"]] = 1
    print(author_kolvo)
def add_book(books):
    numbers = [1, 2, 3, 4, 5]
    """Добавление новой книги"""
    print("\nДобавление новой книги:")
    author = input("Введите имя автора: ").strip()
    name = input("Введите назвние книги: ").strip()
    rating = int(input("Введите оценку книги от 1 до 5: ").strip())
    while not rating in numbers:
        rating = int(input("Введите оценку книги от 1 до 5: ").strip())
    time = input("Введите дату создания книги: ").strip()
    book = {"author": author,
            "name": name,
            "rating": rating, 
            "time": time
            }
    books.append(book)
    save_books(books)
    print("Книга успешно добавлена!")

def load_books():
    if os.path.exists(books_json):
        with open(books_json, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_books(books):
    with open(books_json, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=2)

def main():
    """Главная функция программы"""
    books = load_books()
    while True:
        print("\n" + "=" * 50)
        print("Трекер прочитанных книг")
        print("=" * 50)
        print("1. Добавление книги")
        print("2. Показать список книг")
        print("3. Показать среднюю оценку книг")
        print("4. Количество книг каждого автора")
        print("5. Удалить книгу")
        print("6. Выход")
        print("-" * 50)
        choise = input("Выберите действие (1-6): ").strip()
        if choise == "1":
            add_book(books)
        elif choise == "2":
            list_books(books)
        elif choise == "3":
            stats_books(books)
        elif choise == "4":
            stats_author(books)
        elif choise == "5":
            delete_book(books)
        elif choise == "6":
            break
if __name__ == "__main__":
    main()
