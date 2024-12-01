import math
# محاسبه قدر مطلق یک عدد مثبت
print(abs(10))  # خروجی: 10

# محاسبه قدر مطلق یک عدد منفی
print(abs(-5))  # خروجی: 5

# محاسبه قدر مطلق یک عدد اعشاری
print(abs(-3.14))  # خروجی: 3.14

def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num

# نمونه استفاده
print(absolute_value(-7))   # خروجی: 7
print(absolute_value(4))    # خروجی: 4
print(absolute_value(int(input("یک عدد وارد کنید"))))    # عدد از کاربر : 4


##############################################################################

def fahrenheit_to_celsius():
    fahrenheit = float(input("دمای فارنهایت را وارد کنید: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit} درجه فارنهایت برابر است با {celsius:.2f} درجه سلسیوس.")

fahrenheit_to_celsius()


def pounds_to_grams():
    pounds = float(input("وزن به پوند را وارد کنید: "))
    grams = pounds * 453.592
    print(f"{pounds} پوند برابر است با {grams:.2f} گرم.")

pounds_to_grams()


def feet_to_centimeters():
    feet = float(input("طول به فوت را وارد کنید: "))
    centimeters = feet * 30.48
    print(f"{feet} فوت برابر است با {centimeters:.2f} سانتی‌متر.")

feet_to_centimeters()

def convert_units():
    print("انتخاب کنید:")
    print("1: تبدیل فارنهایت به سلسیوس")
    print("2: تبدیل پوند به گرم")
    print("3: تبدیل فوت به سانتی‌متر")
    
    choice = input("انتخاب خود را وارد کنید (1/2/3): ")
    
    if choice == "1":
        fahrenheit_to_celsius()
    elif choice == "2":
        pounds_to_grams()
    elif choice == "3":
        feet_to_centimeters()
    else:
        print("انتخاب نامعتبر است.")

# اجرای برنامه
convert_units()


##############################################################################
a = int(input("عدد a را وارد کنید"))
b = int(input("عدد b را وارد کنید"))

if a < 0:
    print(1/(math.exp(-a)+1))
elif a > 1:
    print(1/(1+math.exp(-a)))


if(a>b):
   print( math.sqrt(a**2-b**2))
elif(b<a):
   print( math.sqrt(b**2-a**2))
else:
    print(a-b)

if(a>0):
   print("mosbat")
elif(a<0):
   print("manfi")
else:
    print("mosavi")
