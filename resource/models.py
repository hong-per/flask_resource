from resource import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)


class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region_id = db.Column(db.Integer(), db.ForeignKey(
        'region.id'))
    region = db.relationship('Region', backref=db.backref(
        'servers', cascade='all, delete-orphan'))
    host = db.Column(db.String(100), nullable=False, unique=True)
    cpu = db.Column(db.Integer(), nullable=False)
    memory = db.Column(db.Integer(), nullable=False)
    instance = db.Column(db.Integer(), nullable=False)


class Usage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer(), db.ForeignKey(
        'server.id'))
    server = db.relationship('Server', backref=db.backref(
        'logs', cascade='all, delete-orphan'))
    cpu_usage = db.Column(db.Integer(), nullable=False)
    memory_usage = db.Column(db.Integer(), nullable=False)
    instance_usage = db.Column(db.Integer(), nullable=False)
    note = db.Column(db.Text(), nullable=True)
    record_date = db.Column(db.DateTime(), nullable=False)
