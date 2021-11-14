from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), unique=False, nullable=False)
    done = db.Column(db.Boolean(), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'User is {self.task}, id: {self.id}, done: {self.done}' 

    def to_dict(self):
        return {
            "id": self.id,
            "task": self.task,
            "done": self.done,
        }

    @classmethod
    def get_all(cls):
        tasks = cls.query.all()
        return tasks

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self):
        self._is_active = False
        db.session.commit()
        return self

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()