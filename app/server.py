from flask import Flask, jsonify

app = Flask(__name__)

# Фиктивные данные задач
tasks = [
    {"theme": "Python Programming", "task": "Write a function that reverses a string"},
    {"theme": "Web Development", "task": "Create a simple HTML page with a styled header"},
    {"theme": "Machine Learning", "task": "Train a model on the Iris dataset"}
]

# Получить задачу по конкретной теме
@app.route('/tasks/<theme>', methods=['GET'])
def get_task_by_theme(theme):
    # Ищем задачи, соответствующие указанной теме
    filtered_tasks = [task for task in tasks if task["theme"].lower() == theme.lower()]
    if filtered_tasks:
        return jsonify(filtered_tasks)
    return jsonify({"error": "Theme not found"}), 404

if __name__ == '__main__':
    app.run(port=8080)
