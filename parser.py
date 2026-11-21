import requests

def get_group_info(group_number: str):
    """
    Скачивает список всех групп и находит ID нужной группы.
    """
    url = "https://kai.ru/web/studentu/raspisanie1"
    
    params = {
        "p_p_id": "pubStudentSchedule_WAR_publicStudentSchedule10",
        "p_p_lifecycle": "2",
        "p_p_state": "normal",
        "p_p_mode": "view",
        "p_p_resource_id": "getGroupsURL", # Запрос за списком групп
        "p_p_cacheability": "cacheLevelPage",
        "p_p_col_id": "column-1",
        "p_p_col_count": "1",
    }
    
    headers = {"User-Agent": "Mozilla/5.0", "X-Requested-With": "XMLHttpRequest"}
    
    response = requests.post(url, params=params, headers=headers)
    
    if response.status_code != 200:
        return None, None

    groups_list = response.json()
    
    # Ищем нашу группу в списке
    for group in groups_list:
        if group.get("group") == group_number:
            return group.get("id"), group.get("forma") # Возвращаем ID и форму
            
    return None, None # Если группа не найдена

def get_schedule(group_number: str):
    """
    Запрашивает расписание с сайта КАИ по номеру группы.
    """
    # 1. Сначала узнаем ID группы
    group_id, group_form = get_group_info(group_number)
    
    if not group_id:
        print(f"[red]Группа {group_number} не найдена на сайте.[/red]")
        return None

    # 2. Теперь запрашиваем расписание по ID
    url = "https://kai.ru/web/studentu/raspisanie1"
    
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
    
    data = {
        "groupId": group_id,       # Подставляем найденный ID
        "programForm": group_form  # Подставляем форму обучения
    }
    
    headers = {"User-Agent": "Mozilla/5.0", "X-Requested-With": "XMLHttpRequest"}
    
    response = requests.post(url, params=params, data=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка при получении расписания (Код {response.status_code})")
        return None
