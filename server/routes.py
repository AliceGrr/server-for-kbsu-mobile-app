import json

from flask import request

from . import app
from .models import Students, Schedules


class Answer:
    def __init__(self, err_message='', **kwargs):
        self.err_message = err_message
        self.__dict__.update(kwargs)

    def to_json(self):
        return json.dumps(self.__dict__)


@app.route('/kbsu_app', methods=['POST'])
def login():
    """Вход пользователя."""
    user = Students.get_by_id(request.form['id'])

    if user and user.last_name == request.form['last_name']:
        answer = Answer()
        return answer.to_json()
    else:
        answer = Answer('No such student')
        return answer.to_json()


@app.route('/kbsu_app/schedule', methods=['POST'])
def get_schedule():
    """Получение расписания"""
    user = Students.get_by_id(request.form['id'])
    if user and user.last_name == request.form['last_name']:
        schedule = Schedules.get_for_all_week(user.group_code)
        answer = Answer(schedule=schedule)
        return answer.to_json()
    else:
        answer = Answer("Can't find schedule for student")
        return answer.to_json()


@app.route('/kbsu_app/marks', methods=['POST'])
def get_marks():
    pass


@app.route('/kbsu_app/university_resources', methods=['POST'])
def get_university_resources():
    pass


@app.route('/kbsu_app/university_info', methods=['POST'])
def get_university_info():
    pass






