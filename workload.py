def get_non_negative_int(prompt):
    """Запрашивает целое неотрицательное число."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Ошибка: число должно быть неотрицательным.")
        except ValueError:
            print("Ошибка: введите целое число.")

def get_positive_int(prompt):
    """Запрашивает положительное целое число."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Ошибка: число должно быть положительным.")
        except ValueError:
            print("Ошибка: введите целое число.")

def get_positive_float(prompt):
    """Запрашивает положительное дробное число."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Ошибка: число должно быть положительным.")
        except ValueError:
            print("Ошибка: введите число.")

def main():
    print("=== ВВОД ДАННЫХ О НАГРУЗКЕ ===\n")

    subject1 = input("Введите название первого предмета: ")
    count1 = get_non_negative_int(f"Количество занятий по предмету '{subject1}' за неделю: ")
    duration1 = get_positive_int(f"Продолжительность одного занятия по '{subject1}' (в минутах): ")

    subject2 = input("\nВведите название второго предмета: ")
    count2 = get_non_negative_int(f"Количество занятий по предмету '{subject2}' за неделю: ")
    duration2 = get_positive_int(f"Продолжительность одного занятия по '{subject2}' (в минутах): ")

    available_hours = get_positive_float(
        "\nВведите доступное время на неделю (в часах): "
    )

    load1_minutes = count1 * duration1
    load2_minutes = count2 * duration2

    total_minutes = load1_minutes + load2_minutes
    total_hours = total_minutes / 60

    available_minutes = available_hours * 60

    free_minutes = available_minutes - total_minutes
    free_hours = free_minutes / 60

    total_hours_4_weeks = total_hours * 4

    print("\n" + "=" * 45)
    print("           КАРТОЧКА НАГРУЗКИ")
    print("=" * 45)
    print(f"{'Предмет':<20} {'Занятий':<10} {'Мин/зан':<10} {'Часов/нед':<10}")
    print("-" * 45)
    print(f"{subject1:<20} {count1:<10} {duration1:<10} {load1_minutes / 60:<10.2f}")
    print(f"{subject2:<20} {count2:<10} {duration2:<10} {load2_minutes / 60:<10.2f}")
    print("-" * 45)
    print(f"Общая нагрузка за неделю:      {total_hours:.2f} ч.")
    print(f"Доступное время:               {available_hours:.2f} ч.")
    print(f"Оставшееся свободное время:    {free_hours:.2f} ч.")
    print("-" * 45)
    print(f"Нагрузка за 4 недели:          {total_hours_4_weeks:.2f} ч.")
    print("=" * 45)

if __name__ == "__main__":
    main()