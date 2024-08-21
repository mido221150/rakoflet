import requests
from bs4 import BeautifulSoup

class NutritionItem:
    def __init__(self, name, calories, nutrients):
        self.name = name
        self.calories = calories
        self.nutrients = nutrients

    def __str__(self):
        return f"{self.name} - السعرات الحرارية: {self.calories} ، المغذيات: {', '.join(self.nutrients)}"

class NutritionApp:
    def __init__(self):
        self.food_items = []
        self.load_food_data()

    def load_food_data(self):
        # URL للحصول على بيانات الأطعمة
        url = "https://www.example.com/food-data"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # استخراج بيانات الأطعمة من الصفحة
        for food_row in soup.find_all("tr"):
            cells = food_row.find_all("td")
            if len(cells) == 3:
                name = cells[0].text.strip()
                calories = int(cells[1].text.strip())
                nutrients = [nut.strip() for nut in cells[2].text.strip().split(",")]
                food_item = NutritionItem(name, calories, nutrients)
                self.food_items.append(food_item)

    def add_food_item(self):
        name = input("اسم الطعام: ")
        calories = int(input("السعرات الحرارية: "))
        nutrients = input("المغذيات (مفصولة بفواصل): ").split(",")
        nutrients = [nut.strip() for nut in nutrients]
        food_item = NutritionItem(name, calories, nutrients)
        self.food_items.append(food_item)
        print(f"تمت إضافة: {food_item}")

    def display_food_items(self):
        if not self.food_items:
            print("لا توجد عناصر طعام متاحة.")
        else:
            print("عناصر الطعام:")
            for item in self.food_items:
                print(item)

    def interactive_menu(self):
        while True:
            print("\nالقائمة:")
            print("1. إضافة عنصر غذائي")
            print("2. عرض عناصر الطعام")
            print("3. الخروج")
            choice = input("اختر خيارًا: ")

            if choice == '1':
                self.add_food_item()
            elif choice == '2':
                self.display_food_items()
            elif choice == '3':
                print("شكرًا لاستخدامك تطبيق التغذية العلاجية.")
                break
            else:
                print("خيار غير صالح ، يرجى المحاولة مرة أخرى.")

if __name__ == "__main__":
    app = NutritionApp()
    app.interactive_menu()
