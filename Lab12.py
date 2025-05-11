import json

# Початкові дані
employees = [
    {"Surname": "Shevchenko", "Address": "Kyiv, Hrushevskoho 1", "Position": "Manager"},
    {"Surname": "Kovalenko", "Address": "Lviv, Franka 22", "Position": "Engineer"},
    {"Surname": "Bondarenko", "Address": "Odesa, Deribasivska 10", "Position": "Analyst"},
    {"Surname": "Tkachenko", "Address": "Kharkiv, Svobody 15", "Position": "Designer"},
    {"Surname": "Melnyk", "Address": "Dnipro, Gagarina 8", "Position": "Technician"},
    {"Surname": "Kravchenko", "Address": "Zaporizhzhia, Soborna 5", "Position": "Engineer"},
    {"Surname": "Boyko", "Address": "Poltava, Shevchenka 3", "Position": "HR"},
    {"Surname": "Shapoval", "Address": "Vinnytsia, Kyivska 11", "Position": "Developer"},
    {"Surname": "Moroz", "Address": "Rivne, Voli 4", "Position": "Manager"},
    {"Surname": "Petrenko", "Address": "Cherkasy, Pidvalna 9", "Position": "Engineer"}
]

def save_employees_to_file(employees):
    with open("employees.json", "wt", encoding="utf-8") as file:
        json.dump(employees, file, indent=4)

def load_employees_from_file():
    with open("employees.json", "rt", encoding="utf-8") as file:
        return json.load(file)

# Запис початкових даних у файл
save_employees_to_file(employees)

def add_employee():
    employees = load_employees_from_file()
    surname = input("Прізвище: ")
    address = input("Адреса: ")
    position = input("Посада: ")
    employees.append({"Surname": surname, "Address": address, "Position": position})
    save_employees_to_file(employees)
    print("Працівника додано.")

def view_all():
    employees = load_employees_from_file()
    print("\nСписок працівників:")
    for emp in employees:
        print(emp)

def delete_employee():
    employees = load_employees_from_file()
    surname = input("Введіть прізвище працівника для видалення: ")
    new_list = [emp for emp in employees if emp["Surname"].lower() != surname.lower()]
    if len(new_list) != len(employees):
        save_employees_to_file(new_list)
        print("Працівника видалено.")
    else:
        print("Працівника не знайдено.")

def search_by_field():
    employees = load_employees_from_file()
    field = input("Введіть поле для пошуку (Surname, Address, Position): ").capitalize()
    value = input("Введіть значення поля: ")
    results = [emp for emp in employees if emp.get(field, "").lower() == value.lower()]
    print("\nРезультати пошуку:")
    for emp in results:
        print(emp)
    if not results:
        print("Нічого не знайдено.")

def search_by_letter():
    employees = load_employees_from_file()
    letter = input("Введіть літеру: ").lower()
    matches = [emp for emp in employees if emp["Surname"].lower().startswith(letter)]
    if matches:
        print("Працівники, прізвища яких починаються на цю літеру:")
        for emp in matches:
            print(f"{emp['Surname']}: {emp['Address']}")
    else:
        print("Нічого не знайдено.")

# Діалоговий режим
while True:
    print("\nМеню:\n1 - Додати працівника\n2 - Переглянути всіх\n3 - Видалити працівника\n4 - Пошук за полем\n5 - Пошук за літерою прізвища\n6 - Вихід")
    choice = input("Ваш вибір: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_all()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        search_by_field()
    elif choice == "5":
        search_by_letter()
    elif choice == "6":
        print("Завершення програми.")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
