import json

from flask import request
from werkzeug.exceptions import abort

from . import app
from .models import Students, Schedules, Marks, Universities, UniversityResources


class Answer:
    def __init__(self, err_message='', **kwargs):
        self.err_message = err_message
        self.__dict__.update(kwargs)

    def to_json(self):
        return json.dumps(self.__dict__)


@app.route('/kbsu_app', methods=['POST'])
def login():
    """Вход пользователя."""
    student = Students.get_by_id(request.form['id'])

    if student and student.last_name == request.form['last_name']:
        student_info = Students.get_student_info(student.id)
        return student_info
    else:
        abort(404)


@app.route('/kbsu_app/schedule', methods=['POST'])
def get_schedule():
    """Получение расписания"""
    student = Students.get_by_id(request.form['id'])
    if student and student.last_name == request.form['last_name']:
        schedule = Schedules.get_for_all_week(student.group_code)
        return schedule
    else:
        abort(404)


@app.route('/kbsu_app/marks', methods=['POST'])
def get_marks():
    """Получение оценок"""
    student = Students.get_by_id(request.form['id'])
    if student and student.last_name == request.form['last_name']:
        marks = Marks.get_for_all_periods(student.id)
        return marks
    else:
        abort(404)


@app.route('/kbsu_app/university_resources', methods=['POST'])
def get_university_resources():
    """Получение ресурсов университета"""
    student = Students.get_by_id(request.form['id'])
    if student and student.last_name == request.form['last_name']:
        university_resources = UniversityResources.get_university_resources(student.id)
        return university_resources
    else:
        abort(404)


@app.route('/kbsu_app/university_info', methods=['POST'])
def get_university_info():
    """Получение информации об университете"""
    student = Students.get_by_id(request.form['id'])
    if student and student.last_name == request.form['last_name']:
        university_info = Universities.get_university_info(student.id)
        return university_info
    else:
        abort(404)






