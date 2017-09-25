from models import db

from category import Category

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)
    title = db.Column(db.String(20), nullable=False)

    category = db.relation(Category)
