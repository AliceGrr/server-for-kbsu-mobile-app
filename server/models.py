from . import db

lectures_times = {
    1: {'startTime': '9:00', 'endTime': '10:35'},
    2: {'startTime': '10:45', 'endTime': '12:20'},
    3: {'startTime': '13:00', 'endTime': '14:35'},
    4: {'startTime': '14:45', 'endTime': '16:20'},
}


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    patronymic = db.Column(db.String(50))
    group_code = db.Column(db.Integer, db.ForeignKey('groups.id'))

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'

    @staticmethod
    def get_by_id(user_id):
        return Students.query.get(user_id)


class Schedules(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    weekday_id = db.Column(db.Integer, db.ForeignKey('weekdays.id'))
    class_number = db.Column(db.Integer)
    auditorium_number_id = db.Column(db.Integer, db.ForeignKey('auditoriums.id'))
    disciple_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

    @staticmethod
    def get_by_weekday(weekday_id, group_id):
        query = Schedules.query \
            .filter(Schedules.weekday_id == weekday_id) \
            .filter(Schedules.group_id == group_id) \
            .order_by(Schedules.class_number.desc())
        schedule = {
            'dayName': weekday_id,
            'lectures':
                [
                    {
                        'lectureName': str(day.disciple),
                        'teacher': str(day.teacher),
                        'startTime': day.start_time,
                        'endTime': day.end_time,
                        'classroom': day.auditorium_number_id,
                        'instituteId': day.auditorium.institute,
                    }
                    for day in query
                ]
        }
        return schedule

    @staticmethod
    def get_for_all_week(group_id):
        all_schedule = [Schedules.get_by_weekday(i, group_id) for i in range(1, 6)]
        schedule = {
            group_id: all_schedule
        }
        return schedule

    @property
    def start_time(self):
        return lectures_times.get(self.class_number).get('startTime')

    @property
    def end_time(self):
        return lectures_times.get(self.class_number).get('endTime')

    def __repr__(self):
        return f'{self.weekday} {self.class_number} пара ' \
               f'{self.group} {self.auditorium} кабинет {self.auditorium.institutes} корпус ' \
               f'{self.disciple} {self.teacher}'


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    specialization = db.Column(db.String(50))
    schedule = db.relationship('Schedules', backref='group')
    students = db.relationship('Students', backref='group')

    def __repr__(self):
        return f'{self.id} {self.specialization}'

    @staticmethod
    def get_by_id(id):
        return Groups.query.get(id)


class Institutes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    auditoriums = db.relationship('Auditoriums', backref='institutes')

    def __repr__(self):
        return f'{self.id}'


class Auditoriums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schedule = db.relationship('Schedules', backref='auditorium')
    institute = db.Column(db.Integer, db.ForeignKey('institutes.id'))

    def __repr__(self):
        return f'{self.id}'


class Disciplines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    schedule = db.relationship('Schedules', backref='disciple')

    def __repr__(self):
        return f'{self.name}'

    @staticmethod
    def get_by_id(id):
        return Disciplines.query.get(id)


class Weekdays(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    schedule = db.relationship('Schedules', backref='weekday')

    def __repr__(self):
        return f'{self.name}'

    @staticmethod
    def get_by_id(id):
        return Weekdays.query.get(id)


class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    patronymic = db.Column(db.String(50))
    schedule = db.relationship('Schedules', backref='teacher')

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'

    @staticmethod
    def get_by_id(id):
        return Teachers.query.get(id)
