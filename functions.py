import json


def load_candidates():
    """Получение данных из файла"""
    with open('candidates.json', encoding='utf-8') as file_read:
        data = json.load(file_read)
    return data

def get_all():
    """Функция возвращает все данные по кандидатам"""
    candidates = load_candidates()
    return candidates

def get_by_pk(pk):
    """Функция возвращает кандидата по его pk"""
    candidates = load_candidates()
    for canditate in candidates:
        if canditate['pk'] == pk:
            return canditate

def get_by_skill(skill_name):
    """Функция возвращает список кандидатов по скиллу"""
    candidates = load_candidates()
    skill_candidate = []
    for canditate in candidates:
        if skill_name.lower() in canditate['skills'].lower():
            skill_candidate.append(canditate)
    return skill_candidate
