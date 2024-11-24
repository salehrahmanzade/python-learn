import math
# ---------------  1 -----------------
def calculate_bmi(weight, height):
    """Calculate Body Mass Index (BMI)"""
    if height <= 0:
        return "Height must be greater than 0."
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """Determine the BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# User input
try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    if isinstance(bmi, str):
        print(bmi)  # Error message if height is invalid
    else:
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {bmi_category(bmi)}")
except ValueError:
    print("Please enter valid numeric inputs.")

# ---------------  2 -----------------
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def tavan(x, y):
    return x ** y

def divide(x, y):
    if y == 0:
        return "خطا: تقسیم بر صفر ممکن نیست."
    return x / y

def logaritm(x):
    return math.log(x)

def jazr(x):
    return math.sqrt(x)

def cosinos(x):
    # تبدیل زاویه به رادیان
    angle_radians = math.radians(x)
    return math.cos(angle_degrees)

def sinos(x):
        # تبدیل زاویه به رادیان
    angle_radians = math.radians(x)
    return math.sin(angle_radians)

def tan(x):
        # تبدیل زاویه به رادیان
    angle_radians = math.radians(x)
    return math.tan(angle_radians)



print("ماشین حساب ساده")
print("عملیات‌های موجود:")
print("1. جمع")
print("2. تفریق")
print("3. ضرب")
print("4. تقسیم")
print("5. توان")
print("6. لگ")
print("7. جزر")
print("8. کسینوس")
print("9. سینوس")
print("10. تانژان")

while True:
    # گرفتن ورودی کاربر برای انتخاب عملیات
    choice = input("یک عملیات را انتخاب کنید (1/2/3/4/5/6/7/8/9/10) یا 'q' برای خروج: ")

    if choice == 'q':
        print("خروج از برنامه...")
        break

    if choice in ('1', '2', '3', '4','5','6','7','8','9','10'):
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
            
        elif choice == '5':
            print("نتیجه:", tavan(num1, num2))  

        elif choice == '6':
            print("نتیجه:", logaritm(num1))  

        elif choice == '7':
            print("نتیجه:", jazr(num1))  

        elif choice == '8':
            print("نتیجه:", cosinos(num1)) 

        elif choice == '9':
            print("نتیجه:", sinos(num1)) 

        elif choice == '10':
            print("نتیجه:", tan(num1)) 

    else:
        print("ورودی نامعتبر. لطفاً یک عملیات معتبر را انتخاب کنید.")









 # ---------------  3 -----------------

def clac3(x,y,z):
    sq = math.sqrt((x-y)/z)
    ee = math.exp(x+y)
    return print(sq+ee)

 # ---------------  4 -----------------
def calc4(x,r):
    return print(r*x*(1-x))

 # ---------------  5 -----------------
def calc5(w2,w1,k):
    r = w2-(((w2-w1)/k)*k)
    return print(r)

 # ---------------  6 -----------------
def calc5(w2,w1,a,b):
    y = (1/(math.exp(a-b)+1))*(w2-w1)
    return print(y)

 # ---------------  7 -----------------
def calc5(f2,f1):
    y = (f2-f1)/f2
    return print(y)