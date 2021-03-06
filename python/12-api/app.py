from flask import Flask, render_template, request
from flask_peewee.db import Database
from peewee import *
from flask_restful import Resource, Api
from flask_security import Security, PeeweeUserDatastore, \
    UserMixin, RoleMixin, login_required, auth_token_required, current_user
from bson import json_util
import json

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
    def __str__(self):
        return 'Email:{}, id:{}'.format(self.email, self.id)

class UserRoles(db.Model):
    # Because peewee does not come with built-in many-to-many
    # relationships, we need this intermediary class to link
    # user to roles.
    user = ForeignKeyField(User, related_name='roles')
    role = ForeignKeyField(Role, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)

class C(db.Model):
    #device = ForeignKeyField(Device)
    mac = TextField()
    name = TextField()
    owner = ForeignKeyField(User, related_name='cams')

class Device(db.Model):
    mac = TextField()
    ip = TextField()

# Setup Flask-Security
user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)

#@app.before_first_request
#def create_user():
for Model in (C, Role, User, UserRoles):
    Model.create_table(fail_silently=True)

# Api
class A(Resource):
    @auth_token_required
    def get(self):
        return {'current_user': str(current_user)}
        #return {'a': 1}

class B(Resource):
    @auth_token_required
    @login_required
    def get(self):
        return {'b': 2}

class D(db.Model):
    mac = TextField()
    ip = TextField()


class C_API(Resource):
    @auth_token_required
    def get(self):
        cams = C.select().where(C.owner == current_user.id)
        cams_out = [{'mac': cam.mac, 'name': cam.name} for cam in cams]
        return json.dumps(cams_out, default=json_util.default)
    @auth_token_required
    def post(self):
        req = request.get_json(force=True)
        c = C.create(mac=req['mac'], name=req['name'], owner=current_user.id)
        return {'id': c.id, 'c': str(c)}

class D_API(Resource):
    def get(self, mac):
        return {'mac': mac}


api.add_resource(A, '/a')
api.add_resource(B, '/b')
api.add_resource(C_API, '/c', endpoint='c')
api.add_resource(D_API, '/d/is-online/mac/<mac>', endpoint='d')


# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    #app.run(host='0.0.0.0')

