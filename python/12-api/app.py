from flask import Flask, render_template
from flask_peewee.db import Database
from peewee import *
from flask_restful import Resource, Api
from flask_security import Security, PeeweeUserDatastore, \
    UserMixin, RoleMixin, login_required, auth_token_required

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_SALT'] = '12345678'
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECURITY_REGISTERABLE'] = True
app.config['DATABASE'] = {
    'name': 'examplpe.db',
    'engine': 'peewee.SqliteDatabase',
}


# Create Api
api = Api(app)

# Create database conection object
db = Database(app)

class Role(db.Model, RoleMixin):
    name = CharField(unique=True)
    description = TextField(null=True)

class User(db.Model, UserMixin):
    email = TextField()
    password = TextField()
    active = BooleanField(default=True)
    confirmed_at = DateTimeField(null=True)

class UserRoles(db.Model):
    # Because peewee does not come with built-in many-to-many
    # relationships, we need this intermediary class to link
    # user to roles.
    user = ForeignKeyField(User, related_name='roles')
    role = ForeignKeyField(Role, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)

class Device(db.Model):
    pass

# Setup Flask-Security
user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    for Model in (Role, User, UserRoles):
        Model.drop_table(fail_silently=True)
        Model.create_table(fail_silently=True)
    user_datastore.create_user(email='ruslan', password='password')

# Api
class A(Resource):
    @auth_token_required
    def get(self):
        return {'a': 1}

class B(Resource):
    @auth_token_required
    def get(self):
        return {'b': 2}

class HelloWorld(Resource):
    @login_required
    @auth_token_required
    def get(self):
        return {'hello': 'world'}

api.add_resource(A, '/a')
api.add_resource(B, '/b')


# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

