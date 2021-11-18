from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__: "user"

    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(120), unique=False, nullable=False)
    _is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'User is {self.nick}, id: {self.id}' 

    def to_dict(self):
        tasks = Task.get_by_user(self.id)
        return {
            "id": self.id,
            "nick": self.nick,
            "tasks": [task.to_dict() for task in tasks]
        }
    
    @classmethod
    def get_all(cls):
        users = cls.query.all()
        return users

    @classmethod
    def get_by_id(cls,id):
        user = cls.query.get(id)
        return user

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def sof_delete(self):
        self._is_active = False
        db.session.commit()
        return self

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()

class Task(db.Model):
    __tablename__: "task"

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(120), unique=False, nullable=False)
    done = db.Column(db.Boolean(), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f'Task is {self.label}, id: {self.id}, done: {self.done}, user_id: {self.user_id}' 

    def to_dict(self):
        return {
            "id": self.id,
            "label": self.label,
            "done": self.done,
            "user_id": self.user_id
        }

    @classmethod
    def get_all(cls):
        tasks = cls.query.all()
        return tasks

    @classmethod
    def get_by_id(cls,id):
        task = cls.query.get(id)
        return task

    @classmethod
    def get_by_user(cls,user_id):
        tasks = cls.query.filter_by(user_id=user_id)
        return tasks

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()