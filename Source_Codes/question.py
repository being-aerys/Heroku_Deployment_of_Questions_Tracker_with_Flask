# Created by Aashish Adhikari at 6:12 PM 7/16/2021
from database import db
from datetime import datetime

class Question(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Integer, default=False)
    date_saved = db.Column(db.DateTime, default=datetime. utcnow())

    def __repr__(self):
        return "Question {}".format(self.id)