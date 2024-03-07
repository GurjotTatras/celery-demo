import celery.states as states
from flask import Flask, Response
from flask import url_for, jsonify
from worker import celery
from flask import request

dev_mode = True
app = Flask(__name__)


@app.route('/health_check')
def health_check() -> Response:
    return jsonify("OK")

@app.route('/add/<int:param1>/<int:param2>')
def add(param1: int, param2: int) -> str:
    task = celery.send_task('tasks.add', args=[param1, param2])
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response

@app.route('/multiply/<int:param1>/<int:param2>')
def multiply(param1: int, param2: int) -> str:
    task = celery.send_task('tasks.multiply', args=[param1, param2])
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response

@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)
    

@app.route('/check_prime_number/', methods=['POST'])
def prime_number():
    data = request.json
    number = data.get('number')
    task = celery.send_task('tasks.prime_number', args=[number])
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
