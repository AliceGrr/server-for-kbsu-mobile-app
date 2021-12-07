from flask import request, abort

from . import app
from .models import Students, Schedules


@app.route('/kbsu_app', methods=['POST'])
def login():
    """Вход пользователя."""
    user = Students.get_by_id(request.form['id'])
    if user is None:
        abort(404)
    elif user.last_name == request.form['last_name']:
        schedule = Schedules.get_for_all_week(user.group_code)
        return schedule
    else:
        abort(404)





