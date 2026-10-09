def main():
    while True:
        try:
            age = int(input("Введите возраст (от 1 до 120): "))
            if 1 <= age <= 120:
                break
            else:
                print("Ошибка: возраст должен быть от 1 до 120.")
        except ValueError:
            print("Ошибка: введите целое число.")

    while True:
        try:
            hours = float(input("Введите количество часов подготовки на неделе: "))
            if hours >= 0:
                break
            else:
                print("Ошибка: часы не могут быть отрицательными.")
        except ValueError:
            print("Ошибка: введите число.")

    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    group = input("Введите группу: ")
    city = input("Введите город: ")
    subject = input("Введите любимый предмет: ")

    age_in_4_years = age + 4
    
    total_hours_4_weeks = hours * 4
    
    avg_daily_hours = hours / 7

    print("\n" + "="*30)
    print("       КАРТОЧКА ПРОФИЛЯ")
    print("="*30)
    
    print(f"Студент:       {name} {surname}")
    print(f"Группа:        {group}")
    print(f"Город:         {city}")
    print(f"Любимый предмет: {subject}")
    print("-" * 30)
    
    print(f"Возраст через 4 года: {age_in_4_years}")
    
    print(f"Подготовка за 4 недели: {total_hours_4_weeks:.2f} ч.")
    
    print(f"Среднее в день:         {avg_daily_hours:.2f} ч.")
    print("="*30)

if __name__ == "__main__":
    main()