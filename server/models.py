import datetime

from sqlalchemy import desc

from . import db


class Schedules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    weekday_id = db.Column(db.Integer, db.ForeignKey('weekdays.id'), nullable=False)
    auditorium_number_id = db.Column(db.Integer, db.ForeignKey('auditoriums.id'), nullable=False)
    disciple_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
    lecture_number_id = db.Column(db.Integer, db.ForeignKey('lecture_numbers.id'), nullable=False)

    def __init__(self, group_id, weekday_id, auditorium_number_id, disciple_id, teacher_id, lecture_number_id):
        self.group_id = group_id
        self.weekday_id = weekday_id
        self.auditorium_number_id = auditorium_number_id
        self.disciple_id = disciple_id
        self.teacher_id = teacher_id
        self.lecture_number_id = lecture_number_id

    @staticmethod
    def get_by_weekday(weekday_id, group_id):
        query = Schedules.query \
            .filter(Schedules.weekday_id == weekday_id) \
            .filter(Schedules.group_id == group_id) \
            .order_by(desc(Schedules.lecture_number_id))
        schedule = {
            'day_name': {
                'ru': Weekdays.get_by_id(weekday_id).name_ru,
                'eng': Weekdays.get_by_id(weekday_id).name_eng,
            },
            'lectures':
            [
                {
                    'lecture_number': day.lecture_number_id,
                    'disciple': {
                            'ru': day.disciple.name_ru,
                            'eng': day.disciple.name_eng,
                    },
                    'teacher': {
                        'ru': {
                            'first_name': day.teacher.first_name_ru,
                            'last_name': day.teacher.last_name_ru,
                            'patronymic': day.teacher.patronymic_ru,

                        },
                        'eng': {
                            'first_name': day.teacher.first_name_eng,
                            'last_name': day.teacher.last_name_eng,
                            'patronymic': day.teacher.patronymic_eng,
                        }
                    },
                    'startTime': day.lecture_number.start_time,
                    'endTime': day.lecture_number.end_time,
                    'classroom': day.auditorium_number_id,
                    'institute': {
                        'ru': day.auditorium.institute.name_ru,
                        'eng': day.auditorium.institute.name_eng,
                        'address': day.auditorium.institute.address,
                        'longitude': day.auditorium.institute.longitude,
                        'latitude': day.auditorium.institute.latitude,
                    }
                }
                for day in query
            ]
        }
        return schedule

    @staticmethod
    def get_for_all_week(group_id):
        all_schedule = [Schedules.get_by_weekday(i, group_id) for i in range(1, 6)]
        return {'schedule': all_schedule}

    def __repr__(self):
        return f'{self.weekday} {self.class_number} пара ' \
               f'{self.group} {self.auditorium} кабинет {self.auditorium.institutes} корпус ' \
               f'{self.disciple} {self.teacher}'


