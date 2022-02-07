from sqlalchemy_utils import (
    create_database,
    database_exists,
    drop_database
)

from sensyne.models import Product


def init_db(db, app):
    db.init_app(app)
    if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        drop_database(app.config['SQLALCHEMY_DATABASE_URI'])
    create_database(app.config['SQLALCHEMY_DATABASE_URI'])

    with app.app_context():
        db.create_all()
        
        db.session.add_all([
            Product(name='Lavender heart', price=9.25),
            Product(name='Personalised cufflinks', price=45.00),
            Product(name='Kids T-shirt', price=19.95),
        ])
        db.session.commit()