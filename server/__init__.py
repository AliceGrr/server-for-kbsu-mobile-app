from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

create_db = True
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from server import models
from server import routes


if create_db:
    db.drop_all()
    db.create_all()

    from server.models import Weekdays, LectureNumbers, DiscipleTypes, MarkTypes, Universities, UniversityResources, \
    Teachers, Students, Specializations, Faculties, Groups, Institutes, Disciplines, Auditoriums, Schedules, Marks

    db.session.add_all([
        Universities('КБГУ', 'Нальчик, ул. Чернышевского', 12.23423, 12.235252, ''),
    ])
    db.session.commit()

    db.session.add_all([
        Institutes('ИИиЦТ', 'IIiCT', 'Нальчик, ул. Чернышевского 1213', 10.456, 17.1456, 1),
        Institutes('ХимБио', 'HimBio', 'Нальчик, ул. Чернышевского 100', 8.456, 78.1456, 1),
        Institutes('СоцГум', 'SocGum', 'Нальчик, ул. Чернышевского 0', 5.456, 17.1456, 1),
    ])
    db.session.commit()

    db.session.add_all([
        Faculties('ИИКТ', 'IICT', 1),
        Faculties('ИБ', 'IB ', 1),
        Faculties('ХИМММ', 'HIMMM ', 2),
    ])
    db.session.commit()

    db.session.add_all([
        Specializations('ИиВТ', 'IIvT', 1),
        Specializations('ИБ', 'IB ', 1),
        Specializations('ХИМММ', 'HIMMM ', 2),
    ])
    db.session.commit()

    db.session.add_all([
        Groups(1, 2017),
        Groups(2, 2018),
        Groups(3, 2021),
    ])
    db.session.commit()

    db.session.add_all([
        Students('Иван', 'Васильевич', 'Пупкин', 1),
        Students('Vaavo', 'Alls', ' ', 1),
        Students('Мап', 'Фывф', 'вфыв', 2),
    ])
    db.session.commit()

    db.session.add_all([
        Teachers('Олег', 'Бозиев', 'Людинович', 'Oleg', 'Boziev', 'Lydinovich', 1),
        Teachers('Алекс', 'Роллс', ' ', 'Alex', 'Rolls', ' ', 1),
    ])
    db.session.commit()

    db.session.add_all([
        Auditoriums(1, '201'),
        Auditoriums(2, '302a'),
    ])
    db.session.commit()

    db.session.add_all([
        DiscipleTypes('Зачет', 'Test'),
        DiscipleTypes('Экзамен', 'Exam'),
        DiscipleTypes('Дифференцированный зачет', 'Differentiated test'),
        DiscipleTypes('Курсовая работа', 'Coursework'),
    ])
    db.session.commit()

    db.session.add_all([
        Disciplines('Математика', 'Math', 1, 1),
        Disciplines('Физика', 'Physics', 1, 1),
        Disciplines('Музыка', 'Music', 2, 2),
    ])
    db.session.commit()

    db.session.add_all([
        Weekdays('Понедельник', 'Monday'),
        Weekdays('Вторник', 'Tuesday '),
        Weekdays('Среда', 'Wednesday '),
        Weekdays('Четверг', 'Thursday '),
        Weekdays('Пятница', 'Friday '),
        Weekdays('Суббота', 'MondSaturday ay'),
    ])

    db.session.add_all([
        LectureNumbers('9:00', '10:35'),
        LectureNumbers('10:45', '12:20'),
        LectureNumbers('13:00', '14:35'),
        LectureNumbers('14:45', '16:20'),
    ])

    db.session.add_all([
        MarkTypes('Зачтено', 'Passed'),
        MarkTypes('Не зачтено', 'Fail'),
        MarkTypes('Отлично', 'Excellent'),
        MarkTypes('Хорошо', 'Good'),
        MarkTypes('Удовлетворительно', 'Satisfactory'),
        MarkTypes('Неудовлетворительно', 'Fail'),
    ])
    db.session.commit()

    db.session.add_all([
        Schedules(1, 1, 1, 1, 1, 1),
        Schedules(1, 2, 2, 1, 1, 2),
        Schedules(2, 1, 1, 2, 2, 1),
        Schedules(1, 5, 2, 1, 2, 2),
        Schedules(1, 5, 1, 1, 2, 4),
    ])

    db.session.add_all([
        Marks(1, 1, 1, 12, 24, 6, 1, 1, 1),
        Marks(1, 1, 2, 8, 16, 3, 1, 1, 1),
        Marks(1, 1, 2, 1, 3, 7, 2, 1, 2),
        Marks(1, 1, 5, 12, 24, 6, 1, 2, 2),
        Marks(1, 1, 4, 12, 24, 6, 1, 2, 3),
        Marks(1, 1, 3, 6, 7, 25, 3, 1, 3),
        Marks(1, 1, 3, 1, 1, 0, 1, 1, 1),
        Marks(1, 1, 1, 0, 0, 0, 2, 2, 1),
        Marks(1, 1, 2, 8, 45, 4, 1, 1, 2),
    ])

    db.session.commit()



