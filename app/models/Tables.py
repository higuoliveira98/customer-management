from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.name

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    date_birth = db.Column(db.DateTime, nullable=False)
    cpf = db.Column(db.String, unique=True)
    rg = db.Column(db.String, unique=True)
    phone = db.Column(db.String, unique=True)

    def __init__(self, name ,date_birth, cpf, rg, phone):
        self.name = name
        self.date_birth = date_birth
        self.cpf = cpf
        self.rg = rg
        self.phone = phone

    def __repr__(self):
        return "<Customer %r>" % self.name

class Addressess(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String)
    district = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = db.relationship('Customer', foreign_keys=customer_id)

    def __init__(self, street, district, city, state, country, customer_id):
        self.street = street
        self.district = district
        self.city = city
        self.state = state
        self.country = country
        self.customer_id = customer_id

    def __repr__(self):
        return "<Address %r>" % self.id