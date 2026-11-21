import unittest
from formatter import print_schedule

class TestScheduleFormatter(unittest.TestCase):
    
    def test_print_schedule_with_data(self):
        """Тест: проверяем, что функция не падает с ошибкой при правильных данных."""
        # Создаем фейковые данные (как будто мы их скачали с сайта)
        fake_data = {
            '1': [{
                'dayTime': '08:00',
                'disciplName': 'Математика',
                'audNum': '101',
                'prepodName': 'Иванов И.И.'
            }]
        }
        # Если функция отработает без ошибок, тест пройдет
        try:
            print_schedule(fake_data)
        except Exception as e:
            self.fail(f"Функция print_schedule упала с ошибкой: {e}")

    def test_print_schedule_empty(self):
        """Тест: проверяем, что функция корректно обрабатывает пустые данные."""
        fake_data = {}
        try:
            print_schedule(fake_data)
        except Exception as e:
            self.fail(f"Функция print_schedule упала на пустых данных: {e}")

if __name__ == '__main__':
    unittest.main()
