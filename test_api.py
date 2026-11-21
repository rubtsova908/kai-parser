import requests
import json

def check_groups_api():
    url = "https://kai.ru/web/studentu/raspisanie1"
    
    # Параметры, которые обычно использует портал
    params = {
        "p_p_id": "pubStudentSchedule_WAR_publicStudentSchedule10",
        "p_p_lifecycle": "2",
        "p_p_state": "normal",
        "p_p_mode": "view",
        "p_p_resource_id": "getGroupsURL", # Пробуем этот параметр
        "p_p_cacheability": "cacheLevelPage",
        "p_p_col_id": "column-1",
        "p_p_col_count": "1",
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    print("Отправляю запрос за списком групп...")
    response = requests.post(url, params=params, headers=headers)
    
    if response.status_code == 200:
        print("УСПЕХ! Сервер ответил.")
        # Попробуем сохранить ответ в файл, чтобы посмотреть структуру
        with open("groups_test.json", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Ответ сохранен в файл groups_test.json")
        
        # Покажем первые 200 символов
        print("Начало ответа:", response.text[:200])
    else:
        print(f"ОШИБКА: Код {response.status_code}")
        print(response.text[:200])

if __name__ == "__main__":
    check_groups_api()