class Marks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    disciple_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'), nullable=False)
    mark_id = db.Column(db.Integer, db.ForeignKey('mark_types.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
    first_study_point_score = db.Column(db.Integer, nullable=True)
    second_study_point_score = db.Column(db.Integer, nullable=True)
    third_study_point_score = db.Column(db.Integer, nullable=True)
    study_period = db.Column(db.Integer, nullable=False)

    def __init__(self, student_id, group_id, mark_id, first_study_point_score,
                 second_study_point_score, third_study_point_score, disciple_id, teacher_id, study_period):
        self.student_id = student_id
        self.group_id = group_id
        self.mark_id = mark_id
        self.first_study_point_score = first_study_point_score
        self.second_study_point_score = second_study_point_score
        self.third_study_point_score = third_study_point_score
        self.disciple_id = disciple_id
        self.teacher_id = teacher_id
        self.study_period = study_period

    @staticmethod
    def get_by_periods(study_period_id, student_id):
        query = Marks.query \
            .filter(Marks.study_period == study_period_id) \
            .filter(Marks.student_id == student_id)
        schedule = {
            'study_period': study_period_id,
            'marks':
            [
                {
                    'first_study_point_score': disciple.first_study_point_score,
                    'second_study_point_score': disciple.second_study_point_score,
                    'third_study_point_score': disciple.third_study_point_score,
                    'mark': {
                        'ru': MarkTypes.get_by_id(disciple.mark_id).type_ru,
                        'eng': MarkTypes.get_by_id(disciple.mark_id).type_eng,
                    },
                    'disciple': {
                            'ru': Disciplines.get_by_id(disciple.disciple_id).name_ru,
                            'eng': Disciplines.get_by_id(disciple.disciple_id).name_eng,
                    },
                    'teacher': {
                        'ru': {
                            'first_name': Teachers.get_by_id(disciple.teacher_id).first_name_ru,
                            'last_name': Teachers.get_by_id(disciple.teacher_id).last_name_ru,
                            'patronymic': Teachers.get_by_id(disciple.teacher_id).patronymic_ru,

                        },
                        'eng': {
                            'first_name': Teachers.get_by_id(disciple.teacher_id).first_name_eng,
                            'last_name': Teachers.get_by_id(disciple.teacher_id).last_name_eng,
                            'patronymic': Teachers.get_by_id(disciple.teacher_id).patronymic_eng,
                        }
                    },
                }
                for disciple in query
            ]
        }
        return schedule

    @staticmethod
    def get_for_all_periods(student_id):
        student = Students.get_by_id(student_id)
        all_schedule = [Marks.get_by_periods(i, student_id) for i in range(1, student.group.current_study_period)]
        return {'marks': all_schedule}


class Weekdays(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_ru = db.Column(db.String(15), nullable=False, unique=True)
    name_eng = db.Column(db.String(15), nullable=False, unique=True)
    schedule = db.relationship('Schedules', backref='weekday', cascade='all, delete, delete-orphan')

    def __init__(self, name_ru, name_eng):
        self.name_ru = name_ru
        self.name_eng = name_eng

    def __repr__(self):
        return f'{self.name}'

    @staticmethod
    def get_by_id(id):
        return Weekdays.query.get(id)


class LectureNumbers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.String(50), nullable=False)
    end_time = db.Column(db.String(50), nullable=False)
    schedule = db.relationship('Schedules', backref='lecture_number', cascade='all, delete, delete-orphan')

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


class MarkTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_ru = db.Column(db.String(50), nullable=False, unique=True)
    type_eng = db.Column(db.String(50), nullable=False)

    def __init__(self, type_ru, type_eng):
        self.type_ru = type_ru
        self.type_eng = type_eng

    @staticmethod
    def get_by_id(id):
        return MarkTypes.query.get(id)


class DiscipleTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_ru = db.Column(db.String(50), nullable=False, unique=True)
    type_eng = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, type_ru, type_eng):
        self.type_ru = type_ru
        self.type_eng = type_eng


class UniversityResources(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False, unique=True)
    url = db.Column(db.String(50), nullable=False, unique=True)
    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'))

    def __init__(self, type, url, university_id):
        self.type = type
        self.url = url
        self.university_id = university_id


class Universities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(50), nullable=False)
    longitude = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.String(50), nullable=False)
    addictive_info = db.Column(db.String(300), nullable=True)
    resources = db.relationship('UniversityResources', backref='university', cascade='all, delete, delete-orphan')
    institutes = db.relationship('Institutes', backref='university', cascade='all, delete, delete-orphan')

    def __init__(self, name, address, longitude, latitude, addictive_info):
        self.name = name
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.addictive_info = addictive_info


class Institutes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_ru = db.Column(db.String(50), nullable=False, unique=True)
    name_eng = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(50), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)
    latitude = db.Column(db.Float(), nullable=False)
    auditoriums = db.relationship('Auditoriums', backref='institute', cascade='all, delete, delete-orphan')
    faculties = db.relationship('Faculties', backref='institute', cascade='all, delete, delete-orphan')
    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'), nullable=False)

    def __init__(self, name_ru, name_eng, address, longitude, latitude, university_id):
        self.name_ru = name_ru
        self.name_eng = name_eng
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.university_id = university_id

    def __repr__(self):
        return f'{self.id}'


