```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Nickname(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    generated_nickname = db.Column(db.String(100), nullable=False)

class Debate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    statement = db.Column(db.String(500), nullable=False)
    generated_response = db.Column(db.String(500), nullable=False)
    debate_simulation = db.Column(db.String(500), nullable=False)

def save_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return user.id

def save_nickname(user_id, generated_nickname):
    nickname = Nickname(user_id=user_id, generated_nickname=generated_nickname)
    db.session.add(nickname)
    db.session.commit()

def save_debate(user_id, statement, generated_response, debate_simulation):
    debate = Debate(user_id=user_id, statement=statement, generated_response=generated_response, debate_simulation=debate_simulation)
    db.session.add(debate)
    db.session.commit()
```