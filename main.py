from utils import load_candidates_from_json, get_candidate_by_id, get_candidate_by_name, get_candidate_by_skill
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    """Главная страничка со всеми кандидатами"""
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:idx>')
def candidate_page(idx):
    """Страница кандидата"""
    candidate: dict = get_candidate_by_id(idx)
    if candidate:
        return render_template('card.html', candidate=candidate)
    else:
        return "Кандидат не найден"


@app.route('/search/<candidate_name>')
def search_by_name_page(candidate_name):
    """Поиск по имени"""
    candidates = get_candidate_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route('/skill/<skill_name>')
def search_by_skill_name(skill_name):
    """Поиск по навыку"""
    candidates = get_candidate_by_skill(skill_name)
    return render_template('skill.html', skill=skill_name, candidates=candidates)


app.run()
