from rich.console import Console
from rich.table import Table

def print_schedule(data):
    """
    Принимает JSON с расписанием и рисует красивую таблицу.
    """
    console = Console()
    
    if not data:
        console.print("[red]Расписание пустое или не найдено.[/red]")
        return

    table = Table(title="Расписание занятий")
    
    table.add_column("День", style="cyan", no_wrap=True)
    table.add_column("Время", style="magenta", no_wrap=True)
    table.add_column("Предмет", style="green")
    table.add_column("Аудитория", style="yellow")
    table.add_column("Преподаватель", style="blue")

    # Словарь для перевода номеров дней в названия
    days_map = {
        '1': 'Понедельник',
        '2': 'Вторник',
        '3': 'Среда',
        '4': 'Четверг',
        '5': 'Пятница',
        '6': 'Суббота',
        '7': 'Воскресенье'
    }

    # Сортируем дни по порядку (1, 2, 3...), чтобы они не шли вразнобой
    sorted_days = sorted(data.items(), key=lambda x: int(x[0]))
    
    for day_num, lessons in sorted_days:
        # Вот та самая строчка, которую потерял Python:
        day_name = days_map.get(day_num, f"День {day_num}")
        
        # Проходимся по всем парам в этом дне
        for lesson in lessons:
            time = lesson.get('dayTime', '').strip()
            subject = lesson.get('disciplName', '').strip()
            room = lesson.get('audNum', '').strip()
            teacher = lesson.get('prepodName', '').strip()
            
            # Добавляем строку в таблицу
            table.add_row(day_name, time, subject, room, teacher)

    console.print(table)
