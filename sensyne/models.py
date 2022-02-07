from sensyne.db import db


class Product(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<{self.__class__.__name__} %r>' % self.productname

    @staticmethod
    def serialize(obj):
        return {
        'code': obj.code,
        'name': obj.name,
        'price': obj.price
    }