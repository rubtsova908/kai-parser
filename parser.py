import requests

def get_schedule(group_number: str):
    """
    Запрашивает расписание с сайта КАИ.
    """
    url = "https://kai.ru/web/studentu/raspisanie1"
    
    # Параметры из адресной строки (из вашей ссылки)
    params = {
        "p_p_id": "pubStudentSchedule_WAR_publicStudentSchedule10",
        "p_p_lifecycle": "2",
        "p_p_state": "normal",
        "p_p_mode": "view",
        "p_p_resource_id": "schedule",
        "p_p_cacheability": "cacheLevelPage",
        "p_p_col_id": "column-1",
        "p_p_col_count": "1",
    }
    
    # Данные, которые передаются в Payload (Form data)
    # Пока используем ID для группы 4101. 
    # Если захотите проверить другую группу, ID придется поменять.
    data = {
        "groupId": "28536",      # ID группы 4101
        "programForm": "4toto"   # Форма обучения
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "X-Requested-With": "XMLHttpRequest" # Говорим серверу, что мы ждем JSON
    }
    
    response = requests.post(url, params=params, data=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка: не удалось получить данные (Код {response.status_code})")
        print(response.text)
        return None
