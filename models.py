# models.py
from sqlalchemy import Table, Column, Integer, Text
from sqlalchemy.orm import mapper
from database import metadata, db_session

class TeacherCourse(object):
    query = db_session.query_property()
    def __init__(self, id=None, course_title=None, teacher_name=None):
        self.id = id
        self.course_title = course_title
        self.teacher_name = teacher_name

teacher_course = Table('teacher_course', metadata,
    Column('id', Integer, primary_key=True),
    Column('course_title', Text),
    Column('teacher_name', Text)
)

mapper(TeacherCourse, teacher_course)