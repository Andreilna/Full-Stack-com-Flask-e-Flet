from database import db

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }

class Series(db.Model):
    __tablename__ = 'series'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }

class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }