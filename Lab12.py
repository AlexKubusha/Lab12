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

# Запис у файл
with open("employees.json", "wt", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

# Діалоговий режим
while True:
    print("\nМеню:\n1 - Додати працівника\n2 - Переглянути всіх\n3 - Видалити працівника\n4 - Пошук за полем\n5 - Пошук за літерою прізвища\n6 - Вихід")
    choice = input("Ваш вибір: ")

    if choice == "1":
        with open("employees.json", "rt", encoding="utf-8") as file:
            employees = json.load(file)

        surname = input("Прізвище: ")
        address = input("Адреса: ")
        position = input("Посада: ")
        employees.append({"Surname": surname, "Address": address, "Position": position})

        with open("employees.json", "wt", encoding="utf-8") as file:
            json.dump(employees, file, indent=4)
        print("Працівника додано.")

    elif choice == "2":
        with open("employees.json", "rt", encoding="utf-8") as file:
            employees = json.load(file)
        print("\nСписок працівників:")
        for emp in employees:
            print(emp)

    elif choice == "3":
        with open("employees.json", "rt", encoding="utf-8") as file:
            employees = json.load(file)

        surname = input("Введіть прізвище працівника для видалення: ")
        new_list = [emp for emp in employees if emp["Surname"].lower() != surname.lower()]
        if len(new_list) != len(employees):
            with open("employees.json", "wt", encoding="utf-8") as file:
                json.dump(new_list, file, indent=4)
            print("Працівника видалено.")
        else:
            print("Працівника не знайдено.")

    elif choice == "4":
        with open("employees.json", "rt", encoding="utf-8") as file:
            employees = json.load(file)

        field = input("Введіть поле для пошуку (Surname, Address, Position): ").capitalize()
        value = input("Введіть значення поля: ")
        results = [emp for emp in employees if emp.get(field, "").lower() == value.lower()]
        print("\nРезультати пошуку:")
        for emp in results:
            print(emp)
        if not results:
            print("Нічого не знайдено.")

    elif choice == "5":
        with open("employees.json", "rt", encoding="utf-8") as file:
            employees = json.load(file)

        letter = input("Введіть літеру: ").lower()
        matches = [emp for emp in employees if emp["Surname"].lower().startswith(letter)]
        if matches:
            print("Працівники, прізвища яких починаються на цю літеру:")
            for emp in matches:
                print(f"{emp['Surname']}: {emp['Address']}")
        else:
            print("Нічого не знайдено.")

    elif choice == "6":
        print("Завершення програми.")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")