import json


def load_candidates():
    with open('candidates.json', encoding='utf-8') as file_read:
        data = json.load(file_read)
    return data

def get_all():
    candidates = load_candidates()
    return candidates

def get_by_pk(pk):
    candidates = load_candidates()
    for canditate in candidates:
        if canditate['pk'] == pk:
            return canditate

def get_by_skill(skill_name):
    candidates = load_candidates()
    skill_candidate = []
    for canditate in candidates:
        if skill_name.lower() in canditate['skills'].lower():
            skill_candidate.append(canditate)
    return skill_candidate
