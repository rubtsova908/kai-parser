from parser import get_schedule
from formatter import print_schedule

def main():
    print("=== Парсер расписания КАИ ===")
    group = input("Введите номер группы (например, 4101): ").strip()
    
    if not group:
        print("Вы не ввели группу.")
        return

    print(f"Загружаю расписание для группы {group}...")
    data = get_schedule(group)
    
    if data:
        print_schedule(data)
        

if __name__ == "__main__":
    main()
