import json


def load_candidates_from_json() -> list[dict]:
    """Возвращает список всех кандидатов"""
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_candidate_by_id(candidate_id) -> dict:
    """Возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json():
        if candidate["id"] == candidate_id:
            return candidate


def get_candidate_by_name(name) -> list[dict]:
    """Возвращает кандидатов по имени"""
    candidates = load_candidates_from_json()
    result = []
    for candidate in candidates:
        if name == candidate["name"]:
            result.append(candidate)
    return result


def get_candidate_by_skill(skill: str) -> list[dict]:
    """Возвращает кандидатов по навыку"""
    all_candidates = load_candidates_from_json()
    candidates = []
    for candidate in all_candidates:
        if skill.strip().lower() in candidate["skills"].strip().lower():
            candidates.append(candidate)
    return candidates
