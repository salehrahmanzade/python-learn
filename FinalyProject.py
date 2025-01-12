import json
# 
 
# پروژه مدیریت کتابخانه محمد صالح رحمان زاده

# فایل جیسون برای ذخیره‌سازی کتاب‌ها
DATA_FILE = 'books.json'

# دریافت یا لود داده‌ها از فایل جیسون ذخیره کتاب ها 
def load_books():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#  ذخیره‌سازی داده‌ها در فایل بوک جیسون
def save_books(books):
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

# افزودن کتاب جدید
def add_book():
    title = input("عنوان کتاب: ")
    author = input("نویسنده: ")
    year = input("سال انتشار: ")
    books = load_books()
    books.append({"title": title, "author": author, "year": year, "status": "موجود"})
    save_books(books)
    print(f'کتاب "{title}" با موفقیت اضافه شد!')

# نمایش لیست کتاب‌ها
def view_books():
    books = load_books()
    if books:
        for i, book in enumerate(books, 1):
            print(f'{i}. {book["title"]} - نویسنده: {book["author"]} - سال: {book["year"]} - وضعیت: {book["status"]}')
    else:
        print("هیچ کتابی موجود نیست.")

# جستجوی کتاب
def search_book():
    query = input("عبارت جستجو: ").lower()
    books = load_books()
    results = [book for book in books if query in book['title'].lower() or query in book['author'].lower()]
    if results:
        for book in results:
            print(f'{book["title"]} - نویسنده: {book["author"]} - سال: {book["year"]} - وضعیت: {book["status"]}')
    else:
        print("کتابی یافت نشد.")

# امانت کتاب
def borrow_book():
    title = input("عنوان کتاب برای امانت: ")
    books = load_books()
    for book in books:
        if book['title'] == title and book['status'] == 'موجود':
            book['status'] = 'امانت داده‌شده'
            save_books(books)
            print(f'کتاب "{title}" با موفقیت امانت داده شد!')
            return
    print("کتاب مورد نظر موجود نیست یا قبلاً امانت داده شده است.")

# بازگرداندن کتاب
def return_book():
    title = input("عنوان کتاب برای بازگرداندن: ")
    books = load_books()
    for book in books:
        if book['title'] == title and book['status'] == 'امانت داده‌شده':
            book['status'] = 'موجود'
            save_books(books)
            print(f'کتاب "{title}" با موفقیت بازگردانده شد!')
            return
    print("کتاب مورد نظر قبلاً بازگردانده شده یا وجود ندارد.")

# حذف کتاب
def delete_book():
    title = input("عنوان کتاب برای حذف: ")
    books = load_books()
    new_books = [book for book in books if book['title'] != title]
    save_books(new_books)
    print(f'کتاب "{title}" با موفقیت حذف شد!')

# منوی اصلی
def main():
    while True:
        print("\n*** سیستم مدیریت کتابخانه ***")
        print("1. افزودن کتاب جدید")
        print("2. مشاهده لیست کتاب‌ها")
        print("3. جستجوی کتاب")
        print("4. امانت کتاب")
        print("5. بازگرداندن کتاب")
        print("6. حذف کتاب")
        print("7. خروج")
        choice = input("لطفاً یک گزینه انتخاب کنید: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            delete_book()
        elif choice == '7':
            print("خروج از برنامه.")
            break
        else:
            print("گزینه نامعتبر است. لطفاً دوباره تلاش کنید.")

#  اجرای مستقیم اسکریپت
if __name__ == "__main__":
    main()
