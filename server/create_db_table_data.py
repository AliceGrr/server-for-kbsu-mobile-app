from server import db
from server.models import Weekdays, LectureNumbers, DiscipleTypes, MarkTypes, Universities, UniversityResources, \
Teachers, Students, Specializations, Faculties, Groups, Institutes, Disciplines, Auditoriums, Schedules, Marks


db.drop_all()
db.create_all()


db.session.add_all([
    Universities(name_ru='Кабардино-Балкарский государственный университет', name_eng='Kabardino-Balkarian State University',
                 address='улица Чернышевского, 173 Нальчик, Кабардино-Балкарская Республика',
                 latitude=43.494545, longitude=43.596298, addictive_info=''),
])
db.session.commit()

db.session.add_all([
    UniversityResources('site', 'https://kbsu.ru/', 1),
    UniversityResources('vk', 'https://vk.com/kbsu.official', 1),
    UniversityResources('telegram', 'https://telegram.me/s/kbsu1957', 1),
])
db.session.commit()

db.session.add_all([
    Institutes(name_ru='Институт исскуственного интеллекта и цифровых технологий', name_eng='Institute of Artificial Intelligence and Digital Technologies ',
               address='ул. Чернышевского, 173, Нальчик Учебный корпус № 5', latitude=43.495282, longitude=43.594655, university_id=1),
    Institutes(name_ru='Институт информатики, электроники и компьютерных технологий', name_eng='Institute of Informatics, Electronics and Computer TechnologY',
               address='ул. Чернышевского, 173, Нальчик Учебный корпус № 4', latitude=43.495375, longitude=43.597590, university_id=1),
    Institutes(name_ru='Институт педагогики, психологии и физкультурно-спортивного образования', name_eng='Institute Of Education, Psychology and Sports Education',
               address='ул. Чернышевского, 175, Нальчик', latitude=43.495836, longitude=43.595487, university_id=1),
    Institutes(name_ru='Социально-гуманитарный институт', name_eng='Institute of History, Philology and Media',
               address='ул. Чернышевского, 173, Нальчик Учебный корпус № 11', latitude=43.494768, longitude=43.596139, university_id=1),
])
db.session.commit()

db.session.add_all([
    Faculties(name_ru='Информатики и Компьютерных технологий', name_eng='Computer Science and Computer Technology', institute_id=1),
    Faculties(name_ru='Информационной безопасности', name_eng='Information security', institute_id=1),
    Faculties(name_ru='Математики и физики', name_eng='Mathematicians and physicists', institute_id=1),
])
db.session.commit()

db.session.add_all([
    Specializations(name_ru='Информатика и вычислительная техника', name_eng='Computer science and engineering', faculty_id=1),
    Specializations(name_ru='Информационная безопасность', name_eng='Information security', faculty_id=2),
    Specializations(name_ru='Прикладная информатика', name_eng='Applied Computer Science', faculty_id=1),
])
db.session.commit()

db.session.add_all([
    Groups(specialization_id=1, enter_year=2018),
    Groups(specialization_id=1, enter_year=2020),
    Groups(specialization_id=2, enter_year=2017),
    Groups(specialization_id=3, enter_year=2021),
])
db.session.commit()

db.session.add_all([
    Students(id=1802784, first_name='Олеся', last_name='Галяева', patronymic='Владимировна', group_code=1),
    Students(id=2000548, first_name='Иван', last_name='Пупкин', patronymic='Васильевич', group_code=2),
    Students(id=1800218, first_name='Мурад', last_name='Лугуев', patronymic='Магдиевич', group_code=1),
    Students(id=2102158, first_name='Bobalo', last_name='Alex', patronymic='', group_code=3),
])
db.session.commit()

db.session.add_all([
    Teachers(name_ru='Бозиев Олег Людинович', name_eng='Boziev Oleg Ludinovich', faculty_id=1),
    Teachers(name_ru='Акбашева Галина Амировна', name_eng='Akbasheva Galina Amirovna', faculty_id=1),
    Teachers(name_ru='Акбашева Евгения Амировна', name_eng='Akbasheva Evgeniya Amirovna', faculty_id=1),
    Teachers(name_ru='Хаширова Татьяна Юрьевна', name_eng='Hashirova Tatiana Yurievna', faculty_id=1),
])
db.session.commit()

db.session.add_all([
    Auditoriums(institute_id=1, number='314'),
    Auditoriums(institute_id=2, number='201a'),
    Auditoriums(institute_id=3, number='02'),
    Auditoriums(institute_id=4, number='47'),
    Auditoriums(institute_id=2, number='50a'),
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
    Disciplines(name_ru='Иностранный язык в профессиональной сфере', name_eng='Foreign language in the professional sphere', disciple_type_id=2, faculty_id=3),
    Disciplines(name_ru='Специальные главы информатики', name_eng='Special chapters of Computer science', disciple_type_id=1, faculty_id=1),
    Disciplines(name_ru='Нейрокомпьютерные системы', name_eng='Neurocomputer systems', disciple_type_id=1, faculty_id=1),
    Disciplines(name_ru='Технологии разработки программного обеспечения', name_eng='Software development technologies', disciple_type_id=4, faculty_id=1),
    Disciplines(name_ru='Системы программирования', name_eng='Programming systems', disciple_type_id=3, faculty_id=1),
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
    Schedules(group_id=1, weekday_id=1, auditorium_number_id=1, disciple_id=1, teacher_id=1, lecture_number_id=1),
    Schedules(group_id=2, weekday_id=2, auditorium_number_id=2, disciple_id=2, teacher_id=2, lecture_number_id=1),
    Schedules(group_id=3, weekday_id=1, auditorium_number_id=5, disciple_id=4, teacher_id=3, lecture_number_id=1),
    Schedules(group_id=1, weekday_id=1, auditorium_number_id=4, disciple_id=3, teacher_id=2, lecture_number_id=2),
    Schedules(group_id=1, weekday_id=2, auditorium_number_id=2, disciple_id=5, teacher_id=4, lecture_number_id=2),
    Schedules(group_id=1, weekday_id=3, auditorium_number_id=3, disciple_id=1, teacher_id=3, lecture_number_id=3),
    Schedules(group_id=1, weekday_id=4, auditorium_number_id=5, disciple_id=5, teacher_id=1, lecture_number_id=4),
    Schedules(group_id=1, weekday_id=1, auditorium_number_id=4, disciple_id=2, teacher_id=2, lecture_number_id=2),
    Schedules(group_id=1, weekday_id=1, auditorium_number_id=2, disciple_id=4, teacher_id=1, lecture_number_id=1),
])

db.session.add_all([
    # student_id, group_id, disciple_id, disciple_type,
    # teacher_id, study_period, first_study_point_score=None,
    # second_study_point_score=None, third_study_point_score=None, mark_id=None
    Marks(student_id=1802784, group_id=1, disciple_id=1, disciple_type=2, teacher_id=1, study_period=1, first_study_point_score=24, second_study_point_score=8),
    Marks(student_id=1802784, group_id=1, disciple_id=2, disciple_type=4, teacher_id=2, study_period=3, first_study_point_score=16, second_study_point_score=4, third_study_point_score=20, mark_id=3),
    Marks(student_id=1802784, group_id=1, disciple_id=2, disciple_type=1, teacher_id=2, study_period=1, first_study_point_score=3, second_study_point_score=0, third_study_point_score=1, mark_id=6),
    Marks(student_id=1802784, group_id=1, disciple_id=3, disciple_type=3, teacher_id=1, study_period=4, first_study_point_score=1),
])

db.session.commit()