class Faculties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_ru = db.Column(db.String(50), nullable=False, unique=True)
    name_eng = db.Column(db.String(50), nullable=False, unique=True)
    specializations = db.relationship('Specializations', backref='faculty', cascade='all, delete, delete-orphan')
    institute_id = db.Column(db.Integer, db.ForeignKey('institutes.id'), nullable=False)

    def __init__(self, name_ru, name_eng, institute_id):
        self.name_ru = name_ru
        self.name_eng = name_eng
        self.institute_id = institute_id


class Specializations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_ru = db.Column(db.String(50), nullable=False, unique=True)
    name_eng = db.Column(db.String(50), nullable=False, unique=True)
    groups = db.relationship('Groups', backref='specialization', cascade='all, delete, delete-orphan')
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'), nullable=False)

    def __init__(self, name_ru, name_eng, faculty_id):
        self.name_ru = name_ru
        self.name_eng = name_eng
        self.faculty_id = faculty_id


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    specialization_id = db.Column(db.Integer, db.ForeignKey('specializations.id'), nullable=False)
    enter_year = db.Column(db.Integer)
    schedule = db.relationship('Schedules', backref='group', cascade='all, delete, delete-orphan')
    students = db.relationship('Students', backref='group', cascade='all, delete, delete-orphan')

    def __init__(self, specialization_id, enter_year):
        self.specialization_id = specialization_id
        self.enter_year = enter_year

    def __repr__(self):
        return f'{self.id} {self.specialization}'

    @staticmethod
    def get_by_id(id):
        return Groups.query.get(id)

    @property
    def current_study_period(self):
        current_year = datetime.datetime.now().year
        return current_year - self.enter_year


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    patronymic = db.Column(db.String(50), nullable=False)
    group_code = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)

    def __init__(self, first_name, last_name, patronymic, group_code):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.group_code = group_code

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'

    @staticmethod
    def get_by_id(user_id):
        return Students.query.get(user_id)


class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    first_name_ru = db.Column(db.String(50), nullable=False)
    last_name_ru = db.Column(db.String(50), nullable=False)
    patronymic_ru = db.Column(db.String(50), nullable=False)

    first_name_eng = db.Column(db.String(50), nullable=False)
    last_name_eng = db.Column(db.String(50), nullable=False)
    patronymic_eng = db.Column(db.String(50), nullable=False)

    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'), nullable=False)
    schedule = db.relationship('Schedules', backref='teacher', cascade='all, delete, delete-orphan')

    def __init__(self, first_name_ru, last_name_ru, patronymic_ru, first_name_eng, last_name_eng, patronymic_eng, faculty_id):
        self.first_name_ru = first_name_ru
        self.last_name_ru = last_name_ru
        self.patronymic_ru = patronymic_ru

        self.first_name_eng = first_name_eng
        self.last_name_eng = last_name_eng
        self.patronymic_eng = patronymic_eng

        self.faculty_id = faculty_id

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'

    @staticmethod
    def get_by_id(id):
        return Teachers.query.get(id)


class Auditoriums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(5), unique=True, nullable=False)
    schedule = db.relationship('Schedules', backref='auditorium', cascade='all, delete, delete-orphan')
    institute_id = db.Column(db.Integer, db.ForeignKey('institutes.id'), nullable=False)

    def __init__(self, institute_id, number):
        self.institute_id = institute_id
        self.number = number

    @property
    def floor(self):
        return self.number[0]

    def __repr__(self):
        return f'{self.id}'


class Disciplines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_ru = db.Column(db.String(50), nullable=False)
    name_eng = db.Column(db.String(50), nullable=False)
    schedule = db.relationship('Schedules', backref='disciple', cascade='all, delete, delete-orphan')
    disciple_type_id = db.Column(db.Integer, db.ForeignKey('disciple_types.id'), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'), nullable=False)

    def __init__(self, name_ru, name_eng, disciple_type_id, faculty_id):
        self.name_ru = name_ru
        self.name_eng = name_eng
        self.disciple_type_id = disciple_type_id
        self.faculty_id = faculty_id

    def __repr__(self):
        return f'{self.name}'

    @staticmethod
    def get_by_id(id):
        return Disciplines.query.get(id)