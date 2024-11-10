print(True or False);
print("milad" and "str");
print("iman" > "am");
print("sara" < "am");
print("Akbar" <= "sakineh");


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "خطا: تقسیم بر صفر ممکن نیست."
    return x / y

print("ماشین حساب ساده")
print("عملیات‌های موجود:")
print("1. جمع")
print("2. تفریق")
print("3. ضرب")
print("4. تقسیم")

while True:
    # گرفتن ورودی کاربر برای انتخاب عملیات
    choice = input("یک عملیات را انتخاب کنید (1/2/3/4) یا 'q' برای خروج: ")

    if choice == 'q':
        print("خروج از برنامه...")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("عدد اول را وارد کنید: "))
            num2 = float(input("عدد دوم را وارد کنید: "))
        except ValueError:
            print("خطا: لطفاً یک عدد معتبر وارد کنید.")
            continue

        if choice == '1':
            print("نتیجه:", add(num1, num2))

        elif choice == '2':
            print("نتیجه:", subtract(num1, num2))

        elif choice == '3':
            print("نتیجه:", multiply(num1, num2))

        elif choice == '4':
            print("نتیجه:", divide(num1, num2))

    else:
        print("ورودی نامعتبر. لطفاً یک عملیات معتبر را انتخاب کنید.")
