from rich.console import Console
from rich.table import Table

def print_schedule(data):
    """
    Принимает данные с расписанием (словарь или список) и рисует таблицу.
    """
    console = Console()
    
    if not data:
        console.print("[red]Расписание пустое или не найдено.[/red]")
        return

    table = Table(title="Расписание занятий")
    table.add_column("День / Дата", style="cyan", no_wrap=True)
    table.add_column("Время", style="magenta", no_wrap=True)
    table.add_column("Предмет", style="green")
    table.add_column("Аудитория", style="yellow")
    table.add_column("Преподаватель", style="blue")

    days_map = {
        '1': 'Понедельник', '2': 'Вторник', '3': 'Среда',
        '4': 'Четверг', '5': 'Пятница', '6': 'Суббота', '7': 'Воскресенье'
    }

    # Если данные пришли в виде СЛОВАРЯ (как для 4101)
    if isinstance(data, dict):
        sorted_days = sorted(data.items(), key=lambda x: int(x[0]))
        for day_num, lessons in sorted_days:
            day_name = days_map.get(day_num, f"День {day_num}")
            for lesson in lessons:
                table.add_row(
                    day_name,
                    lesson.get('dayTime', '').strip(),
                    lesson.get('disciplName', '').strip(),
                    lesson.get('audNum', '').strip(),
                    lesson.get('prepodName', '').strip()
                )
                
    # Если данные пришли в виде СПИСКА (как для 4123)
    elif isinstance(data, list):
        for lesson in data:
            # Пытаемся взять номер дня (если он есть)
            day_num = str(lesson.get('dayNum', ''))
            if day_num in days_map:
                day_label = days_map[day_num]
            else:
                # Если номера нет, берем первую дату из списка
                dates = lesson.get('dayDate', '').split()
                day_label = dates[0] if dates else "—"

            table.add_row(
                day_label,
                lesson.get('dayTime', '').strip(),
                lesson.get('disciplName', '').strip(),
                lesson.get('audNum', '').strip(),
                lesson.get('prepodName', '').strip()
            )
    else:
        console.print("[red]Неизвестный формат данных.[/red]")
        return

    console.print(table)
