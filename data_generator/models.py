from data_generator import db


class FirstName(db.Model):
    __tablename__ = 'first_names'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return (f'<{self.__class__.__name__}>: {self.first_name}'
                f'<Gender>: {self.gender}')


class LastName(db.Model):
    __tablename__ = 'last_names'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return (f'<{self.__class__.__name__}>: {self.last_name}'
                f'<Gender>: {self.gender}')


class JobTitle(db.Model):
    __tablename__ = 'job_titles'
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return (f'<{self.__class__.__name__}>: {self.job_title}'
                f'<Gender>: {self.gender}')


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    voivodeship = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: {self.city}, {self.voivodeship}'
