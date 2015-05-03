from app import db
from datetime import datetime


class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text())
    created_time = db.Column(db.DateTime())

    def __init__(self, title, text, created_time=None):
        self.title = title
        self.text = text
        if created_time is None:
            self.created_time = datetime.utcnow()
        else:
            self.created_time = created_time
