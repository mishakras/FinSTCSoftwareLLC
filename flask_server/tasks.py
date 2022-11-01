

from flask import (
    Blueprint, request, jsonify
)

from db import get_db

bp = Blueprint('to_dos', __name__, url_prefix='/to_dos')


@bp.route('/', methods=('GET', 'POST', 'PUT', 'DELETE'))
def all_books():
    response_object = {'status': 'success'}
    db = get_db()
    if request.method == 'POST':
        post_data = request.get_json()
        description = post_data.get('description')
        date_completed = post_data.get('date_completed')
        error = None
        if not description:
            error = 'Description is required.'
            response_object['message'] = 'Description is required.'
        elif not date_completed:
            error = 'Date of completion is required.'
            response_object['message'] = 'Date of completion is required.'
        if error is None:
            try:
                db.execute(
                    "INSERT INTO tasks (description, done_at, done) VALUES (?, ?, ?)",
                    (description, date_completed, 0),
                )
                db.commit()
                response_object['message'] = 'Task added!'
            except db.IntegrityError:
                response_object['message'] = 'Task with this description already exists!'
    elif request.method == 'PUT':
        put_data = request.get_json()
        description = put_data.get('description')
        completed = put_data.get('completed')
        error = None
        if not description:
            error = 'Description is required.'
            response_object['message'] = 'Description is required.'
        if error is None:
            try:
                db.execute(
                    "UPDATE tasks SET done = ? WHERE description = ?",
                    (completed, description),
                )
                db.commit()
                if completed:
                    response_object['message'] = 'Task done!'
                else:
                    response_object['message'] = 'Task undone!'
            except db.IntegrityError:
                response_object['message'] = 'Task with this description already exists!'
    elif request.method == 'DELETE':
        delete_data = request.get_json()
        print(delete_data)
        description = delete_data.get('description')
        print(type(description))
        try:
            db.execute(
                "DELETE FROM tasks WHERE description = ?",
                (description,),
            )
            db.commit()
            response_object['message'] = 'Task deleted!'
        except db.IntegrityError:
            response_object['message'] = 'Task with this description does not exist!'
    else:
        tasks = db.execute(
            'SELECT description, done_at, done FROM tasks'
        ).fetchall()
        response_object['Tasks'] = tasks
    return jsonify(response_object)
