from flask import Flask, render_template
from flask_peewee.db import Database
from peewee import *
from flask_security import Security, PeeweeUserDatastore, \
    UserMixin, RoleMixin, login_required

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_PASSWORD_SALT'] = '12345678'
app.config['DATABASE'] = {
    'name': 'examplpe.db',
    'engine': 'peewee.SqliteDatabase',
}

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

# Setup Flask-Security
user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    for Model in (Role, User, UserRoles):
        Model.drop_table(fail_silently=True)
        Model.create_table(fail_silently=True)
    user_datastore.create_user(email='matt@nobien.net', password='password')

# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')

if __name__ == '__main__':

    print(app.config['SECURITY_PASSWORD_HASH'])
    print(app.config['SECURITY_PASSWORD_SALT'])
    app.run()

