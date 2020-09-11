# app.py
from flask import Flask
from flask_restplus import Resource, Api, fields
from database import db_session
from models import TeacherCourse

application = Flask(__name__)
api = Api(application,
          version='0.1',
          title='Koru Mindfulness API',
          description='Smashing Boxes Koru Mindfulness API',
)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/teacher_course')
class TeacherCourse(Resource):
    model = api.model('Model', {
        'id': fields.Integer,
        'course_title': fields.String,
        'teacher_name': fields.String,
         ##add more fields here
    })
    @api.marshal_with(model, envelope='resource')
    def get(self, **kwargs):
        from models import TeacherCourse
        return TeacherCourse.query.all()

@application.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    application.run(debug=True)
