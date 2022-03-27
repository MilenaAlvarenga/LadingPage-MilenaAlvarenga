from utils.db import db

class messagess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    message = db.Column(db.String(300), nullable=False)

    def __init__(self,fullname, email, message) -> None: 
        self.fullname = fullname
        self.message = message
        self.email = email

    def __repr__(self) -> str:
        return f"Messages({self.id},'{self.lastname}', '{self.message}' , '{self.email}')"
    