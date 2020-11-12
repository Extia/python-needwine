from .. import db, flask_bcrypt


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    password_hash = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode(
            'utf-8'
        )

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)
