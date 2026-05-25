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
    pass

def save_books(books):
    pass

def main():
    while True:
        # показать меню
        # вызвать нужную функцию
        break

if __name__ == "__main__":
    main()
