import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from db import get_db

bp = Blueprint('to_dos', __name__, url_prefix='/to_dos')


@bp.route('/', methods=('GET', 'POST'))
def all_books():
    response_object = {'status': 'success'}
    db = get_db()
    if request.method == 'POST':
        description = request.form['description']
        done_at = request.form['done_at']
        error = None
        if not description:
            error = 'Description is required.'
        elif not done_at:
            error = 'Date of completion is required.'
        if error is None:
            db.execute(
                "INSERT INTO todos (description, done_at, done) VALUES (?, ?, ?)",
                (description, done_at, 0),
            )
            db.commit()
        response_object['message'] = 'Task added!'
    to_dos = db.execute(
        'SELECT description, done_at, done FROM todos'
    ).fetchall()
    response_object['to_dos'] = to_dos
    return jsonify(response_object)
