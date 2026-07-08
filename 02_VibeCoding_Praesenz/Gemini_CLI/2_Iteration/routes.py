from flask import Blueprint, render_template, jsonify, request
from config import config
from search_loop import search_loop
from word_selector import word_selector

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/status')
def status():
    loop_status = search_loop.get_status()
    cfg = config.get_config()
    return jsonify(
        status="Running" if loop_status["is_running"] else "Stopped",
        count=loop_status["search_count"],
        last_word=loop_status["last_word"],
        current_search_engine=loop_status["current_search_engine"],
        time_remaining=loop_status["time_remaining"],
        words_count=word_selector.get_words_count(),
        config=cfg
    )

@main_bp.route('/toggle', methods=['POST'])
def toggle():
    loop_status = search_loop.get_status()
    if loop_status["is_running"]:
        search_loop.stop()
    else:
        search_loop.start()
    
    updated_status = search_loop.get_status()
    return jsonify(
        status="Running" if updated_status["is_running"] else "Stopped",
        count=updated_status["search_count"]
    )

@main_bp.route('/config', methods=['POST'])
def update_config():
    data = request.get_json() or {}
    try:
        updated = config.update_config(data)
        return jsonify(status="success", config=updated)
    except Exception as e:
        return jsonify(status="error", message=str(e)), 400

@main_bp.route('/dictionary/words', methods=['GET', 'POST', 'DELETE'])
def dictionary_words():
    if request.method == 'GET':
        return jsonify(words=word_selector.get_all_words())
        
    elif request.method == 'POST':
        data = request.get_json() or {}
        word = data.get('word', '').strip()
        if not word:
            return jsonify(status="error", message="Word cannot be empty"), 400
        if word_selector.add_word(word):
            return jsonify(status="success", word=word)
        return jsonify(status="error", message="Could not add word"), 500
        
    elif request.method == 'DELETE':
        data = request.get_json() or {}
        word = data.get('word', '').strip()
        if not word:
            return jsonify(status="error", message="Word cannot be empty"), 400
        if word_selector.remove_word(word):
            return jsonify(status="success", word=word)
        return jsonify(status="error", message="Could not remove word or word not found"), 400
