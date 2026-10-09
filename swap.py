first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

print("\n--- До обмена ---")
print(f"first_room  = {first_room}")
print(f"second_room = {second_room}")

temp = first_room
first_room = second_room
second_room = temp

print("\n--- После обмена ---")
print(f"first_room  = {first_room}")
print(f"second_room = {second_room}")